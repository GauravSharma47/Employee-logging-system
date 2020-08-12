# Generated by Django 3.0.5 on 2020-08-11 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logindate', models.DateField(auto_now=True)),
                ('logintime', models.TimeField(auto_now=True)),
                ('logoutdate', models.DateField()),
                ('logouttime', models.TimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Employee')),
            ],
        ),
    ]