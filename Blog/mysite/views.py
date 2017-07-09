from django.shortcuts import render
from .models import Blog, Tag
from django.shortcuts import render_to_response
# Create your views here.
def __get_blog_info(objs):
    blog = []
    for blog_obj in objs:
        blog.append(
            {
                'title': blog_obj.title,
                'id': blog_obj.id,
                'head_pic_url': blog_obj.head_pic_url,
                'brief': blog_obj.brief,
                'pub_time': blog_obj.pub_time,
                'page_views': blog_obj.page_views,
            }
        )
    return blog


def index(request):
    blog_objs = Blog.objects.all()
    tags = Tag.objects.all()
    blogs = __get_blog_info(blog_objs)
    for blog in blogs:
        print("blog_brief", blog['brief'])
    content = {'blogs': blogs}
    return render_to_response('index.html', content)


def detail(request):
    blog_id = request.GET.get('id')
    blog = Blog.objects.get(id=blog_id)
    blog.page_views += 1
    blog.save()
    #blog_content = repr(blog.content)
    return render_to_response('detail.html', {'blog': blog})