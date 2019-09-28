from django.contrib import admin
from member.models import Request
from member.models import Complaint
# Register your models here.
admin.site.register(Request)
admin.site.register(Complaint)