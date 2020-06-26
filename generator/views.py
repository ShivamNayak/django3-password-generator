from django.shortcuts import render
from django.http import HttpResponse
from random import choice

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    
    store=list('abcdefghijklmnopqrstuvwxyz')
    
    
    if request.GET.get('uppercase'):
        store.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('number'):
        store.extend(list('1234567890'))
    
    if request.GET.get('special'):
        store.extend(list('!@#$%^&*'))
    
    length=int(request.GET.get('length',8))
    
    password_variable = ''
    
    while(length>0):
        length-=1
        password_variable+=choice(store)    
    
    return render(request,'generator/password.html',{'password':password_variable})

def about(request):
    return render(request,'generator/about.html')

#def home(request):
#   return HttpResponse('Hello There friend')

#def home(request):
#    return render(request,'generator/home.html',{'password':'ijdijvdij'})
