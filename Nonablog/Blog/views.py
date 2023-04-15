from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.views.generic import ListView , DetailView
from django.http import HttpResponse
from .forms import *
from django.core.paginator import Paginator ,PageNotAnInteger,EmptyPage

class blogs(ListView):
    model=Post
    template_name='blogs/blog-home.html'
    paginate_by = 2

    
    def get_queryset(self):
        return Post.objects.filter(status=1)


class blogs_single(DetailView):
    model=Post
    template_name='blogs/blog-single.html'
    
def add_post(request):
    if request.method == 'POST':
        form = AddNewPost(request.POST)
        if form.is_valid():
            form.save(commit=False)
            obj = form.instance
            return redirect('/')
        return HttpResponse(f"{form.errors}")    
    
    form = AddNewPost('blog/letest_post.html')
    context={'form':form}
    return render(request,'blogs/add_post.html',context)

def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'object_list':posts}
    return render(request,'blogs/blog-home.html',context)