# Generated by Django 2.2.1 on 2019-10-02 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheque_details',
            name='flatno',
            field=models.CharField(max_length=5),
        ),
    ]
