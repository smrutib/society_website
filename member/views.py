from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from member import forms
from . import forms
from member.tables import Cheque_details_table
from member.models import Cheque_details,Request,Complaint,LandL
from home.models import CustomUser 
from datetime import date
from django.urls import reverse
from datetime import datetime


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
			print(form.errors)
	else:
		form = forms.ComplaintForm()

	complaints = (Complaint.objects.filter(username =request.user.username )).order_by('complaint_date')

	context1={'form':form,'complaints':complaints}

	return render(request,'member/complaint.html',context1)

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
			print(form.errors)
	else:

		form = forms.RequestForm()

	table = (Request.objects.filter(username =request.user.username )).order_by('request_date')

	context = {'form':form , 'table':table}	
	return render(request,'member/request.html',context)


def cheque_details(request):
	if request.method == 'POST':
		form = forms.ChequeDetailsForm(request.POST)
		if form.is_valid():
			print("valid")
			s = form.cleaned_data['wing']
			t=form.cleaned_data['flat']
			st=s+t
			c=form.cleaned_data['chequeno']
			a=form.cleaned_data['amount']
			b=form.cleaned_data['bank']
			rem=form.cleaned_data['remarks']
			d=form.cleaned_data['cheque_date']
			record =form.save(commit=False)			
			record.user=request.user.username
			record.flatno=st
			record.chequeno=c
			record.amount=a
			record.bank=b
			record.remarks=rem
			record.cheque_date=d
			record.save()     
			form = forms.ChequeDetailsForm()
		else:
			print(form.errors)
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
			print(form.errors)
	else:
		form = forms.LandLForm()
	lls = LandL.objects.filter(username = request.user.username).order_by('landl_date')
	context2 = {'form':form , 'lls':lls }	
	return render(request,'member/landl.html',context2)


def complaint_delete(request,i):

	Complaint.objects.filter(id=i).delete()

	return HttpResponseRedirect(reverse('member:complaint'))

