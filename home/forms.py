from django.forms import ModelForm
from home.models import visitors
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class visitorsform(ModelForm):
	class Meta:
		model=visitors
		fields=('name','telephone','flat_no','purpose')


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = '__all__'