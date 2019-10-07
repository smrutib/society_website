from django.shortcuts import render
from home.models import CustomUser
from member.models import Request,Complaint
from django.http import HttpResponseRedirect  
from django.urls import reverse
from member.models import Complaint,Cheque_details,LandL
from django.db.models import Q
from django.contrib import messages
def index(request):
	
	return render(request,'commitee/c_index.html')

def complaint(request):

	intercom_complaints=Complaint.objects.filter(complaint_type='Intercom').order_by('complaint_date')
	leakage_complaints=Complaint.objects.filter(complaint_type='Leakage').order_by('complaint_date')
	cleaning_complaints=Complaint.objects.filter(complaint_type='Cleaning').order_by('complaint_date')
	other_complaints=Complaint.objects.filter(complaint_type='Other').order_by('complaint_date')


	if request.method=='POST':
		srch=request.POST['srh']
		if srch:
			match=Complaint.objects.filter(Q(flatno__icontains=srch))

			if match:
				return render(request,'commitee/c_complaint.html',{'sr':match,'intercom_complaints':intercom_complaints,'leakage_complaints':leakage_complaints,'cleaning_complaints':cleaning_complaints,'other_complaints':other_complaints})
			else:
				messages.error(request,'no result found')

				return render(request,'commitee/c_complaint.html',{'sr':match,'intercom_complaints':intercom_complaints,'leakage_complaints':leakage_complaints,'cleaning_complaints':cleaning_complaints,'other_complaints':other_complaints})
		else:
			return HttpResponseRedirect(reverse('commitee:complaint'),{'sr':match,'intercom_complaints':intercom_complaints,'leakage_complaints':leakage_complaints,'cleaning_complaints':cleaning_complaints,'other_complaints':other_complaints})	

	return render(request,'commitee/c_complaint.html',{'intercom_complaints':intercom_complaints,'leakage_complaints':leakage_complaints,'cleaning_complaints':cleaning_complaints,'other_complaints':other_complaints})

def request(request):

	sale_requests=Request.objects.filter(request_type='SalesAgreement',completed = False ).order_by('request_date')
	Addp_requests=Request.objects.filter(request_type='AddressProof',completed = False ).order_by('request_date')
	cctv_requests=Request.objects.filter(request_type='CCTV',completed = False ).order_by('request_date')
	noc_requests=Request.objects.filter(request_type='NOC',completed = False ).order_by('request_date')
	other_requests=Request.objects.filter(request_type='Other',completed = False ).order_by('request_date')
	
	if request.method=='POST':
		srch=request.POST['srh']
		if srch:
			match=Request.objects.filter(Q(flatno__icontains=srch))
			if match:
				return render(request,'commitee/c_request.html',{'sr':match,'sale_requests':sale_requests,'Addp_requests':Addp_requests,'cctv_requests':cctv_requests,'noc_requests':noc_requests,'other_requests':other_requests})
			else:
				messages.error(request,'no result found')
				return render(request,'commitee/c_request.html',{'sr':match,'sale_requests':sale_requests,'Addp_requests':Addp_requests,'cctv_requests':cctv_requests,'noc_requests':noc_requests,'other_requests':other_requests})

		else:
			return HttpResponseRedirect(reverse('commitee:request',{'sr':match,'sale_requests':sale_requests,'Addp_requests':Addp_requests,'cctv_requests':cctv_requests,'noc_requests':noc_requests,'other_requests':other_requests}))
	return render(request,'commitee/c_request.html',{'sale_requests':sale_requests,'Addp_requests':Addp_requests,'cctv_requests':cctv_requests,'noc_requests':noc_requests,'other_requests':other_requests})


def cheque_details(request):

	cheques=Cheque_details.objects.all().order_by('entry_date')
	if request.method=='POST':
		srch=request.POST['srh']
		if srch:
			match= Cheque_details.objects.filter(Q(flatno__icontains=srch))
			if match:
				return render(request,'commitee/c_cheque_details.html',{'sr':match,'cheques':cheques})
			else:
				messages.error(request,'no result found')
				return render(request,'commitee/c_cheque_details.html',{'sr':match,'cheques':cheques})

		else:
			return HttpResponseRedirect(reverse('commitee:cheque_details',{'sr':match,'cheques':cheques}))
	return render(request,'commitee/c_cheque_details.html',{'cheques':cheques})

def landl(request):
	lls=LandL.objects.all().order_by('landl_date')
	if request.method=='POST':
		srch=request.POST['srh']
		if srch:
			match= Cheque_details.objects.filter(Q(flatno__icontains=srch))
			if match:
				return render(request,'commitee/c_landl.html',{'sr':match,'lls':lls})
			else:
				messages.error(request,'no result found')
				return render(request,'commitee/c_landl.html',{'sr':match,'lls':lls})

		else:
			return HttpResponseRedirect(reverse('commitee:landl',{'sr':match,'lls':lls}))


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

def complaintsearch(request):
	
	return render(request,'commitee/c_complaint.html')