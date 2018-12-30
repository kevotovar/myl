from django.db import models

from user.models import User


class Shop(models.Model):
    name = models.CharField(max_length=120)
    location = models.TextField()
    employees = models.ManyToManyField(User, through='Employee')

    def __str__(self):
        return self.name

    def can_report_tournament(self):
        self.tournaments.filter()


class Employee(models.Model):
    OWNER = 1
    EMPLOYEE = 2
    EMPLOYEE_KINDS = (
        (OWNER, 'Owner'),
        (EMPLOYEE, 'Employee'),
    )
    employee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employee_shop')
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name='shop_employees')
    kind = models.IntegerField(choices=EMPLOYEE_KINDS, default=EMPLOYEE)

    def __str__(self):
        return '{} - {}'.format(self.shop.name, self.employee.full_name)
