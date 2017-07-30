from django.contrib import admin

# Register your models here.
from mysite.models import Blog, Tag, Category, Friend
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Friend)
