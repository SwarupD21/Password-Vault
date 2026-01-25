from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    # path("login",views.logged_in,name="logged_in"),
    # path("logout",views.logout_user,name="logout_user"),
    # path("register",views.register,name="register"),
    path("vault/",views.vault_view,name="vault_view"),
    path("show/<int:id>/", views.show_password, name="show_password"),  
    path("edit/<int:id>",views.edit_pass,name="edit_pass"),
    path("delete/<int:id>",views.pass_delete,name="pass_delete"),
]