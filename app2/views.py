from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import contactForm, registerForm, loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def landingPageView(request):
    return render(request,'landingPage.html')
def pricingPageView(request):
    return render(request,'pricingPage.html')
def contactPageView(request):
    message=''
    if request.method=='POST':
        f=contactForm(request.POST)
        if f.is_valid():
            print("Your response is recorded")
        else:
            print("Your Request is failed")
            return render(request,'contactPage.html',{'form':f})
    else:
        f=contactForm()
    return render(request,'contactPage.html',{"form":f, 'message':message})

items=[
    {"title":"Personal", "des":"For individuals and small teams looking to manage their tasks.", },
    {"title":"Starter"},
    {"title":"Advanced"}
]
def pricingPageView2(request):
    return render(request,'pricingPage2.html',{"items":items})

def registerPageView(request):
    form = registerForm()
    if request.method=='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Hurry!! Account Created Successfully !!")
            return redirect('loginPage')
    return render(request,"register.html",{'form':form})

def loginView(request):
    form=loginForm(request.POST)
    if request.method=="POST":
        form=loginForm(request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            pwd=form.cleaned_data['password']

            user=authenticate(request,username=un,password=pwd)
            
            if user is not None:
                login(request,user)
                return redirect('dashboardPage')
            else:
                return render(request,'loginPage.html',{'form':form})
        else:
            return render(request,'loginPage.html',{'form':form})
        
    return render(request, 'loginPage.html', {'form':form})

def dashboardView(request):
    return render(request, 'dashboard.html')

def logOutView(request):
    logout(request)
    return redirect('landingPage')
# my_name="Eeksha"
users=[
    {"name":"Eeksha", "age": 21},
    {"name":"Prajwal", "age": 56},
    {"name":"ABC", "age": 30}
]

def greetPageView(request):
    return render(request,'greetPage.html',{"users":users})
