# Generated by Django 3.0.6 on 2020-05-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storm_inv', '0009_person_movement'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='movement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
