# Generated by Django 3.0.5 on 2020-08-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20200813_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='logout',
            field=models.DateTimeField(null=True),
        ),
    ]