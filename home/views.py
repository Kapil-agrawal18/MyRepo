from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is home page")

def login(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=first_name,email=email,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("items")
        else:
            messages.info(request,'invalid credentials')
            return redirect("/login")

    else:
        return render(request,'login.html')

def index_2(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        password1 = request.POST['password1']

        if User.objects.filter(email=email).exists():
            messages.info(request,'email already taken')
            return redirect("index_2")
        else:
            user = User.objects.create_user(email=email, first_name=first_name, password=password1, username=first_name,)
            user.save();
            messages.info(request,'user created now you can login from login page')
            return redirect("login")
    else:
        return render(request,'index_2.html')

def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')

def items(request):
    return render(request,'items.html')



    #username=kapil
    #password=kap@123il
