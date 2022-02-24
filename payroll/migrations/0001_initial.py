# Generated by Django 4.0.2 on 2022-02-24 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['employee_id'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimekeepingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hours', models.DecimalField(decimal_places=2, max_digits=6)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
                ('employee_report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='payroll.employeereport')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timekeeping_records', to=settings.AUTH_USER_MODEL)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.report')),
            ],
        ),
        migrations.CreateModel(
            name='PayPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_periods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employeereport',
            name='pay_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.payperiod'),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='report',
            field=models.ManyToManyField(to='payroll.Report'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payroll.jobgroup'),
        ),
    ]
