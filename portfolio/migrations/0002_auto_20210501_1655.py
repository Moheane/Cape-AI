# Generated by Django 3.2 on 2021-05-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_details',
            name='location',
            field=models.CharField(default='Johannesburg', max_length=30),
        ),
        migrations.AlterField(
            model_name='personal_details',
            name='Linkedin',
            field=models.CharField(max_length=30),
        ),
    ]
