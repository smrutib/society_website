from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import RegexValidator,MinValueValidator

#from home.models import CustomUser

# Create your models here.
class Complaint(models.Model):

        complaint_date=models.DateField( auto_now_add=True)
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
        complain_img = models.ImageField(upload_to='complaint_images/',null=True,blank=True) 



class Request(models.Model):

        
        request_date=models.DateField(auto_now_add=True)
        flatno=models.CharField(max_length=5)
        username=models.CharField(max_length=200)
        #username= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        request_choices = [
        ('NOC', 'NOC'),
        ('AddressProof', 'AddressProof(Passport)'),
        ('SalesAgreement', 'SalesAgreement(NOC)'),
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
        bank_format = models.FileField(upload_to='request_bank_format/',blank=True)


class Cheque_details(models.Model):
        entry_date=models.DateField(auto_now_add=True)
        flatno=models.CharField(max_length=5)
        user = models.CharField(max_length=50)
        cheque_date=models.DateField( auto_now_add=False)
        chequeno = models.CharField(max_length=6 , validators=[RegexValidator(r'^\d{1,10}$')])
        amount=models.IntegerField(validators=[MinValueValidator(0, message="Amount should be more than 0")])
        bank=models.CharField(max_length=200)
        remarks=models.CharField(max_length=500,default="none")
        

class LandL(models.Model):

        landl_date=models.DateField( auto_now_add=True)
        flatno=models.CharField(max_length=5)
        username=models.CharField(max_length=200)
        from_date=models.DateField( auto_now_add=False)
        to_date=models.DateField( auto_now_add=False)
        #username= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        agreement= models.FileField(upload_to='landl_docs_agreement/')
        police_ver = models.FileField(upload_to='landl_docs_police/')
