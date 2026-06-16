from django.shortcuts import render
from .models import Signupmodel
from .forms import Signupform
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

def home(request):
    
    return render(request, 'account/home.html')

class SignupView(CreateView):
    
    form_class = Signupform
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    
    template_name = 'account/login.html'
    redirect_authenticated_user = True 
    
class UserLogoutView(LogoutView):
    
    next_page = 'login'    
 
    