from django.shortcuts import render, redirect
from genshin.models import CharInfo
from django.core.paginator import Paginator
from .forms import CharInfoForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.
def home(request):
    return render(request, 'genshin/home.html')



def signup(request):
    
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
    
    else:
        form = UserCreationForm()
                
    return render(request, 'genshin/signup.html', {'form':form})

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    
    else:
        form = AuthenticationForm()
            
    
    return render(request, 'genshin/login.html', {'form' : form})

def listpage(request):
    chars = CharInfo.objects.all()

    paginator = Paginator(chars, 4)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'genshin/listpage.html', {
        'page_obj': page_obj
    })
    
def CharForm(request):
    
    if request.method == 'POST':
        form = CharInfoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('CharForm')
    
    else:
        form = CharInfoForm()
    
    return render(request, 'genshin/charform.html', {'form': form})    