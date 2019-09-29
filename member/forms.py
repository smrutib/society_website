from django import forms 

from member.models import Request
from django.forms import ModelForm 
from datetime import date
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
import time 
from member.models import Complaint
from member.models import Cheque_details
from django.forms import ModelForm

from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import SelectDateWidget

class RequestForm(ModelForm):

	
	
	cctv_time_from=forms.DateTimeField(initial=timezone.now)
	cctv_time_to=forms.DateTimeField(initial=timezone.now)
	request=forms.CharField(widget=forms.Textarea)
	created=forms.BooleanField(initial=True,required=False)
	inprogress=forms.BooleanField(initial=False,required=False)
	completed=forms.BooleanField(initial=False,required=False)
	class Meta:
		model = Request
		fields = '__all__'
		
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

class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		fields = '__all__'



class ChequeDetailsForm(ModelForm):
	#cheque_date=forms.DateField(widget=SelectDateWidget)
	class Meta:
		model = Cheque_details
		fields = ['cheque_date','chequeno','amount','bank']
		exclude=['user']
		widgets={'cheque_date' : SelectDateWidget}

		#widget={'cheque_date' : DatePickerInput()}

