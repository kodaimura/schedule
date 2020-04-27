from django.db import models

# Create your models here.

CATEGORY_CHOICE = (
    ('0','-'),
    ('1','仕事'),
    ('2','タスク'),
    ('3','締切り'),
    ('4','本番'),
    ('5','遊び'),
    ('6','その他'),
)
class Schedule(models.Model):
    user_id = models.IntegerField(blank=False)
    S_id = models.AutoField(primary_key=True)
    year = models.CharField("年",max_length=4, blank=False)
    month = models.CharField("月",max_length=2, blank=False)
    day = models.CharField("日",max_length=2, blank=False)
    time = models.CharField("時",max_length=5, default='00:00')
    task = models.CharField("予定",max_length=30, blank=False)
    details = models.TextField("詳細",blank=True)
    importance = models.BooleanField("重要")
    category = models.CharField("分類",choices=CATEGORY_CHOICE,default='0',max_length=5)
