from django import template
from Blog.models import Post , Category
register = template.Library()



@register.inclusion_tag('blogs/latest_post.html')   
def last_post():
    posts=Post.objects.filter(status=1).order_by('published_date')[:4]
    return {'posts':posts}

@register.inclusion_tag('blogs/category.html')
def categore_tag():
    posts = Post.objects.filter(status=1)
    cat = Category.objects.all()
    dic = {}
    for name in cat:
        dic[name]=posts.filter(category=name).count()
    return {'categoris':dic}    