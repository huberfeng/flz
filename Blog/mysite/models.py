from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['-add_time']


class Category(models.Model):
    category = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['-add_time']


class Blog(models.Model):
    title = models.CharField('标题', max_length=100)
    head_pic_url = models.CharField('头图链接', max_length=250, default='/static/img/default.jpg')
    pub_time = models.DateTimeField(auto_now_add=True)
    brief = models.CharField('摘要', max_length=200, blank=True, null=True)
    content = RichTextUploadingField('正文', blank=True, null=True)
    page_views = models.PositiveIntegerField('阅读量', default=0, editable=False)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    category = models.ForeignKey(Category, verbose_name='分类')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']


class Profile_Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True,unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['-add_time']


class Profile(models.Model):
    title = models.CharField('标题', max_length=50)
    head_pic_url = models.CharField('头图链接', max_length=250,default='/static/img/default.jpg',null=True,blank=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField('正文', blank=True, null=True)
    tags = models.ManyToManyField(Profile_Tag, blank=True, verbose_name=u'标签')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']


class Friend(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    friend_url = models.CharField('链接', max_length=250, default='http://')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

