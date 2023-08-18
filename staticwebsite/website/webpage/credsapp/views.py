from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['Username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method =='POST':
        username = request.POST['Username']
        firstname = request.POST['First_Name']
        lastname = request.POST['Last_Name']
        email = request.POST['Email']
        password = request.POST['Password1']
        cpassword = request.POST['Password2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                print("Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
                print("Email already registered")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save();
                return redirect('login')
                print("User created Successfully")

        else:
           messages.info(request,'password does not match')
           print('password does not match')
           return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')