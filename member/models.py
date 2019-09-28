from django.db import models
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

        request_date=models.DateField( auto_now_add=False)
        flatno=models.CharField(max_length=5)
        username=models.CharField(max_length=200)
        #username= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        request_choices = [
        ('NOC', 'NOC'),
        ('AddressProof', 'AddressProof'),
        ('SalesAgreement', 'SalesAgreement'),
        ('CCTV', 'CCTv'),
        ('Other','Other')
        ]
        request_type=models.CharField(
        max_length=100,
        choices=request_choices,
        default='NOC',
        )
        name_to_be_addressed=models.CharField(max_length=100)
        new_members_names=models.CharField(max_length=200)
        sales_details=models.CharField(max_length=300)
        cctv_from=models.DateTimeField()
        cctv_to=models.DateTimeField()
