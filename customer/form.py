from django import forms
from .models import Customer
from django.contrib.auth.models import User

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']



class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['address','mobile','profile_pic']
