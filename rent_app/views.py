from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.contrib.staticfiles.urls import static



def index(request):
    return render(request,"index.html")


def registration(request):
    return render(request,"registration.html")


def register(request):
    print('-'*30+'> ' 'The registration form was submitted.')
    errors = User.objects.basic_validator(request.POST)

    # Validate form, check if email already exists in database.

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        print('-'*30+'> ', 'Errors: ', errors)
        return redirect('/registration')

    else:
        user = User.objects.get(email=request.POST['email'])
        # Save user info to form input
        if 'first_name' not in request.session:
            request.session['first_name'] = request.POST['first_name']  
        if 'last_name' not in request.session:
            request.session['last_name'] = request.POST['last_name']
        if 'email' not in request.session:
            request.session['email'] = request.POST['email']
        if 'welcome_msg' not in request.session:
            request.session['welcome_msg'] = 'You\'re now a registered user.'
        if 'userid' not in request.session:
            request.session['userid'] = user.id
        if 'isadmin' not in request.session:
            request.session['isadmin'] = user.is_admin 
        print('-'*30+'> ', 'A new user was created!')
        print('-'*30+'> ', 'Current users:\n', User.objects.all())
        return redirect('/success')


def login(request):
    # Save login email to form input
    if 'email' not in request.session:
        request.session['email'] = request.POST['email']

    # Validate user input, make sure form is complete and filled out.
    # Check to see if user exists and password is valid.
    print(request.POST)
    errors = User.objects.login_validator(request.POST)
    print("The length of errors is: " + str(len(errors)))
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        print('-'*30+'> ', 'Errors: ', errors)
        return redirect('/registration')

    else:
        user = User.objects.get(email=request.POST['email'])
        if 'first_name' not in request.session:
            request.session['first_name'] = user.first_name
        if 'last_name' not in request.session:
            request.session['last_name'] = user.last_name 
        if 'phone_num' not in request.session:
            request.session['phone_num'] = user.phone_num
        if 'email' not in request.session:
            request.session['email'] = user.email
        if 'welcome_msg' not in request.session:
            request.session['welcome_msg'] = 'You\'ve logged in successfully.'
        if 'userid' not in request.session:
            request.session['userid'] = user.id
        if 'isadmin' not in request.session:
            request.session['isadmin'] = user.is_admin    
        print('-'*30+'> ', 'The user id is', request.session['userid'])
        print('-'*30+'> ', 'The user status is', request.session['isadmin'])
        print('-'*30+'> ', 'Password is correct!')
        print('-'*30+'> ', 'User logged in successfully. ')
        return redirect('/success')


def success(request):
    if 'userid' in request.session:
        if request.session["isadmin"]==True:
            print('-'*30+'> ', 'Admin has  logged in.')
            return render(request, 'admin_page.html')

        else:
            context = {
                'users' : User.objects.all(),
                'cars' : Car.objects.all()
            }
            print('-'*30+'> ', 'User has been logged in.')
            return render(request, 'dashboard.html', context)
    else:
        print('-'*30+'> ', 'Someone tried to access /success without logging in.')
        return redirect('/registration')


def logout(request):
    request.session.flush()
    print('-'*30+'> ', 'User has been logged oout.')
    return redirect('/')


def add_car(request):
    if 'userid' in request.session:
        errors = Car.objects.car_validator(request.POST, request.FILES)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            print('-'*30+'> ', 'Errors: ', errors)
            return redirect('/success')
        else:
            return redirect('/success')


def car_list(request):
    if 'userid' in request.session:
        context = {
            "all_cars": Car.objects.all(),
            
        }
    return render(request, "car_list.html", context)


def car_details(request,car_id):
    thisCar=Car.objects.get(id=car_id)
    context = {
        "thisCar": thisCar,
    }
    return render(request, "car_details.html", context)

def book(request,car_id):
    thisCar=Car.objects.get(id=car_id)
    # thisUser=User.objects.get(id=request.session['userid'])
    # rental=Rental.objects.get(car_id=thisCar,user_id=thisUser)
    # rental.days=request.POST['days']
    # total_cost=rental.days*thisCar.price
    
    context = {
        "thisCar": thisCar,
    #     "total_cost":total_cost,
    }
    return render(request, "booking.html", context)


def about_us(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")
