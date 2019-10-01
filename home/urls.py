from django.urls import path
from .views import SignUpView
from home import views




urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('visitorsform/',views.visitors, name="visitors"),
    path('quotation/',views.quotation_upload,name="quotation_upload")
]