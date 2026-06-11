from django.shortcuts import render

# Create your views here.
def home(request):
    
    content = {
        'name':'furina',
    }
    
    return render(request, 'genshin/index.html',content)