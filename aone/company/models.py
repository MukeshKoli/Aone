from django.db import models
from django.urls import reverse
# Create your models here.


class Company(models.Model):

    compID = models.AutoField(primary_key=True, editable=False, unique=True)
    compName = models.CharField(max_length=256, verbose_name="Company Name")
    CompAddress = models.TextField(verbose_name="Address")
    compContact = models.CharField(max_length=20, verbose_name="Contact")
    compEmail = models.EmailField(blank=True, verbose_name="Email Id")
    compLocation = models.CharField(max_length=150, blank=True, verbose_name="Location")

    def __str__(self):

        return self.compName


