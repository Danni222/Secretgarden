from django import forms
from .models import Order
from datetime import date
from django.forms.extras.widgets import SelectDateWidget
#import LengthValidator and ComplexityValidator from passwords.validators
from passwords.validators import (LengthValidator, ComplexityValidator)

#import Customer model from your application models
from store.models import Customer

#create the form class
class CustomerForm(forms.ModelForm):
    #use predefined validators attributes from password.validators module
    #add form label
    #add help_text information
    #specify widget as passwordInput
    password=forms.CharField(validators=[LengthValidator(min_length=8),
	ComplexityValidator(complexities=dict(UPPER=1,LOWER=1,DIGITS=1)),],
	widget=forms.PasswordInput,max_length=40,label='Password',
        help_text='Please use at least one uppercase and a number and must be 8 characters or more')
    
    class Meta:
       #Define the model class created under models for this form
        model= Customer
        #Below you define which model fiels you want to display 
        fields=['fname','lname','email','phoneNumber','password']

        
class SignInForm(forms.Form):
    email=forms.CharField(label='Email Address',widget=forms.TextInput(attrs={'size': '30'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'size':'30'}),label='Password')

quantityChoices = [(i, str(i)) for i in range(1, 31)]
class CartAddProductForm(forms.Form):
         quantity = forms.TypedChoiceField(choices=quantityChoices,coerce=int)
         update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput) 

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['address','postalCode','city','deliverydate']
      #  deliverydate=forms.DateInput(format='%Y/%m/%d')
       # citys=(('McAllen','McAllen'),('Hidalgo','Hidalgo'))
        city=forms.ModelChoiceField(queryset=Order.objects.all(),label='City')
     

class OrderCreateBouquetForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['address','postalCode','city','makebouquet','deliverydate']
       # deliverydate=forms.DateField(widget=SelectDateWidget())
