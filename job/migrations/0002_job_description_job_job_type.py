# Generated by Django 5.1.7 on 2025-03-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('FULL TIME ', 'FULL TIME '), ('PART TIME ', 'PART TIME ')], default='', max_length=15),
        ),
    ]
