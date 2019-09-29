from django.db import models
from datetime import date
from django.utils import timezone
#from home.models import CustomUser

# Create your models here.
class Complaint(models.Model):

        complaint_date=models.DateField( auto_now_add=False)
        flatno=models.CharField(max_length=5)
        username=models.CharField(max_length=200)
        #username= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        complaint_choices = [
        ('Intercom', 'Intercom'),
        ('Leakage', 'Leakage'),
        ('Cleaning', 'Cleaning'),
        ('Other','Other')
        ]
        complaint_type=models.CharField(
        max_length=100,
        choices=complaint_choices,
        default='Other',
        )
        description=models.CharField(max_length=500)
        complain_img = models.ImageField(upload_to='complaint_images/', default="noimage.jpg") 



class Request(models.Model):


        request_date=models.DateField(auto_now_add=True)
        flatno=models.CharField(max_length=5)
        username=models.CharField(max_length=200)
        #username= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        request_choices = [
        ('NOC', 'NOC'),
        ('AddressProof', 'AddressProof'),
        ('SalesAgreement', 'SalesAgreement'),
        ('CCTV', 'CCTV'),
        ('Other','Other')
        ]
        request_type=models.CharField(max_length=100,choices=request_choices,default='NOC')

        name_to_be_addressed=models.CharField(max_length=100,blank=True)
        new_members_names=models.CharField(max_length=200,blank=True)
        sales_details=models.CharField(max_length=300,blank=True)
        cctv_time_from=models.DateTimeField(blank=True,default=timezone.now)
        cctv_time_to=models.DateTimeField(blank=True,default=timezone.now)
        request=models.CharField(max_length=500,blank=True)
        created=models.BooleanField(default=True)
        inprogress=models.BooleanField(default=False)
        completed=models.BooleanField(default=False)

