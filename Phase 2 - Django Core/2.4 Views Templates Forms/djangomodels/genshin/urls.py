from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('listpage', views.listpage, name='listpage'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login_view, name = 'login'),
    path('CharForm', views.CharForm, name = 'CharForm')
]
