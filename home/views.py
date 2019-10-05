from home.models import visitors,CustomUser
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from home import forms
from .forms import CustomUserCreationForm,quotationform
from django.views.generic import View
from django.shortcuts import redirect


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
    def form_valid(self,form):
    	s=form.cleaned_data['wing']
    	t=form.cleaned_data['flat']
    	st=s+t
    	form.instance.flat_no=st
    	form.instance.rights="normal"
    	return super().form_valid(form)
    		
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



def login_success(request):
    if request.objects.filter(rights="normal"):
    	return redirect("member/")
    elif request.objects.filter(rights="commitee"): 
    	return redirect("commitee/admin.html")
    else:
        return redirect("commitee/option.html")

