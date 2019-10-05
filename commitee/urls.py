from django.contrib import admin
from django.urls import path, re_path
from commitee import views
from .views import GeneratePdf
app_name='commitee'
urlpatterns = [
	re_path(r'^$',views.index,name='index'),
	path('complaint',views.complaint,name='complaint'),
	path('request',views.request,name='request'),
	path('cheque_details',views.cheque_details,name='cheque_details'),
	path('landl',views.landl,name='landl'),
	path('option',views.option,name='option'),
	path('admin',views.admin,name='admin'),
	path('makeadmin/<str:pk>/',views.makeadmin,name="makeadmin"),
	path('makenormal/<str:pk>/',views.makenormal,name="makenormal"),
	path('psales/<int:i>/',views.sales_request_progress,name='sales_request_progress'),
	path('csales/<int:i>/',views.sales_request_complete,name='sales_request_complete'),
	path('pAddp/<int:i>/',views.Addp_request_progress,name='Addp_request_progress'),
	path('cAddp/<int:i>/',views.Addp_request_complete,name='Addp_request_complete'),
	path('pcctv/<int:i>/',views.cctv_request_progress,name='cctv_request_progress'),
	path('ccctv/<int:i>/',views.cctv_request_complete,name='cctv_request_complete'),
	path('pother/<int:i>/',views.other_request_progress,name='other_request_progress'),
	path('cother/<int:i>/',views.other_request_complete,name='other_request_complete'),
	path('pnoc/<int:i>/',views.noc_request_progress,name='noc_request_progress'),
	path('cnoc/<int:i>/',views.noc_request_complete,name='noc_request_complete'),
	path('pdfdownload', GeneratePdf.as_view(),name='htmltopdf'),


]