# Generated by Django 2.2 on 2021-04-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210305_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='../media/doctor.jpg', upload_to='doc_certi_pic'),
        ),
    ]
