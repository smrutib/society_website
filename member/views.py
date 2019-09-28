from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
	return render(request,'member/index.html')

def complaint(request):
	if request.method == 'POST':
		form = forms.ComplaintForm(request.POST,request.FILES)
		if form.is_valid():
			record =form.save()
			record.save()
			form = forms.ComplaintForm()
	else:
		form = forms.ComplaintForm()
	return render(request,'member/complaint.html',{'form':form})

def request(request):
	return render(request,'member/request.html')
# Create your views here.
