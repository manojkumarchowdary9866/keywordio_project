from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('please provide email address')
        email=self.normalize_email(email)
        user=self.model(email=email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    
    def create_superuser(self,email,first_name,last_name,password):
        user=self.create_user(email,first_name,last_name,password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=UserProfileManager()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']


    def get_full_name(self):
        return self.first_name+' '+self.last_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.first_name+' '+self.last_name


class BOOK(models.Model):
    Book_name=models.CharField(max_length=100,primary_key=True)
    Author_name=models.CharField(max_length=100)
    Publish_date=models.DateField()

    def __str__(self):
        return self.Book_name
    








    