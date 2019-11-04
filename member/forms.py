from django import forms 
from member.models import Request
from django.forms import ModelForm 
from datetime import date
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
import time 
from member.models import Complaint
from member.models import Cheque_details,LandL
from django.forms import ModelForm

from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import SelectDateWidget

class RequestForm(ModelForm):

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

	
	cctv_time_from=forms.DateTimeField(initial=timezone.now)
	cctv_time_to=forms.DateTimeField(initial=timezone.now)
	request=forms.CharField(widget=forms.Textarea)
	created=forms.BooleanField(initial=True,required=False)
	inprogress=forms.BooleanField(initial=False,required=False)
	completed=forms.BooleanField(initial=False,required=False)
	class Meta:
		model = Request
		fields = '__all__'
		exclude=['username','date_of_issue','flatno','created','inprogress','completed']
		
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
	    	 self.fields_required(['new_members_names','sales_details','bank_format'])
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

	class Meta:
		model = Complaint
		fields = '__all__'
		exclude=['username','flatno']



class ChequeDetailsForm(ModelForm):
	#cheque_date=forms.DateField(widget=SelectDateWidget)
	remarks=forms.CharField(widget=forms.Textarea)
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
	class Meta:
		model = Cheque_details
		fields = ['cheque_date','chequeno','amount','bank','remarks']
		exclude=['user','flatno']
		widgets={'cheque_date' : SelectDateWidget}

		#widget={'cheque_date' : DatePickerInput()}


class LandLForm(ModelForm):
	#cheque_date=forms.DateField(widget=SelectDateWidget)
	
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
	class Meta:
		model = LandL
		fields = ['from_date','to_date','agreement','police_ver']
		exclude=['username','flatno']
		widgets={'from_date' : SelectDateWidget,'to_date' : SelectDateWidget}

