from django.urls import path
from .views import SignUpView
from home import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('visitorsform/',views.visitors, name="visitors"),
    path('quotation/',views.quotation_upload,name="quotation_upload"),
    #path('test/',views.test, name="test"),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
   	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
   ]

