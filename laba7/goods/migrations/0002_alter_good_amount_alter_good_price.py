# Generated by Django 4.2.5 on 2023-10-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.IntegerField(),
        ),
    ]