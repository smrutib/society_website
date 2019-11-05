from django.db import models
from django.contrib.auth.models import AbstractUser

class visitors(models.Model):
	name=models.CharField(max_length=50)
	telephone=models.CharField(max_length=10,primary_key=True)
	flat_no=models.CharField(max_length=10)
	purpose=models.CharField(max_length=50)

class CustomUser(AbstractUser):

	# add additional fields in here
	name=models.CharField(max_length=256)
	username=models.CharField(max_length=100,primary_key=True)
	password=models.CharField(max_length=100)
	telephone=models.CharField(max_length=10)
	flat_no = models.CharField(max_length=20)
	email = models.EmailField(max_length=100)

	rights = models.CharField(max_length=10, default="normal")


class Quotation(models.Model):
	company_name=models.CharField(max_length=50)
	telephone=models.CharField(max_length=10)
	email=models.CharField(max_length=20)
	description=models.CharField(max_length=100)
	pdf=models.FileField(upload_to='quotations/pdfs/')


def __str__(self):
	return self.name

