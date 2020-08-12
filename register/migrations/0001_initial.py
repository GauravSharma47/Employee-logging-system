# Generated by Django 3.0.5 on 2020-08-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('fname', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=14)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now=True)),
                ('uId', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('pwd', models.CharField(max_length=100)),
                ('empId', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
