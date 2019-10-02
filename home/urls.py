from django.urls import path
from .views import SignUpView
<<<<<<< HEAD

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
=======
from home import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('visitorsform/',views.visitors, name="visitors"),
    path('quotation/',views.quotation_upload,name="quotation_upload")
>>>>>>> fd25907e5c836c06d2d769b9161b1aeadc725d8c
]