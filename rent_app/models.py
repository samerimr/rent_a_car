from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PHONE_REGEX = re.compile(r'^[0-9]+$')

# Define new manager
class ErrorManager(models.Manager):
    
    def basic_validator(self, requestPOST):
        errors={}
        user_list= User.objects.filter(email=requestPOST['email'])
        if len(requestPOST['first_name']) <2:
            errors['first_name']= "First name should be at least 2 characters long."
        if len(requestPOST['last_name']) <2:
            errors['last_name']= "Last name should be at least 2 characters long."
        if len(requestPOST['email']) <1:
            errors['email'] = "Email required for registration."
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors['email_format'] = "Please enter a valid email."
        if not NAME_REGEX.match(requestPOST['first_name']):
            errors['first_name_format'] = "Please enter a valid first name."
        if not NAME_REGEX.match(requestPOST['last_name']):
            errors['last_name_format'] = "Please enter a valid last name."
        if not PHONE_REGEX.match(requestPOST['phone_num']):
            errors['phone_num_format'] = "Please enter a valid phone."  
        if len(requestPOST['password']) < 8:
            errors['password_len'] = "Password must be at least 8 characters long."
        if requestPOST['password'] != requestPOST['confirm_pw']:
            errors['password_match'] = "Please confirm password before registering, they do not match."
        if len(user_list)>0:
            errors['existing_user'] = "That email is already associated with an account."
        if not len(errors):
            hash= bcrypt.hashpw(requestPOST['password'].encode(), bcrypt.gensalt()).decode()
            print(hash)
            user = User.objects.create(first_name=requestPOST['first_name'], last_name=requestPOST['last_name'], email=requestPOST['email'], phone_num=requestPOST['phone_num'], password=hash)
            user.save()
        return errors

    def login_validator(self, requestPOST):
        errors = {}
        user_list = User.objects.filter(email=requestPOST['email'])
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors['format'] = "Please enter a valid email."
        if len(requestPOST['email']) < 1:
            errors['login_email'] = "Login email cannot be blank."
        if len(user_list) < 1:
            errors['email_error'] = "This email is not associated with an account."
        if len(user_list) > 0:
            user = User.objects.get(email=requestPOST['email'])
            if not bcrypt.checkpw(requestPOST['password'].encode(), user.password.encode()):
                errors['pw_error'] = "You could not be logged in."
            else:
                print('-'*30+'> ', 'Password is correct!')
                print('-'*30+'> ', 'User logged in successfully. ')
        return errors


    def car_validator(self, requestPOST, requestFILES):
        errors = {}
        if len(requestPOST['model']) < 1 or len(requestPOST['brand']) < 1 or len(requestPOST['color']) < 1 or len(requestPOST['fuel_type']) < 1 or len(requestPOST['production_date']) < 1 or len(requestPOST['gear_type']) < 1 or len(requestPOST['price']) < 1:
            errors['fields'] = "fill all fields."
        
        if not len(errors):
            new_car = Car.objects.create(model=requestPOST['model'], brand=requestPOST['brand'], color=requestPOST['color'], fuel_type=requestPOST['fuel_type'], production_date=requestPOST['production_date'], gear_type=requestPOST['gear_type'], photo=requestFILES['photo'], price=requestPOST['price'])
            new_car.save()
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=245)
    last_name = models.CharField(max_length=245)
    email = models.CharField(max_length=45)
    phone_num = models.IntegerField()
    password =models.CharField(max_length=245)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ErrorManager()

class Car(models.Model):
    brand= models.CharField(max_length=100)
    color= models.CharField(max_length=100)
    users_rent = models.ManyToManyField(User, through="Rental")
    production_date= models.DateTimeField(auto_now_add=True)
    model= models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=100)
    gear_type=models.CharField(max_length=100)
    price= models.IntegerField()
    photo= models.ImageField(upload_to='images/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ErrorManager()

class Rental(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    total_price = models.IntegerField()
    days = models.IntegerField()
    is_rented = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ErrorManager()


