from django.forms import ModelForm
from home.models import visitors,Quotation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser 
from django import forms 

class visitorsform(ModelForm):
	class Meta:
		model=visitors
		fields=('name','telephone','flat_no','purpose')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields=('name','username','telephone','flat_no','email')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('name','username','telephone','flat_no','email')

class quotationform(ModelForm):
	class Meta:
		model=Quotation
		fields='__all__'

