from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from home.models import visitors,Quotation

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['name','username','password','telephone','flat_no','email']

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(visitors)

admin.site.register(Quotation)

