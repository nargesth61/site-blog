from django.urls import path,include
from .views import *

app_name ='blog'

urlpatterns = [
    path('',blogs.as_view(),name='blog_home'),
    path('<int:pk>',blogs_single.as_view(),name='single'),
    path('addpost/',add_post,name='addpost'),
    path('category/<str:cat_name>',blogs.as_view(),name='category'),
    path('search/',blog_search,name='search'),
]