from django.db import models
from django import forms
from django.db.models.functions import datetime
from .constants import *
   
class PlaceModel(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    tel=models.CharField(max_length=30)
    numbers=models.IntegerField(choices=PLACE_NUMBER_CHOICES)

    def __str__(self):
        return self.name

class MemberModel(models.Model):
    membername=models.CharField(max_length=20)
    gender=models.IntegerField(choices=[(0, '男性'), (1, '女性'), (2, 'その他')])
    tel=models.CharField(max_length=30)

    def __str__(self):
        return self.membername


class ScheduleModel(models.Model):
    place=models.ForeignKey(PlaceModel,on_delete=models.PROTECT)
    member=models.ForeignKey(MemberModel,on_delete=models.PROTECT)
    # kinds=models.CharField(max_length=20, choices=[(v, v) for v in ['ハイエース 定員七人', 'セレナ 定員五人', 'タント 定員三人', 'アルト白 定員三人', 'アルト黄 定員三人']], blank=True)
    kinds=models.CharField(max_length=20, choices=CAR_CHOICES, blank=True)
    datetime=models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"))


    def __str__(self):
        return self.place.name