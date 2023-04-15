from django.urls import path,include
from .views import *

app_name ='mainweb'

urlpatterns = [
    path('',index_viwe,name='index'),
    path('contact',contact_viwe,name='contact'),
    path('about',about_viwe,name='about'),
    path('elements',elements_viwe,name='elements'),
]