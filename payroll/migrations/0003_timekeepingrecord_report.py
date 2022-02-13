# Generated by Django 4.0.2 on 2022-02-11 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_remove_timekeepingrecord_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='timekeepingrecord',
            name='report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='payroll.report'),
            preserve_default=False,
        ),
    ]