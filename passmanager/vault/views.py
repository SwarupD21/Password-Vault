from django.shortcuts import render
from .models import Password
from django.contrib.auth.models import User
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .utils import encrypt_password,decrypt_password
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, "home.html")

@login_required()
def vault_view(request):
    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        login_identifier=data.get("login_identifier")
        plain_password =data.get("encrypted_password")
        notes=data.get("notes")
        encrypted_password = encrypt_password(plain_password)
        Password.objects.create(
            user=request.user,
            name=name,
            login_identifier=login_identifier,
            encrypted_password=encrypted_password,
            notes=notes,
        )
        return redirect('vault_view')
    queryset=Password.objects.filter(user=request.user)
    context={'passmanage':queryset}
    return render(request,'vault.html',context)

@login_required
def edit_pass(request,id):
    queryset=get_object_or_404(Password,id=id,user=request.user)
    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        login_identifier=data.get("login_identifier")
        notes=data.get("notes")
        plain_password=data.get("encrypted_password")

        if plain_password:
            encrypted_password = encrypt_password(plain_password)
            queryset.encrypted_password=encrypted_password
        queryset.name=name
        queryset.login_identifier=login_identifier
        queryset.notes=notes
        queryset.save()
        return redirect("vault_view")
    return render(request,"edit_password.html",{"entry":queryset})

@login_required
def pass_delete(request,id):
    queryset=get_object_or_404(Password,id=id,user=request.user)
    if request.method == "POST":
        queryset.delete()
        return redirect("vault_view")

    return render(request, "delete_password.html", {"entry": queryset})

@login_required
def show_password(request, id):
    entry = get_object_or_404(Password, id=id, user=request.user)
    decrypted_password = decrypt_password(entry.encrypted_password)
    context = {
        "entry": entry,
        "password": decrypted_password
    }
    return render(request, "show_password.html", context)

# def register(request):
#     if request.user.is_authenticated:
#         return redirect("vault_view")

#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         if not username or not password:
#             messages.error(request, "All fields are required ❌")
#             return redirect("register")

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists ❌")
#             return redirect("register")

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )

#         login(request, user)
#         messages.success(request, "Account created 🎉")
#         return redirect("vault_view")

#     return render(request, "register.html")


# def logged_in(request):
#     if request.user.is_authenticated:
#         return redirect("vault_view")

#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             messages.success(request, "Welcome back 🔐")
#             return redirect("vault_view")

#         messages.error(request, "Invalid username or password ❌")

#     return render(request, "login.html")

# def logout_user(request):
    # logout(request)
    # messages.info(request, "Logged out 👋")
    # return redirect("logged_in")