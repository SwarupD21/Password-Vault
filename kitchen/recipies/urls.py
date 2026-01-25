from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipies, name='recipies'),
    path('register/', views.register, name='register'),
    path('login/', views.loggedin, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_recipe/<int:id>/', views.delete_recipe, name="delete_recipe"),
    path('update_recipe/<int:id>/', views.update_recipe, name="update_recipe"),
]