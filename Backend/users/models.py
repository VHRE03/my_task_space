from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    is_superuser = models.BooleanField(default=False)
    groups = None
    user_permissions = None
    is_staff = None
    is_active = None
    last_login =None
    date_joined = None
    
    def __str__(self):
        return self.username