from django.shortcuts import render
from django.http import HttpResponse
from member import forms
from . import forms
from member.tables import Cheque_details_table
from member.models import Cheque_details

def index(request):
	return render(request,'member/index.html')

def complaint(request):
	if request.method == 'POST':
		form = forms.ComplaintForm(request.POST)
		if form.is_valid():
			record =form.save()
			record.save()
			form = forms.ComplaintForm()
	else:
		form = forms.ComplaintForm()
	return render(request,'member/complaint.html',{'form':form})

def request(request):
	if request.method == 'POST':
		form = forms.RequestForm(request.POST)
		if form.is_valid():
			record =form.save()
			record.save()
			form = forms.RequestForm()
	else:
		form = forms.RequestForm()
	return render(request,'member/request.html',{'form':form})


def cheque_details(request):
	user = User.objects.get(username=username)
	print(user)
	if request.method == 'POST':
		form = forms.ChequeDetailsForm(request.POST)
		if form.is_valid():
			record =form.save(commit=False)
			record.user = user
			record.save()
			form = forms.ChequeDetailsForm()
	else:
		form = forms.ChequeDetailsForm()
	table = Cheque_details_table(Cheque_details.objects.filter(user = user))

	context = {'form':form , 'table':table}	
	return render(request,'member/cheque_details.html',context)

