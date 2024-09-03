from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from django .contrib import messages
from home.models import Contact,Destination,TicketBooking

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

def Login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or Password is incorrect")
            
        
    return render(request,'login.html')

def signup(request):

    if request.method =="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')


        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('signup')

        if password!=confirm_password:
            messages.error(request,"Password does not match")
            return redirect('signup')
        else:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            return redirect('home')

    return render(request,'signup.html')


def logOut(request):
    logout(request)
    return redirect('login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        
        con=Contact(name=name,email=email,phone=phone,message=message)
        con.save()

    return render(request,'contact.html')

def tickets(request):
    if request.method =="POST":
        if 'placename' in request.POST:
            name=request.POST.get('name')
            email=request.POST.get('email')
            placename=request.POST.get('placename')
            cityname=request.POST.get('cityname')
            hotelname=request.POST.get('hotelname')

            arabian_places =["Dubai" ,"Kuwait","Bahrain","Abu dhabi","Riyadh","Qatar","Saudi Arabia"]

            if placename not in arabian_places:
                messages.error(request,"Please Enter any arabian country")
                return redirect('tickets')

            dest =Destination(name=name,email=email,placename=placename,cityname=cityname,hotelname=hotelname)
            dest.save()
        elif 'seats' in request.POST:
            urcity =request.POST.get('urcity')
            todest=request.POST.get('todest')
            day=request.POST.get('day')
            seats=request.POST.get('seats')
            message=request.POST.get('message')

            booking =TicketBooking(urcity=urcity,todest=todest,day=day,seats=seats,message=message)
            booking.save()
            

    return render(request,'tickets.html')

def bahrain(request):
    return render(request,'bahrain.html')

def abudhabi(request):
    return render(request,'abudhabi.html')

def riyadh(request):
    return render(request,'riyadh.html')

def qatar(request):
    return render(request,'qatar.html')

def kuwait(request):
    return render(request,'kuwait.html')

def saudiarabia(request):
    return render(request,'saudi_arabia.html')
