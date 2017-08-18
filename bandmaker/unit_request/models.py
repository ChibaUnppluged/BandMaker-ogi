from django.db import models
from accounts.models import MyUser
from instrument.models import instrument
# Create your models here.
class Request(models.Model):
    request_user = models.ForeignKey(MyUser)
    unit_name = models.CharField(max_length = 50,blank = False,default="")
    
    member_1 = models.CharField(max_length=50,default="",blank=True)
    inst_1 = models.ForeignKey(instrument,blank=True)
    member_2 = models.CharField(max_length=50,default="",blank=True)
    inst_2 = models.ForeignKey(instrument,blank=True)
    member_3 = models.CharField(max_length=50,default="",blank=True)
    inst_3 = models.ForeignKey(instrument,blank=True)
    member_4 = models.CharField(max_length=50,default="",blank=True)
    inst_4 = models.ForeignKey(instrument,blank=True)
    member_5 = models.CharField(max_length=50,default="",blank=True)
    inst_5 = models.ForeignKey(instrument,blank=True)

    recruit_inst1 = models.ForeignKey(instrument,blank=True)
    recruit_inst2 = models.ForeignKey(instrument,blank=True)
    recruit_inst3 = models.ForeignKey(instrument,blank=True)
    recruit_inst4 = models.ForeignKey(instrument,blank=True)
    recruit_inst5 = models.ForeignKey(instrument,blank=True)

    music = models.TextField(max_length = 300,blank=True)
    comment = models.TextField(max_length=300)

class Applicant(models.Model):
    request = models.ForeignKey(Request)
    applicant_user =models.ForeignKey(MyUser)
    comment = models.TextField(max_length=300)