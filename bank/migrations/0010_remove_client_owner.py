# Generated by Django 2.0rc1 on 2018-01-30 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0009_auto_20180130_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='owner',
        ),
    ]