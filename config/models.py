from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = ((STATUS_NORMAL,'正常'),(STATUS_DELETE,'删除'),)

    title = models.CharField(max_length=50,verbose_name="标题")
    href = models.URLField(verbose_name="链接")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,
                                         verbose_name="状态")
    weigh = models.PositiveIntegerField(default=1, choices=zip(range(1,6),range(1,6)),
                                         verbose_name="权重",help_text="权重高展示序列靠前")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete = models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural='友链'

class SideBar(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = ((STATUS_NORMAL,'正常'),(STATUS_DELETE,'删除'),)

    name = models.CharField(max_length=10,verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,
                                         verbose_name="状态")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete = models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural='标签'




