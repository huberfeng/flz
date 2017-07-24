from django.db import models


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
    content = models.TextField('正文', blank=True, null=True)
    page_views = models.PositiveIntegerField('阅读量', default=0, editable=False)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    category = models.ForeignKey(Category, verbose_name='分类')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']



