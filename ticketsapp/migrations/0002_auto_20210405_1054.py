# Generated by Django 3.1.7 on 2021-04-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='perfomanceTime',
            field=models.TimeField(auto_now=True),
        ),
    ]
