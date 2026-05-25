from django.contrib import admin
from django.urls import path, include
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('blogs/', include('blogs.urls')),
    path('shop/', include('shop.urls')),
]