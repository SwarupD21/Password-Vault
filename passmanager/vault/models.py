from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Password(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='vault_entries')
    name = models.CharField(max_length=500)
    login_identifier = models.CharField(max_length=255)
    encrypted_password = models.TextField()
    notes = models.TextField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.login_identifier})"