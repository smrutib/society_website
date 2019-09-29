from django.shortcuts import render
from django.http import HttpResponse
from member import forms
def index(request):
	return render(request,'member/index.html')

def complaint(request):
	return render(request,'member/complaint.html')

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

