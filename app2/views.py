from django.shortcuts import render
from django.http import HttpResponse
from .form import contactForm, registerForm

# Create your views here.
def landingPageView(request):
    return render(request,'landingPage.html')
def pricingPageView(request):
    return render(request,'pricingPage.html')
def contactPageView(request):
    if request.method=='POST':
        f=contactForm(request.POST)
        if f.is_valid():
            print("Your response is recorded")
        else:
            print("Your Request is failed")
    return render(request,'contactPage.html')
def pricingPageView2(request):
    return render(request,'pricingPage2.html',{"items":items})
def registerPageView(request):
    return render(request,"register.html",{'form':form})

# my_name="Eeksha"
users=[
    {"name":"Eeksha", "age": 21},
    {"name":"Prajwal", "age": 56},
    {"name":"ABC", "age": 30}
]
items=[
    {"title":"Personal", "des":"For individuals and small teams looking to manage their tasks.", },
    {"title":"Starter"},
    {"title":"Advanced"}
]
def greetPageView(request):
    return render(request,'greetPage.html',{"users":users})
