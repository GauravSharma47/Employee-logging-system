# Generated by Django 3.0.5 on 2020-08-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_attendance_nummins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='numMins',
            field=models.TimeField(null=True),
        ),
    ]