from django.contrib.auth.forms import UserCreationForm
from .models import Signupmodel

class Signupform(UserCreationForm):
    
    class Meta:
        
        model = Signupmodel
        fields = [
            'username', 'email', 'phone', 'password1', 'password2'
        ]
        