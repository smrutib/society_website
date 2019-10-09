from django import forms
from commitee.models import announcement
from django.forms import ModelForm

class AnnounceForm(ModelForm):

	class Meta:
		model = announcement
		fields = '__all__'
		
