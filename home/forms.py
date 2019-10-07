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
	wing_choices = [
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),

	]
	wing=forms.CharField(max_length=1, widget=forms.Select(choices=wing_choices),)

	flat_choices=[
	('101','101'),
	('102','102'),
	('103','103'),
	('104','104'),
	('201','201'),
	('202','202'),
	('203','203'),
	('204','204'),
	('301','301'),
	('302','302'),
	('303','303'),
	('304','304'),
	('401','401'),
	('402','402'),
	('403','403'),
	('404','404'),
	('501','501'),
	('502','502'),
	('503','503'),
	('504','504'),
	('601','601'),
	('602','602'),
	('603','603'),
	('604','604'),
	('701','701'),
	('702','702'),
	('703','703'),
	('704','704'),
	('801','801'),
	('802','802'),
	('803','803'),
	('804','804'),
	('901','901'),
	('902','902'),
	('903','903'),
	('904','904'),

	]
	flat=forms.CharField(max_length=3,
	widget=forms.Select(choices=flat_choices),)
	rights=forms.CharField(max_length=10 ,widget = forms.HiddenInput(),required=False)
		
	#rights = forms.CharField(widget=forms.HiddenInput(),initial="normal")
	class Meta(UserCreationForm):
		model = CustomUser
		fields=('name','username','telephone','flat_no','email')
		exclude=['flat_no']


class CustomUserChangeForm(UserChangeForm):

	wing_choices = [
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),

	]
	wing=forms.CharField(max_length=1, widget=forms.Select(choices=wing_choices),)

	flat_choices=[
	('101','101'),
	('102','102'),
	('103','103'),
	('104','104'),
	('201','201'),
	('202','202'),
	('203','203'),
	('204','204'),
	('301','301'),
	('302','302'),
	('303','303'),
	('304','304'),
	('401','401'),
	('402','402'),
	('403','403'),
	('404','404'),
	('501','501'),
	('502','502'),
	('503','503'),
	('504','504'),
	('601','601'),
	('602','602'),
	('603','603'),
	('604','604'),
	('701','701'),
	('702','702'),
	('703','703'),
	('704','704'),
	('801','801'),
	('802','802'),
	('803','803'),
	('804','804'),
	('901','901'),
	('902','902'),
	('903','903'),
	('904','904'),

	]
	flat=forms.CharField(max_length=3,
	widget=forms.Select(choices=flat_choices),
	)
	rights=forms.CharField(max_length=10 ,widget = forms.HiddenInput(),required=False)
	class Meta(UserChangeForm):
		model = CustomUser
		fields = ('name','username','telephone','flat_no','email')
		exclude=['flat_no','rights']



class quotationform(ModelForm):
	class Meta:
		model=Quotation
		fields='__all__'

