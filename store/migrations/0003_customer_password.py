# Generated by Django 3.1.7 on 2021-04-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='123456', max_length=50),
        ),
    ]