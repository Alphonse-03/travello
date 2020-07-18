from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        customer_name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        confirm=request.POST['password2']

        if password == confirm:

            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                return redirect('register')
               
            else:
                user=User.objects.create_user(first_name=customer_name,password=password,email=email,username=username)
                user.save();
                print("created")
                return redirect("login")
                
            
        
        else:
            messages.info(request,"Password is not matching")
            return redirect('register')

        return redirect("/")

    else:
        return render(request,"registration.html")

def login(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else:
            messages.info(request,"You are not a reistered member please register and then login")
            return redirect("login")   
            
        
    else:
        return render(request,"login.html")