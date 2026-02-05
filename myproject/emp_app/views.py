# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.models import User


# Home Page
def default(request):
    return render(request, 'emp_app/default.html')
    
def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
                messages.error(request, "Invalid Credentials !")
                return redirect(settings.LOGIN_URL)

    return render(request, 'accounts/login.html')


def logoutView(request):
    logout(request)
    return render(request, 'accounts/logout.html')

def signupView(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    if request.method == 'POST':
        if User.objects.filter(username = username):
            messages.error(request, 'Username already exists!')
            return redirect('signup')
        elif User.objects.filter(email=email):
            messages.error(request,"Email already taken!")
            return redirect('signup')
        else:
            user = User.objects.create(
                username = username,
                email = email,
                first_name = first_name,
                last_name = last_name
            )
            user.set_password(password)
            user.save()
            messages.info(request, 'User Registration Success! Please login.')
            return redirect('login')


    return render(request, 'accounts/signup.html')

@login_required
def HomePage(request):
    users = employee.objects.all()
    context = {'users': users}
    return render(request, "emp_app/index.html", context)

# About Page
def AboutUS(request):
    return render(request, "emp_app/about.html")

# Services Page
def Services(request):
    return render(request, "emp_app/services.html")

# Add New employee
@login_required
def Add_emp(request):
    if request.method == "POST":
        name = request.POST.get("name")
        empid = request.POST.get("empid")
        dept = request.POST.get("dept")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        salary= request.POST.get("salary")
        
        if name and empid and dept and address and phone and email and salary:
            user = employee(name=name, empid=empid, dept=dept, address=address, phone=phone, email=email,salary=salary)
            user.save()
            messages.success(request, "employee added successfully!")
            return redirect("home")
        else:
            messages.error(request, "All fields are required! ")

    return render(request, "emp_app/add_emp.html")

# Edit employee Details
@login_required
def Editemp(request, id):
    user = get_object_or_404(employee, id=id)

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.empid = request.POST.get("empid")
        user.dept = request.POST.get("dept")
        user.address = request.POST.get("address")
        user.phone = request.POST.get("phone")
        user.email = request.POST.get("email")
        user.salary = request.POST.get("salary")
        user.save()
        messages.success(request, "employee details updated successfully!")
        return redirect("home")

    return render(request, "emp_app/update.html", {"user": user})

# Delete employee
@login_required
def Deleteemp(request, id):
    if request.method == "POST":
        user = get_object_or_404(employee, id=id)
        user.delete()
        messages.success(request, "employee deleted successfully! ")
        return redirect('home')

    messages.error(request, "Something went wrong!")
    return redirect('home')