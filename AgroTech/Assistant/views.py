from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from datetime import datetime
#from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from Assistant.models import Sgn
from Assistant.models import Suppsgn,SupplierOrder


def landing_page(request):
    return render(request, 'landing_page.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
    
    # If GET request or authentication failed, show login form
    return render(request, 'admin_login.html', {'form': UserCreationForm()})

def signup(request):
    if request.method == 'POST':   #it will run only when a form is post otherwise only rendering will be done
        username = request.POST['Username']   #here request.POST is a library and .get is a function
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        address = request.POST['address']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1!=password2:
            return HttpResponse("Password Mismatched")
        else:
            myuser = User.objects.create_user(username,email,password1)  #Create a user for me whose details are this
            myuser.first_name=fname
            myuser.last_name=lname

            myuser.save()

            signup = Sgn(username=username,fname=fname,lname=lname, email=email,address=address,date = datetime.today())
            signup.save()
            messages.success(request,"You are successfully registered.")
            return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':   
        username = request.POST['Username']  
        password1 = request.POST['pass1']

        user = authenticate(request,username=username, password=password1)
        
        if user is not None:
            login(request, user)
            #fname = user.first_name
            return redirect('farmerDashboard')            #{'fname': fname}
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('signin')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('signin')

def farmerDashboard(request):
    return render(request,'farmerDashboard.html')

def FarmOrder(request):
    FarmerOrder = SupplierOrder.objects.all()
    return render(request,'FarmOrder.html',{'FarmerOrder': FarmerOrder})

def suppliersignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email=request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()

            suppliersignup = Suppsgn(username=username,fname=fname,lname=lname,email=email,phone=phone, address=address,date = datetime.today())
            suppliersignup.save()
            return redirect('suppliersignin')
    return render(request,'suppliersignup.html')

def suppliersignin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('supplier')
        else:
            messages.success(request, "Username or Password is incorrect!!!")
            return render(request,'suppliersignin.html')
    return render(request,'suppliersignin.html')

def Sppsignout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('suppliersignin')

def supplier(request):
    return render(request,'supplier.html')

def PlaceOrder(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        cropName = request.POST.get('cropName')
        cropQuantity = request.POST.get('cropQuantity')
        address = request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
          
        PlaceOrder = SupplierOrder()
        PlaceOrder.name = name
        PlaceOrder.email = email
        PlaceOrder.phone = phone
        PlaceOrder.crop_name = cropName
        PlaceOrder.crop_quantity = cropQuantity
        PlaceOrder.address = address
        PlaceOrder.city = city
        PlaceOrder.state = state
        PlaceOrder.zip = zip
        PlaceOrder.date = datetime.today()

        PlaceOrder.save()
        messages.success(request,"Your Order is being placed successfully, now wait for farmer's response")
        return redirect('supplier')
    return render(request,'PlaceOrder.html')


def AIF(request):
    return render(request,'AIF.html')
def CFFF(request):
    return render(request,'CFFF.html')
def CIS(request):
    return render(request,'CIS.html')
def KMDY(request):
    return render(request,'KMDY.html')
def Krishi(request):
    return render(request,'Krishi.html')
def MAS(request):
    return render(request,'MAS.html')
def NMOEO(request):
    return render(request,'NMOEO.html')
def NMONF(request):
    return render(request,'NMONF.html')
def PMFBY(request):
    return render(request,'PMFBY.html')
def PMKSN(request):
    return render(request,'PMKSN.html')
def PMKSY(request):
    return render(request,'PMKSY.html')

def weather(request):
    return render(request, 'weather.html')

def index(request):
    return render(request, 'index.html')

def YourOrder(request):
    FarmerOrder = SupplierOrder.objects.all()
    return render(request,'YourOrder.html',{'FarmerOrder': FarmerOrder})