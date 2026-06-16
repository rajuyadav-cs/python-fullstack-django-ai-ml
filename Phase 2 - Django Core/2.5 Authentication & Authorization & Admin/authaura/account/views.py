from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

class Index(View):
    
    def get(request):
        
        return render(request, 'account/index.html')