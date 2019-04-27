# _*_ coding:utf-8 _*_
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

class AdminUser(models.Model):
    """博主信息"""
    name = models.CharField(verbose_name='姓名', max_length=10)
    address = models.CharField(verbose_name='地址', max_length=100)
    phone = models.CharField(verbose_name='电话', max_length=20)
    email = models.EmailField(verbose_name='邮箱')

    class Meta:
        verbose_name = '博主信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Categories(models.Model):
    """博文分类"""

    name = models.CharField(verbose_name='名称', max_length=20)

    class Meta:
        verbose_name = '博文分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tags(models.Model):
    """标签管理"""
    tag = models.CharField(verbose_name='名称', max_length=20)
    add_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Articles(models.Model):
    """博文管理"""
    title = models.CharField(verbose_name='标题', max_length=20)
    img = models.ImageField(verbose_name='封面图', upload_to='articles', blank=True, null=True)
    author = models.ForeignKey(AdminUser, on_delete=models.CASCADE, null=True, verbose_name='作者')
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False, verbose_name='所属类别')
    tags = models.ManyToManyField(Tags)
    add_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    click_nums = models.IntegerField(verbose_name='阅读数', default=0)
    comment_nums = models.IntegerField(verbose_name='评论数', default=0)
    fav_nums = models.IntegerField(verbose_name='点赞数', default=0)
    info = models.CharField(verbose_name='摘要', max_length=200, default='')
    is_index = models.BooleanField(verbose_name='是否首页轮播', default=0)
    content = UEditorField(verbose_name='博文内容',
                           width=700,
                           height=400,
                           toolbars='full',
                           imagePath='articles',
                           filePath='articles',
                           upload_settings={'imageMaxSizing': 1024000},
                           default='')

    class Meta:
        verbose_name = '博文'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class CommenttUser(models.Model):
    """评论用户"""
    nickname = models.CharField(verbose_name='用户昵称', max_length=10)
    usericon = models.ImageField(verbose_name='用户头像', upload_to='users')
    area = models.CharField(verbose_name='地址', max_length=100)
    gender = models.BooleanField(verbose_name='性别', default=1)
    article = models.CharField(verbose_name='评论的文章', max_length=20)
    comment = models.TextField(verbose_name='评论内容',null=True)

    class Meta:
        verbose_name = '评论用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Jottings(models.Model):
    """心情随笔"""
    title = models.CharField(verbose_name='标题', max_length=20)
    img = models.ImageField(verbose_name='封面图', upload_to='articles', blank=True, null=True)
    author = models.ForeignKey(AdminUser, on_delete=models.CASCADE, null=True, verbose_name='作者')
    tags = models.ManyToManyField(Tags)
    add_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    click_nums = models.IntegerField(verbose_name='阅读数', default=0)
    comment_nums = models.IntegerField(verbose_name='评论数', default=0)
    fav_nums = models.IntegerField(verbose_name='点赞数', default=0)
    info = models.CharField(verbose_name='摘要', max_length=200,
                            default='随笔，顾名思义。就是在想记叙某件事的时候，稍稍写上几笔，叫做随笔，而心情随笔就是，表诉心情的喜，怒，哀，乐时记叙的文字。')
    content = UEditorField(verbose_name='博文内容',
                           width=700,
                           height=400,
                           toolbars='full',
                           imagePath='articles',
                           filePath='articles',
                           upload_settings={'imageMaxSizing': 1024000},
                           default='')

    class Meta:
        verbose_name = '心情随笔'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ItsMe(models.Model):
    """It's Me"""
    tag = models.CharField(verbose_name='标签', max_length=2)
    title = models.CharField(verbose_name='标题', max_length=10)
    se_title = models.CharField(verbose_name='副标题', max_length=10)
    info = models.CharField(verbose_name='副标题', max_length=40)

    class Meta:
        verbose_name = "It's Me"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GetMessage(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    email = models.EmailField(verbose_name='邮箱')
    subject = models.CharField(verbose_name='主题', max_length=100)
    message = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = "留言处理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
