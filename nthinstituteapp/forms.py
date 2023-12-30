from django import forms
from django.contrib.auth.models import User
from .models import CommentData

class CommentForm(forms.ModelForm):
    content=forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Text Here...','cols':10,'rows':10}))
    class Meta:
        model=CommentData
        fields=('content',)







class RegistrationForm(forms.ModelForm):
    first_name=forms.CharField(label='Enter First Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(label='Enter Last Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    username=forms.CharField(label='Enter Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email=forms.EmailField(label='Enter Your Email Id',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password=forms.CharField(label='Enter Your Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')


class ContactForm(forms.Form):
    first_name=forms.CharField(
        label='Enter First Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }
        )
    )
    last_name=forms.CharField(
        label='Enter Last Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            }
        )
    )
    email=forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    location=forms.CharField(
        label='Enter Your Location',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Location'
            }
        )
    )
    courses=forms.CharField(
        label='Enter Course Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Course Name'
            }
        )
    )
    referred_by=forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Referred Person Name'
            }
        )
    )