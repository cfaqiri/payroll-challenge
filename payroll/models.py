from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class Report(models.Model):
    employer = models.ForeignKey('auth.User', related_name='reports', on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)


class JobGroup(models.Model):
    employer = models.ForeignKey('auth.User', related_name='job_groups', on_delete=models.CASCADE)
    title = models.CharField(max_length=1)
    rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.title)


class Employee(models.Model):
    employer = models.ForeignKey('auth.User', related_name='employees', on_delete=models.CASCADE)
    # Job groups should not be deleted, unless no longer needed for any employees
    number = models.IntegerField()
    job_group = models.ForeignKey(JobGroup, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.number)


class PayPeriod(models.Model):
    employer = models.ForeignKey('auth.User', related_name='pay_periods', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.start_date} to {self.end_date}"


class EmployeeReport(models.Model):
    employer = models.ForeignKey('auth.User', related_name='employee_reports', on_delete=models.CASCADE)
    report = models.ManyToManyField(Report)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_period = models.ForeignKey(PayPeriod, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['employee_id']

    def __str__(self):
        return f"{self.employee} from {self.pay_period.start_date} to {self.pay_period.end_date}: {self.amount_paid}"


class TimekeepingRecord(models.Model):
    employer = models.ForeignKey('auth.User', related_name='timekeeping_records', on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    date = models.DateField()
    hours = models.DecimalField(max_digits=6, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Null is true because the employee report may be created after the timekeeping instance is saved
    employee_report = models.ForeignKey(EmployeeReport, on_delete=models.CASCADE, null=True)

    def __str__(self):
        date = str(self.date)
        return f"{self.employee} on {date}"