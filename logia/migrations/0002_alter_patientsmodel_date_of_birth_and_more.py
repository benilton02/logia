# Generated by Django 4.0.4 on 2022-04-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsmodel',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='transactionsmodel',
            name='timestamp',
            field=models.DateField(blank=True),
        ),
    ]
