# Generated by Django 4.0.4 on 2022-04-30 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=256)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(blank=True, default='')),
            ],
            options={
                'db_table': 'patients',
            },
        ),
        migrations.CreateModel(
            name='PharmaciesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'pharmacies',
            },
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='TransactionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=256)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateField(blank=True, default='')),
                ('patient_uuid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logia.patientsmodel')),
                ('pharmacy_uuid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logia.pharmaciesmodel')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
