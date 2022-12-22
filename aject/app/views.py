from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import Contact

def home(request):
    return render(request,'index.html')


def register(request):
 if request.method == 'POST':
    username= request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password== password2:
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Already Used!')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Used!')
            return redirect('register')
        else:
            user= User.objects.create_user(username=username,email=email,password=password2)
            user.save();
            return redirect('login')
    else:
        messages.info(request,'Password Not The Same!')
        return redirect('register')
 else:
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid!')
            return redirect('login')

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def blog(request):
    return render(request,'blog.html')


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        if len(name)<2 or len(email)<3 or len(message)<5:
           messages.error(request,'Please fiil the form correctly!')
           contact.name = name
           contact.email = email
           contact.message = message

        else:
            contact.name = name
            contact.email = email
            contact.message = message
            contact.save()
            messages.success(request,'Your message has been sent ')
    return render(request, 'contact.html')
