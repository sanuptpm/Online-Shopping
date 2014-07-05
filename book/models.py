from django.db import models
from django.contrib.auth.models import User

from PIL import Image


# Create your models here.

 
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)

class Catagory(models.Model):
	cname=models.CharField(max_length=200)
	purdate=models.DateTimeField('purchase-date')
	createdby=models.ForeignKey(User)

class Product(models.Model):
	pname=models.CharField(max_length=200)
	discription=models.CharField(max_length=500)
	price=models.IntegerField()
	noitem=models.IntegerField()
	createdby=models.ForeignKey(User)
	cid=models.ForeignKey(Catagory)
	photo=models.ImageField(upload_to='photo') #image in pjct/media/photo
	
class Cart(models.Model):
	uid=models.ForeignKey(User)
	pid=models.ForeignKey(Product)
	noitem=models.IntegerField()
	purdate=models.DateTimeField("purchase-date")
	deldate=models.DateTimeField("delivary-date")
	status=models.CharField(max_length=10)
