# Generated by Django 3.2.21 on 2023-09-19 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dictionary',
            unique_together={('word', 'translation')},
        ),
    ]
