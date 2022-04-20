import email
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home_app.models import Contact
# Create your views here.

def home(request):
    context = {"variable1" : "Vaariable 1 got 50 cars", "variable2" : "Variable 2 got 20 cars"}
    return render(request, 'index.html', context)
    # return HttpResponse("This is my Home page")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is About page")
def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is Services page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = request.POST.get('name')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    
    return render(request, 'contact.html')
    #return HttpResponse("This is Contact page")                            

