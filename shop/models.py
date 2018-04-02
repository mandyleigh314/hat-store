from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class Order(models.Model):
    customername = models.CharField(max_length=200)
    customeremail = models.CharField(max_length=200, db_index=True)
    customerphone = models.CharField(max_length=200)
    customeraddress = models.CharField(max_length=200)
    customercity = models.CharField(max_length=200)
    customerstate = models.CharField(max_length=200)
    customerzip = models.CharField(max_length=200)
    billingaddress = models.CharField(max_length=200)
    billingcity = models.CharField(max_length=200)
    billingstate = models.CharField(max_length=200)
    billingzip = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
