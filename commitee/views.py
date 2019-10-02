from django.shortcuts import render

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
	