from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic/customer',null=True,blank=True,default='profile_pic/customer/lazy.png')
    address=models.CharField(max_length=40,blank=True,null=True)
    mobile=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.user.username
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name