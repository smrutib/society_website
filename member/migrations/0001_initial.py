

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('flatno', models.CharField(max_length=5)),
                ('user', models.CharField(max_length=50)),
                ('cheque_date', models.DateField()),
                ('chequeno', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Amount should be more than 0')])),
                ('bank', models.CharField(max_length=200)),
                ('remarks', models.CharField(default='none', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('flatno', models.CharField(max_length=5)),
                ('username', models.CharField(max_length=200)),
                ('complaint_type', models.CharField(choices=[('Intercom', 'Intercom'), ('Leakage', 'Leakage'), ('Cleaning', 'Cleaning'), ('Other', 'Other')], default='Other', max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('complain_img', models.ImageField(blank=True, null=True, upload_to='complaint_images/')),
            ],
        ),
        migrations.CreateModel(
            name='LandL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landl_date', models.DateField(auto_now_add=True)),
                ('flatno', models.CharField(max_length=5)),
                ('username', models.CharField(max_length=200)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('agreement', models.FileField(upload_to='landl_docs_agreement/')),
                ('police_ver', models.FileField(upload_to='landl_docs_police/')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('flatno', models.CharField(max_length=5)),
                ('username', models.CharField(max_length=200)),
                ('request_type', models.CharField(choices=[('NOC', 'NOC'), ('AddressProof', 'AddressProof(Passport)'), ('SalesAgreement', 'SalesAgreement(NOC)'), ('CCTV', 'CCTV'), ('Other', 'Other')], default='NOC', max_length=100)),
                ('name_to_be_addressed', models.CharField(blank=True, max_length=100)),
                ('new_members_names', models.CharField(blank=True, max_length=200)),
                ('sales_details', models.CharField(blank=True, max_length=300)),
                ('cctv_time_from', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('cctv_time_to', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('request', models.CharField(blank=True, max_length=500)),
                ('created', models.BooleanField(default=True)),
                ('inprogress', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('bank_format', models.FileField(blank=True, upload_to='request_bank_format/')),
            ],
        ),
    ]
