from django.shortcuts import render
from home.models import CustomUser
from member.models import Request,Complaint
from django.http import HttpResponseRedirect  
from django.urls import reverse
from member.models import Complaint,Cheque_details,LandL
<<<<<<< HEAD
from django.http import HttpResponse
from django.views.generic import View

from society_website.utils import render_to_pdf

# Create your views here.

def index(request):
	
	return render(request,'commitee/c_index.html')

def complaint(request):

	intercom_complaints=Complaint.objects.filter(complaint_type='Intercom').order_by('complaint_date')
	leakage_complaints=Complaint.objects.filter(complaint_type='Leakage').order_by('complaint_date')
	cleaning_complaints=Complaint.objects.filter(complaint_type='Cleaning').order_by('complaint_date')
	other_complaints=Complaint.objects.filter(complaint_type='Other').order_by('complaint_date')

	context1={'intercom_complaints':intercom_complaints,'leakage_complaints':leakage_complaints,'cleaning_complaints':cleaning_complaints,'other_complaints':other_complaints}
	return render(request,'commitee/c_complaint.html',context1)

def request(request):

	sale_requests=Request.objects.filter(request_type='SalesAgreement',completed = False ).order_by('request_date')
	Addp_requests=Request.objects.filter(request_type='AddressProof',completed = False ).order_by('request_date')
	cctv_requests=Request.objects.filter(request_type='CCTV',completed = False ).order_by('request_date')
	noc_requests=Request.objects.filter(request_type='NOC',completed = False ).order_by('request_date')
	other_requests=Request.objects.filter(request_type='Other',completed = False ).order_by('request_date')
	context={'sale_requests':sale_requests,'Addp_requests':Addp_requests,'cctv_requests':cctv_requests,'noc_requests':noc_requests,'other_requests':other_requests}


	return render(request,'commitee/c_request.html',context)

def cheque_details(request):

	cheques=Cheque_details.objects.all().order_by('entry_date')

	return render(request,'commitee/c_cheque_details.html',{'cheques':cheques})

def landl(request):
	lls=LandL.objects.all().order_by('landl_date')

	return render(request,'commitee/c_landl.html',{'lls':lls})

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
	
def sales_request_progress(request,i):

	Request.objects.filter(id=i).update(inprogress=True)

	return HttpResponseRedirect(reverse('commitee:request'))
	#return render(request,'commitee/c_request.html')

def sales_request_complete(request,i):

	Request.objects.filter(id=i).update(completed=True)

	return HttpResponseRedirect(reverse('commitee:request'))

def Addp_request_progress(request,i):

	Request.objects.filter(id=i).update(inprogress=True)

	return HttpResponseRedirect(reverse('commitee:request'))
	#return render(request,'commitee/c_request.html')

def Addp_request_complete(request,i):

	Request.objects.filter(id=i).update(completed=True)

	return HttpResponseRedirect(reverse('commitee:request'))

def cctv_request_progress(request,i):

	Request.objects.filter(id=i).update(inprogress=True)

	return HttpResponseRedirect(reverse('commitee:request'))
	#return render(request,'commitee/c_request.html')

def cctv_request_complete(request,i):

	Request.objects.filter(id=i).update(completed=True)

	return HttpResponseRedirect(reverse('commitee:request'))

def noc_request_progress(request,i):

	Request.objects.filter(id=i).update(inprogress=True)

	return HttpResponseRedirect(reverse('commitee:request'))
	#return render(request,'commitee/c_request.html')

def noc_request_complete(request,i):

	Request.objects.filter(id=i).update(completed=True)

	return HttpResponseRedirect(reverse('commitee:request'))
def other_request_progress(request,i):

	Request.objects.filter(id=i).update(inprogress=True)

	return HttpResponseRedirect(reverse('commitee:request'))
	#return render(request,'commitee/c_request.html')

def other_request_complete(request,i):

	Request.objects.filter(id=i).update(completed=True)

	return HttpResponseRedirect(reverse('commitee:request'))



class GeneratePdf(View):
	def get(self, request, *args, **kwargs):
		cheques=Cheque_details.objects.all().order_by('entry_date')
		pdf = render_to_pdf('commitee/c_cheque_details.html',{'cheques':cheques})
		return HttpResponse(pdf, content_type='application/pdf')
