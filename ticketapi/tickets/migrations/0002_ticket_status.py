# Generated by Django 2.2.1 on 2019-05-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CLOSED', 'Closed')], default='pending', max_length=155),
        ),
    ]
