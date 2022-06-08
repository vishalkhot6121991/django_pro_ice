from datetime import date, datetime
from email import message
from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context={
        'variable':'this is send'
    }
    messages.success(request,"This is test message")
    return render(request,'index.html',context)
   # return HttpResponse("this is homepage")
def about(request):
    return render (request,'about.html',)
   # return HttpResponse("this is about page")
def services(request):
    return render (request,'services.html',)
   # return HttpResponse("this is servicespage")
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name'),
        phone=request.POST.get('phone'),
        email=request.POST.get('email'),
        password=request.POST.get('password'),
        contact=Contact(name=name,phone=phone,email=email,password=password,date=datetime.today())
        contact.save()
        messages.success(request, 'your message have been send vishal servers!')
    return render (request,'contact.html',)
    #return HttpResponse("this is contactpage")



