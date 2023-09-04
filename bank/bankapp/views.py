from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from . models import District

# Create your views here.

def homepage(request):
    # return render(request,"index.html")
    districts = District.objects.all()
    demo = {'districts': districts}
    return render(request, 'index.html',demo)

# def district_list(request):
#     districts = District.objects.all()
#     demo = {'districts':districts}
#     return render(request, 'index.html', demo)

def redirect_to_wikipedia(request, district_id):
    district = District.objects.get(id=district_id)
    return redirect(request,district.wikipedia_link)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('button')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):
     if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                print("user created")
                return redirect('login')

        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
     return   render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def button(request):
    return render(request,"button.html")
def form(request):
    return render(request,"form.html")



