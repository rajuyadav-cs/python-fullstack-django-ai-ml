from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def posts(request):
    return HttpResponse("Post page")