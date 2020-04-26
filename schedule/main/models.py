from django.db import models

# Create your models here.

class Schedule(models.Model):
    S_id = models.AutoField(primary_key=True)
    year = models.CharField("年",max_length=4, blank=False)
    month = models.CharField("月",max_length=2, blank=False)
    day = models.CharField("日",max_length=2, blank=False)
    time = models.CharField("時",max_length=5, default='00:00')
    task = models.CharField("予定",max_length=30, blank=False)
    details = models.TextField("詳細",blank=True)
    importance = models.BooleanField("重要")
