from django.db import models


class ProductItem(models.Model):
    """Model of all scraping items"""

    name = models.CharField(max_length=150)
    type = models.TextField(blank=True)
    link = models.TextField()
    image_link = models.TextField()
    price = models.IntegerField()
    cashback = models.IntegerField()
    specifications = models.TextField(blank=True, null=True)
    product_html = models.TextField()

    def __str__(self):
        return self.name
