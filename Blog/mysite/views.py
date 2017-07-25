from django.shortcuts import render
from .models import Blog, Tag, Category
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
__category = {
    'geek': '技术博客',
    'life': '生活随笔',
    'xc': '瞎扯',

}
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

def __pagination(request, objs, display_num=5, after_range=5, before_range=4):
    paginator = Paginator(objs, display_num)

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    try:
        objects = paginator.page(page)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    except:
        objects = paginator.page(1)

    if page > after_range:
        page_range = paginator.page_range[page - after_range:page + before_range]
    else:
        page_range = paginator.page_range[0:page + before_range]

    return objects, page_range

def __get_blog_list(request, obj_list):
    obj_latest = __get_latest(obj_list)
    obj_infos_all = __get_blog_info(obj_list)
    obj_infos, obj_page_range = __pagination(request,obj_infos_all)
    return obj_latest, obj_infos, obj_page_range

def __get_latest(objs, max_num=3):
    obj_num = objs.count()
    latest = []

    if obj_num > max_num:
        for i in range(max_num):
            latest.append({'title':objs[i].title, 'id':objs[i].id})
    else:
        for i in range(obj_num):
            latest.append({'title': objs[i].title, 'id': objs[i].id})
    return latest

def index(request):
    blog_objs = Blog.objects.all()
    tags = Tag.objects.all()
    # blogs = __get_blog_info(blog_objs)
    latest, blogs, page_range = __get_blog_list(request, blog_objs)

    content = {'latest':latest,
               'blogs': blogs,
               'page_range': page_range,
               'tags': tags,
               }
    return render_to_response('index.html', content)

def geek(request):
    geek = Category.objects.get(category=__category['geek'])
    blog_objs = Blog.objects.filter(category=geek)
    latest, blogs, page_range = __get_blog_list(request, blog_objs)
    tags = Tag.objects.all()
    content = {'latest': latest,
               'blogs': blogs,
               'page_range': page_range,
               'tags': tags,
               }
    return render_to_response('index.html', content)

def tag(request):
    tag_id = request.GET.get('id')
    get_tag = Tag.objects.get(id=tag_id)
    blog_objs = Blog.objects.filter(tags=get_tag)
    latest, blogs, page_range = __get_blog_list(request, blog_objs)
    tags = Tag.objects.all()
    content = {'latest': latest,
               'blogs': blogs,
               'page_range': page_range,
               'tags': tags,
               }
    return render_to_response('index.html', content)

def detail(request):
    blog_id = request.GET.get('id')
    blog = Blog.objects.get(id=blog_id)
    blog.page_views += 1
    blog.save()
    #blog_content = repr(blog.content)
    return render_to_response('detail.html', {'blog': blog})


