from django.urls import path
from . import views
from .views import SignupView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.home, name ='home'),
    path('signup/',SignupView.as_view(template_name = 'account/signup.html'),name= 'signup'),
    path('login/', LoginView.as_view(template_name = 'account/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(), name= 'logout')
]
