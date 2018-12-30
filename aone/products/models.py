from django.db import models
from company.models import Company


# Create your models here.


class Products(models.Model):
    KG = "Kg"
    Pcs = "Pcs"
    Bags = "Bags"
    Box = "Box"

    PER_CHOICES = (
        (KG, 'Kg'),
        (Pcs, 'Pcs'),
        (Bags, 'Bags'),
        (Box, 'Box')
    )

    prodID = models.AutoField(primary_key=True, editable=False, unique=True)
    prodName = models.CharField(max_length=256, verbose_name="Product Name")
    compName = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Company Name")
    prodCode = models.CharField(max_length=150, verbose_name="Product Code")
    rate = models.FloatField(verbose_name="Rate")
    per = models.CharField(max_length=15, choices=PER_CHOICES, verbose_name="Per")
    prodPhoto = models.ImageField(upload_to='prodImage', blank=True)

    def __str__(self):

        return self.prodName


