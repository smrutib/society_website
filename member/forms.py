from django import forms 
from member.models import Request
from django.forms import ModelForm 
from datetime import date
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
import time 

"""class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateTimeInput):
	input_type='time'"""
   
class RequestForm(ModelForm):

	'''name_to_be_addressed=forms.CharField(required=False)
	new_members_names=forms.CharField(required=False)
	sales_details=forms.CharField(required=False)
	cctv_date=forms.DateField(required=False)
	#cctv_time_from=forms.DateTimeField(required=False)
	#cctv_time_to=forms.DateTimeField(required=False)'''
	
	cctv_time_from=forms.DateTimeField(initial=timezone.now)
	cctv_time_to=forms.DateTimeField(initial=timezone.now)
	request=forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Request
		fields = '__all__'
		"""widgets = {
            'cctv_date': DateInput(),
            'cctv_time_from':DateTimeInput(),
            'cctv_time_to':DateTimeInput()
                   
        }"""
	def fields_required(self, fields):
		"""Used for conditionally marking fields as required."""
		for field in fields:
			if not self.cleaned_data.get(field, ''):
				msg = forms.ValidationError("Below field is required.")
				self.add_error(field, msg)


	def clean(self):
	    choice = self.cleaned_data.get('request_type')

	    '''if choice='NOC':
	        self.fields_required(['name_to_be_addressed'])
	    else:
	        self.cleaned_data['name_to_be_addressed'] = '''

	    if choice=='AddressProof':
	    	 self.fields_required(['name_to_be_addressed'])
	    else:
	        self.cleaned_data['name_to_be_addressed'] = ''

	    if choice=='SalesAgreement':
	    	 self.fields_required(['new_members_names','sales_details'])
	    else:
	        self.cleaned_data['new_members_names','sales_details'] = ''

	    if choice=='CCTV':
	    	 self.fields_required(['cctv_time_from','cctv_time_to'])
	    else:
	        self.cleaned_data['cctv_time_from','cctv_time_to'] = timezone.now,timezone.now

	    if choice=='Other':
	    	 self.fields_required(['request'])
	   

	    return self.cleaned_data