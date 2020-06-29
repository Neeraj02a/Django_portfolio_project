from django.db import models

# Create your models here.
class Job(models.Model):
    # models.Model here help up to create class and provide all shorts of required files to support it and help the object created to save in DB
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)