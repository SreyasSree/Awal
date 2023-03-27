from django.db import models

from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _

COLORS = (
    ('GOLD','GOLD'),
    ('BLACK', 'BLACK'),
    ('COPPER','COPPER'),
    ('GOLD STAINLESS STEEL','GOLD STAINLESS STEEL'),
    ('SILVER STAINLESS STEEL','SILVER STAINLESS STEEL'),
    ('COPPER PAINT','COPPER PAINT')
)

SIZE = (
    ('60cm*60cm','60cm*60cm'),
    ('90cm*90cm', '90cm*90cm'),
    ('100cm*100cm','100cm*100cm'),
    ('70cm*70cm','70cm*70cm'),
    ('80cm*80cm','80cm*80cm'),
)

QUANTITY = (
    ('1','1'),
    ('2', '2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20'),
)


# Create your models here.
class Category(models.Model):
    title = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.TextField()
    image1 = models.ImageField()
    image2 = models.ImageField(null=True,blank=True)
    image3 = models.ImageField(null=True,blank=True)
    price = models.IntegerField()
    cut_price = models.IntegerField()
    colors = models.CharField(max_length=50 , choices=COLORS)
    size = models.CharField(max_length=50 , choices=SIZE)
    category = models.ForeignKey('Category',on_delete= models.CASCADE, related_name='categories')
    quantity = models.CharField(max_length=50 , choices=QUANTITY)

    def __str__(self):
        return self.title



class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal = models.IntegerField()
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    save = models.BooleanField()
    

    def __str__(self):
        return self.customer_id


class OrderItem(models.Model):
    order = models.ForeignKey(Order ,on_delete= models.CASCADE)
    product = models.ForeignKey(Product ,on_delete= models.CASCADE)