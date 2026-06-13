from django.shortcuts import render, redirect
from genshin.models import CharInfo
from django.core.paginator import Paginator
from .forms import CharInfoForm
# Create your views here.
def home(request):
    chars = CharInfo.objects.all()

    paginator = Paginator(chars, 4)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'genshin/index.html', {
        'page_obj': page_obj
    })
    
def charform(request):
    
    if request.method == 'POST':
        form = charform(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('charform')
    
    form = CharInfoForm()
    
    return render(request, 'genshin/charform.html', {'form': form})    