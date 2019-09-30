from django.contrib import admin
from member.models import Request
from member.models import Complaint
from member.models import Cheque_details,LandL
# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('request_date',)


class ComplaintAdmin(admin.ModelAdmin):
    readonly_fields = ('complaint_date',)

class ChequeAdmin(admin.ModelAdmin):
    readonly_fields = ('entry_date',)

admin.site.register(Request,RequestAdmin)
admin.site.register(Complaint,ComplaintAdmin)
admin.site.register(Cheque_details,ChequeAdmin)
admin.site.register(LandL)