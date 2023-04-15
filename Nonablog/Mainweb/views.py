from django.shortcuts import render

def index_viwe(request):
    return render(request,'website/index.html') 

def contact_viwe(request):
    return render(request,'website/contact.html') 

def about_viwe(request):
    return render(request,'website/about.html') 

def elements_viwe(request):
    return render(request,'website/elements.html') 