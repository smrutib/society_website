from django import forms 
from member.models import Complaint
from django.forms import ModelForm

class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		fields = '__all__'
