from django.db import models


class ProductItem(models.Model):
    name = models.CharField(max_length=150)  # Medium / Dev.to
    link = models.TextField()
    image_link = models.TextField()
    price = models.IntegerField()
    cashback = models.IntegerField()
    specifications = models.TextField(blank=True, null=True)
    product_html = models.TextField()


    def __str__(self):
        return self.name
