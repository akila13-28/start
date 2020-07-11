from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField().primary_key=True
    catalog=models.TextField(null=True)
    catagory = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    question = models.TextField(null=True)
    description = models.TextField(null=True)