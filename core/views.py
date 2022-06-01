from django.shortcuts import render, HttpResponse #

# Create your views here.

"""
Inicio home/
Historia about /
Servicio services/
Visitanos store/
Contacto contact/
Blog blog/
Sample sample/
"""

def home(request):
    #return HttpResponse("Inicio")
    return render(request, 'core/home.html')

def about(request):
    #return HttpResponse("Historia")
    return render(request, 'core/about.html')

def store(request):
    #return HttpResponse("Visitanos")
    return render(request, 'core/store.html')

def contact(request):
    #return HttpResponse("Contacto")
    return render(request, 'core/contact.html')

def blog(request):
    #return HttpResponse("Blog")
    return render(request, 'core/blog.html')

def sample(request):
    #return HttpResponse("Sample")
    return render(request, 'core/sample.html')