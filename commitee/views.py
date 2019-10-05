from django.shortcuts import render
from home.models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
	
	return render(request,'commitee/c_index.html')

def complaint(request):

	return render(request,'commitee/c_complaint.html')

def request(request):

	return render(request,'commitee/c_request.html')

def cheque_details(request):

	return render(request,'commitee/c_cheque_details.html')

def landl(request):

	return render(request,'commitee/c_landl.html')

def option(request):

	return render(request,'commitee/option.html')

def admin(request):
	mem=CustomUser.objects.all()
	return render(request,'commitee/admin.html',{'mem':mem})

def makeadmin(request, pk):
    r = CustomUser.objects.get(pk=pk)
    r.rights="commitee"
    r.save()
    return HttpResponseRedirect(reverse('commitee:admin'))

def makenormal(request, pk):
    r = CustomUser.objects.get(pk=pk)
    r.rights="normal"
    r.save()
    return HttpResponseRedirect(reverse('commitee:admin'))
	