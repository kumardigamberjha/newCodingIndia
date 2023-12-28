from django.shortcuts import render, redirect
from Registration.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from CodingIndia.settings import EMAIL_HOST_USER
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def VerifyOTP(request):
    if request.method == "POST":
        userotp = request.POST.get('otp')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')   
        email = request.POST.get('email')  
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        if password1 == password2:
            form = User(first_name=first_name, last_name=last_name, email=email, username=username, password = password1)
            form.set_password(password1)
            form.save()
            print("Custom User Save")

        print("USername: ", username)
        print("Password: ", password1)

        user = authenticate(request, username=username, password=password1)
        print("User: ", user)
        if user is not None:
            print("Login Done")
            login(request, user)
            return JsonResponse({'data': 'Hello'}, status=200)

        messages.success(request, 'Custom User Save')
    
    return JsonResponse({'data': 'Hello'}, status=200)



def SignUpView(request):
    form = CreateUserForm()
    user = request.user
    

    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        # phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print("Email: ", email, username)
        form = CreateUserForm(request.POST)
        if not User.objects.filter(email=email).exists():
            if form.is_valid():
                otp = random.randint(100000, 999999)
                print("Hello")
                send_mail("User Data: ", f"Verify Your Mail by the OTT: /n {otp}", EMAIL_HOST_USER, [email], fail_silently=True) 
                messages.success(request, 'User saved Successfully')
                return render(request, 'Registration/otp.html', {'otp': otp, 'first_name': first_name, 'last_name': last_name, 'email': email,'username': username, 'password1': password1, 'password2': password2})
            else:
                print("Form Error: ", form.errors)
                messages.error(request, form.errors)
        else:
            print("Email Already Exists", form.errors)
            messages.error(request, "Email Already Available")
    context = {'form': form}
    return render(request, 'Registration/Signup.html', context)



@csrf_exempt
def VerifyLoginOTP(request):
    if request.method == "POST":
        userotp = request.POST.get('otp')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login Done")
            print("OTP: ", userotp)
    return JsonResponse({'data': 'Hello'}, status=200)
 

def LoginView(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=email).username
        except:
            username = None
        print("Username: ", username)
        print("password: ", password)
        print("Email: ", email)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            otp = random.randint(100000, 999999)
            # print("OTP: ", otp)
            send_mail("User Data: ", f"Verify Your Mail by the OPT: /n {otp}", EMAIL_HOST_USER, [email], fail_silently=True)

            return render(request, 'Registration/signinotp.html', {'otp': otp, 'username': username, 'password': password})   
        else:
            messages.error(request, 'Invalid Entry')
            # print("Some error")
    context = {}
    return render(request, 'Registration/Signup.html', context)



def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('/')



################ GET USER DATA ###################
@csrf_exempt
def Getusername(request):
    if request.method == "POST":
        username = request.POST.get("username")
        #print("username: ", username)
        if User.objects.filter(username=username).exists():
            #print("username Exists")
            amount = "Username Exists"
            return JsonResponse({'amount' : amount}, status=200)
        else:
            amount = "Looking good"
            return JsonResponse({'amount' : amount}, status=200)



@csrf_exempt
def GetEmail(request):
    if request.method == "POST":
        email = request.POST.get("email")
        #print("username: ", email)
        if User.objects.filter(email=email).exists():
            #print("Email Exists")
            amount = "Email Exists"
            return JsonResponse({'amount' : amount}, status=200)
        else:
            amount = "Looking good"
            return JsonResponse({'amount' : amount}, status=200)
        
    
