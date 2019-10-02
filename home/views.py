from home.models import visitors,CustomUser
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from home import forms
from .forms import CustomUserCreationForm,quotationform

def home(request):
	return render(request,"home/homepage.html")
def visitors(request):
	if request.method == 'POST':
		form=forms.visitorsform(request.POST)
		if form.is_valid():
			s = form.cleaned_data['wing']
			t=form.cleaned_data['flat']
			st=s+t
			record=form.save(commit=False)
			record.flatno=st
			record=form.save()
			record.save()
			form=forms.visitorsform()
	else:
		form=forms.visitorsform()
	return render(request, "home/visitors.html",{'form':form})
	
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'home/signup.html'

def quotation_upload(request):
	if request.method == 'POST':
		form=forms.quotationform(request.POST,request.FILES)
		if form.is_valid():
			record=form.save()
			record.save()
			form=forms.quotationform()

	else:
		form=forms.quotationform()
	return render(request, "home/quotation.html",{'form':form})

