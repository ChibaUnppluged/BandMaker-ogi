# coding:utf-8
from django.db import models

# Create your models here.
class MyPage(models.Model):
    nickname = models.CharField(max_length=20)
    birth_date = models.DateField()
