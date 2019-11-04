from django.urls import path,re_path
from .views import SignUpView
from home import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
re_path(r'^$',views.base,name='base'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('visitorsform/',views.visitors, name="visitors"),
    path('quotation/',views.quotation_upload,name="quotation_upload"),
    #path('test/',views.test, name="test"),

    #path('password_reset/',auth_views.password_reset, name='password_reset'),
    #path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    #re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        #auth_views.password_reset_confirm, name='password_reset_confirm'),
    #path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),

   ]

