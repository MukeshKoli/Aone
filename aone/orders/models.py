from django.db import models
from django.utils import timezone
from company.models import Company
from products.models import Products
import time
import datetime
import random


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

    orderId = models.CharField(max_length=256, unique=True, blank=True,
                               verbose_name="Order ID")
    orderDate = models.DateField(default=datetime.date.today(), verbose_name="Date")
    orderMonth = models.DateField(default=datetime.date.today(), verbose_name="Month")
<<<<<<< HEAD
    compName = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, verbose_name="Company Name")
    itemName = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, verbose_name="Items")
    itemQuantity = models.PositiveIntegerField(verbose_name="Quantity", default=1)
=======
    compName = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name="Company Name")
    itemName = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, verbose_name="Items")
    itemQuantity = models.PositiveIntegerField(max_length=256, verbose_name="Quantity", default=1)
>>>>>>> b485e7c327aed112c5b759b728aabce054f19b09
    orderStatus = models.CharField(max_length=50, choices=STATUS_CHOICES,
                                   default="In Progress", verbose_name="Status")

    def __str__(self):
        return str(self.compName)


    def save(self):

        self.orderId = random.randint(1000000000, 9999999999)
        super(Orders, self).save()



