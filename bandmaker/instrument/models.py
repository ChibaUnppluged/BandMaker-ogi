from django.db import models

# Create your models here.
class instrument(models.Model):
    inst_name = models.CharField(max_length=30,blank=False)