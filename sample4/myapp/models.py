from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    birthday = models.DateField()
    def __self__(self):
        return self.user_name

