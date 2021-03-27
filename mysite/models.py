from django.db import models
from django.utils import timezone

class Post(models.Model):
    # 建立資料表
    title = models.CharField(max_length=200)
    vid = models.CharField(max_length=20,default="WC_MRckl0rk") #記得加預設值
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
