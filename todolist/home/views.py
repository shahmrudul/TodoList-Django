from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.
def home(request):
    return render(request,'home.html')
@never_cache
def todolist(request):
   return render(request,'todolist.html')

def register(request):
    if request.method=='POST':
      firstname=request.POST['firstname']
      lastname=request.POST['lastname']
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      if User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Taken,Please Try Different One')
            return redirect('register')
      else:
            user=User.objects.create_user(first_name=firstname, last_name= lastname,username=username,password=password,email=email)
            user.save();
            print('User created')
            return redirect('login')



    else:
     return render(request,'register.html')
@never_cache   
def login(request):
 if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
            auth.login(request,user)
            return redirect('todolist')

    else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

 else:
  return render(request,'login.html')
@never_cache
def logout(request):
   auth.logout(request)
   return redirect('/')

