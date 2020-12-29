from django.db import models


# Create your models here.



class PlaceInfo(models.Model):
    score_people_num = models.IntegerField(default=None, verbose_name="评价人数")
    score = models.FloatField(default=0.0, verbose_name="评价分数")
    place_name = models.CharField(default=None, verbose_name="地点名称",max_length=100)
    category = models.CharField(max_length=100, verbose_name="类别（shopping\visit\food）", default="None")
    introduction = models.CharField(max_length=200, verbose_name="介绍）", default="None")
    sub_category = models.CharField(max_length=100, verbose_name="子分类", default="None")
    image = models.ImageField(upload_to='img/place', verbose_name="图片", default="avatar.png")

    class Meta:
        verbose_name = "PlaceInfo"
        verbose_name_plural = "PlaceInfo"

    def __str__(self):
        return self.place_name
