# Generated by Django 2.2 on 2021-04-05 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_patientprescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprescription',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.TakeAppointment'),
        ),
    ]
