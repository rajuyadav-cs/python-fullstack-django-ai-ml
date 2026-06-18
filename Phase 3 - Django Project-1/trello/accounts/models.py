from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices

class UserRole(TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    MANAGER = 'MANAGER', 'Manager'
    DEVELOPER = 'DEVELOPER', 'Developer'
class User(AbstractUser):
    
    role = models.CharField(
        max_length= 20,
        choices= UserRole.choices,
        default = UserRole.DEVELOPER 
    )
    profile_image = models.ImageField(upload_to= 'profile_images', blank= True, null= True)
    phone_number = models.CharField(max_length=15, blank= True, )
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    
    
    def __str__(self):
        return self.username
