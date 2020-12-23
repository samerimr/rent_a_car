from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        names = re.compile(r'^[a-zA-Z]{2,45}$') #checkk thiiiiiiiiiis
        # add keys and values to errors dictionary for each invalid field
        if not names.match(postData['first_name']):
            errors["first_name"] = "First name should be at least 2 characters and only letters"
        if not names.match(postData['last_name']):
            errors["last_name"] = "Last name should be at least 2 characters and only letters"
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"   
        if len(postData['password']) < 9 :
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_pw'] : #checkkkk
            errors["confirm_pw"] = "Password confirmation does not match"
        return errors    

    def exist(self,postData):
        errors = {}
        user=User.objects.filter(email=postData['login_email'])
        if not user:
            errors['login_email'] ="Please enter a valid email address."
        return errors
    def insert(self,postData):
        pw_hash=bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt()).decode()
        user=User.objects.create(first_name=postData['first_name'],last_name=postData['last_name'],phone_num=postData['phone_num'],email=postData['email'],password=pw_hash)
        return user

class User(models.Model):
        first_name = models.CharField(max_length=245)
        last_name = models.CharField(max_length=245)
        email = models.CharField(max_length=45)
        phon_num = models.IntegerField(max_length=245)
        password =models.CharField(max_length=245)
        is_admin = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        objects = UserManager()

class Car(models.Model):
        brand= models.CharField(max_length=100)
        color= models.CharField(max_length=100)
        uploaded_by= models.ForeignKey(User, related_name="car_uploaded", on_delete=models.CASCADE) #the user who uploaded a given car
        users_rent = models.ManyToManyField(User , related_name="rent_car")
        production_date= models.DateTimeField(auto_now_add=True)
        Model= models.CharField(max_length=100)
        fule_type=models.CharField(max_length=100)
        Gear_type=models.CharField(max_length=100)
        price= models.IntegerField(max_length=245)
        photo= models.ImageField(Upload_to='image/',blank=True,null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        objects = UserManager()
        
