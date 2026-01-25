from django.contrib import admin
from .models import Password

# Register your models here.
@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "login_identifier",
        "user",
        "created_at",
    )
    search_fields=(
        "name",
        "login_identifier",
        "created_at",
    )
    readonly_fields = (
        "encrypted_password",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)
    def has_change_permission(self, request, obj=None):
        return False