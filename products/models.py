from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Sub_category(models.Model):
    tittle = models.CharField(max_length=255)

    def __str__(self):
        return self.tittle


class Category(models.Model):
    tittle = models.CharField(max_length=255)
    sub_category = models.ManyToManyField(Sub_category)

    def __str__(self):
        return self.tittle


class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=3000)
    sub_category = models.ManyToManyField(Sub_category)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    req = models.TextField()
    sub_category1 = models.CharField(max_length=250, default='')
    sub_category2 = models.CharField(max_length=250, default='')
    sub_category3 = models.CharField(max_length=250, default='')
    url_1 = models.CharField(max_length=250, default='')
    url_2 = models.CharField(max_length=250, default='')
    url_3 = models.CharField(max_length=250, default='')
    url_1_name = models.CharField(max_length=250, default='')
    url_2_name = models.CharField(max_length=250, default='')
    url_3_name = models.CharField(max_length=250, default='')


    def __str__(self):
        return self.name


