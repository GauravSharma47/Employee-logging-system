# Generated by Django 3.0.5 on 2020-08-12 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('fname', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now=True)),
                ('uId', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=40)),
                ('pwd', models.CharField(max_length=20)),
                ('empId', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logindate', models.DateField(auto_now=True)),
                ('logintime', models.TimeField(auto_now=True)),
                ('logoutdate', models.DateField(null=True)),
                ('logouttime', models.TimeField(null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Employee')),
            ],
        ),
    ]
