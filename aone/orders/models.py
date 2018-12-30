from django.db import models
from django.utils import timezone
from company.models import Company
from products.models import Products
import time
import datetime


# Create your models here.

today = datetime.date.today()


class Orders(models.Model):

    In_Progress = "In Progress"
    Billable = "Billable"
    Billed = "Billed"
    STATUS_CHOICES = (
        (In_Progress, 'In Progress'),
        (Billable, 'Billable'),
        (Billed, 'Billed')
    )

    orderId = models.CharField(max_length=256, unique=True, null=False, verbose_name="Order ID")
    orderDate = models.DateTimeField(default=timezone.now(), verbose_name="Date")
    orderMonth = models.DateField(default=datetime.date.today(), verbose_name="Month")
    compName = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Company Name")
    itemName = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Items")
    orderStatus = models.CharField(max_length=50, choices=STATUS_CHOICES,
                                   default="In Progress", verbose_name="Status")

    def __str__(self):
        return self.orderId

