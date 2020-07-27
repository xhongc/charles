from django.db import models


# Create your models here.
class Nana(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, help_text='网址标题')
    description = models.CharField(max_length=255, default='这里还没什么描述', help_text='描述')
    url = models.CharField(max_length=255, null=False, blank=False)
    img_path = models.CharField(max_length=255, default='/', help_text='导航图片')
    read_no = models.IntegerField(default=0, help_text='浏览数')
    ordering = models.IntegerField(default=99, help_text='置顶')
    cate = models.ForeignKey('Category', on_delete=models.CASCADE, db_constraint=False, related_name='cates')


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, help_text='类目标题')
    html_id = models.CharField(max_length=64, null=False, blank=False, unique=True, help_text='类目ID')

    def __str__(self):
        return self.title
