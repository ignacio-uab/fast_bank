# Generated by Django 2.0rc1 on 2018-01-26 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20180112_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bank.CompanyGroup'),
        ),
        migrations.AddField(
            model_name='movement',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
