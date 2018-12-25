from django.db import models

from user.models import User


class Shop(models.Model):
    name = models.CharField(max_length=120)
    location = models.TextField()
    employees = models.ManyToManyField(User, through='Employee')

class Employee(models.Model):
    OWNER = 1
    EMPLOYEE = 2
    EMPLOYEE_KINDS = (
        (OWNER, 1),
        (EMPLOYEE, 2),
    )
    employee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employee_shop')
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name='shop_employees')
    kind = models.IntegerField(choices=EMPLOYEE_KINDS, default=EMPLOYEE)
