# Generated by Django 2.2 on 2021-04-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_auto_20210406_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprescription',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
