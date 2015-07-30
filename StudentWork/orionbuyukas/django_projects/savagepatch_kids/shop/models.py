from django.db import models

# Create your models here.
class User(models.Model):
    shipping_info=models.ForeignKey(Shipping)


class Blog(models.Model):
    blog = models.TextField
    pub_date = models.DateTimeField(auto_now_add=True)

class Shipping(models.Model):
    user = models.ForeignKey(User)
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)

class Product(models.Model):
    item_name = models.CharField(max_length=255)
    add_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    img_link = models.CharField(max_length=255) #optional
