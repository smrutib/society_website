
from home.models import visitors,CustomUser
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
# Create your views here.
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
			record.save()
			form=forms.visitorsform()
	else:
		form=forms.visitorsform()
	return render(request, "home/visitors.html",{'form':form})
	
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'home/signup.html'