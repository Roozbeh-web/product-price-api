from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
