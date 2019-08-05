from django.db import models


class Name(models.Model):
    name=models.CharField(max_length=50,verbose_name="姓名")
    sex=models.CharField(max_length=10,verbose_name="性别")
    age=models.IntegerField(verbose_name="年龄")
