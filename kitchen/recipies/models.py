from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your models here.
class menu(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_desc = models.TextField()
    recipe_img = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.recipe_name