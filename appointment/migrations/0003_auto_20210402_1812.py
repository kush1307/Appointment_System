# Generated by Django 2.2 on 2021-04-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20210402_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='image',
            field=models.ImageField(default='../media/doctor.jpg', upload_to='doc_pro_pic'),
        ),
    ]
