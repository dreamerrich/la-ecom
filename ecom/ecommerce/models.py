from django.db import models

# Create your models here.
category_opt = (('women', 'Women'), ('men', 'Men'))

class product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=category_opt)
    prize = models.CharField(max_length=100)
    image = models.ImageField( max_length=100)

class cart(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amt = models.CharField(max_length=200)





