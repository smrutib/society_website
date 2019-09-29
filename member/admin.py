from django.contrib import admin
from member.models import Request
from member.models import Complaint
from member.models import Cheque_details
# Register your models here.
admin.site.register(Request)
admin.site.register(Complaint)
admin.site.register(Cheque_details)
