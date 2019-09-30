from django.shortcuts import render
from django.http import HttpResponse
from member import forms
from . import forms
from member.tables import Cheque_details_table
from member.models import Cheque_details,Request,Complaint
from home.models import CustomUser 
from datetime import date

def index(request):
	
	return render(request,'member/index.html')

def complaint(request):
	if request.method == 'POST':
		form = forms.ComplaintForm(request.POST,request.FILES)
		if form.is_valid():
			s = form.cleaned_data['wing']
			t=form.cleaned_data['flat']
			st=s+t
			record =form.save()
			record.username=request.user.username
			record.flatno=st
			record.save()
			form = forms.ComplaintForm()
	else:
		form = forms.ComplaintForm()
	return render(request,'member/complaint.html',{'form':form})

def request(request):
	if request.method == 'POST':
		#s=request.POST.get('wing')+request.POST.get('flat')
		#print(s)
		form = forms.RequestForm(request.POST,request.FILES)
		if form.is_valid():
			s = form.cleaned_data['wing']
			t=form.cleaned_data['flat']
			st=s+t
			record =form.save(commit=False)
			record.username=request.user.username
			record.flatno=st
			#record.date_of_issue=date.today
			record.save()
			form = forms.RequestForm()
	else:
		form = forms.RequestForm()
	table = (Request.objects.filter(username =request.user.username ))

	context = {'form':form , 'table':table}	
	return render(request,'member/request.html',context)


def cheque_details(request):
	if request.method == 'POST':
		form = forms.ChequeDetailsForm(request.POST)
		if form.is_valid():
			s = form.cleaned_data['wing']
			t=form.cleaned_data['flat']
			st=s+t
			record =form.save(commit=False)
			#record.user = request.user
			
			record.user=request.user.username
			record.flatno=st
			record.save()
			form = forms.ChequeDetailsForm()
	else:
		form = forms.ChequeDetailsForm()
	
	table = Cheque_details_table(Cheque_details.objects.filter(user = request.user.username))

	context = {'form':form , 'table':table}	
	return render(request,'member/cheque_details.html',context)

def landl(request):
	if request.method == 'POST':
		form = forms.LandLForm(request.POST,request.FILES)
		if form.is_valid():
			s = form.cleaned_data['wing']
			t=form.cleaned_data['flat']
			st=s+t
			record =form.save()
			record.username=request.user.username
			record.flatno=st
			record.save()
			form = forms.LandLForm()
	else:
		form = forms.LandLForm()
	return render(request,'member/landl.html',{'form':form})