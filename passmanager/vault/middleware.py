import time
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class VaultAutoLockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # 🔒 DO NOT auto-lock auth pages
        if request.path.startswith("/accounts/"):
            return self.get_response(request)

        if not request.user.is_authenticated:
            return self.get_response(request)

        last_activity = request.session.get("last_activity")
        now = time.time()

        if last_activity:
            if now - last_activity > settings.VAULT_AUTO_LOCK_TIME:
                request.session.flush()
                return redirect('/accounts/login/')

        request.session["last_activity"] = now
        return self.get_response(request)
