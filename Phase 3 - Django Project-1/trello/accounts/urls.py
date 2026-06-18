from django.urls import path
from .views import RegisterView, LoginView, DashBoard,Logout, ProfileView
urlpatterns = [
    path('register',RegisterView.as_view(), name= 'register'),
    path('login',LoginView.as_view(template_name = 'accounts/login.html'), name= 'login'),
    path('dashboard',DashBoard.as_view(), name= 'dashboard'),
    path('logout', Logout.as_view(), name= 'logout'),
    path('profile', ProfileView.as_view(), name= 'profile')
]

