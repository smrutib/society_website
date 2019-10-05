from django.contrib import admin
from django.urls import path, re_path
from member import views
app_name='member'
urlpatterns = [
	re_path(r'^$',views.index,name='index'),
	path('complaint',views.complaint,name='complaint'),
	path('request',views.request,name='request'),
	path('cheque_details',views.cheque_details,name='cheque_details'),
	path('landl',views.landl,name='landl'),
	path('complaint_delete/<int:i>/',views.complaint_delete,name='complaint_delete'),

]