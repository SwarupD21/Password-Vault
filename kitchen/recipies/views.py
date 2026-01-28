from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import menu
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import decorators

# Create your views here.

@login_required
def recipies(request):
    if request.method=="POST":
        data = request.POST
        recipe_name = request.POST.get('recipe_name')
        recipe_desc = request.POST.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')
        menu.objects.create(
            recipe_name=recipe_name,
            recipe_desc=recipe_desc,
            recipe_img=recipe_img,
            user = request.user
        )
        return redirect('/recipies/')
    queryset = menu.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    context = {'recipies':queryset}
    return render(request,'recipe.html',context)

def delete_recipe(request,id):
    queryset = menu.objects.get(id=id,user=request.user)
    queryset.delete()
    return redirect('/recipies/')

def update_recipe(request,id):
    queryset = menu.objects.get(id=id,user=request.user)
    
    if request.method == "POST":
        data = request.POST
        recipe_name = request.POST.get('recipe_name')
        recipe_desc = request.POST.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        if recipe_img:
            queryset.recipe_img = recipe_img
        queryset.save()
        return redirect('/recipies/')
    context = {'recipies':queryset}
    return render(request,'update_recipe.html',context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("login")
    return render(request, "register.html")

def loggedin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)   # session created
            return redirect("/recipies/")
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("login")

