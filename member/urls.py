from django.contrib import admin
from django.urls import path, re_path
from member import views
app_name='member'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    path('complaint',views.complaint,name='complaint'),
    path('request',views.request,name='request'),
    ]