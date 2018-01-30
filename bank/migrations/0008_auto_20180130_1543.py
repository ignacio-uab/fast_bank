# Generated by Django 2.0rc1 on 2018-01-30 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20180130_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movement',
            name='id',
        ),
        migrations.AlterField(
            model_name='movement',
            name='bank',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bank.BankAccount'),
        ),
    ]