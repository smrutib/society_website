from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'member/index.html')

def complaint(request):
	return render(request,'member/complaint.html')

def request(request):
	return render(request,'member/request.html')
# Create your views here.
