# Generated by Django 3.0.6 on 2020-05-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storm_inv', '0005_auto_20200513_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='lname',
            field=models.CharField(default='', max_length=100),
        ),
    ]