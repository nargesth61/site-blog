from django.contrib import admin
from .models import *



class AdminPost(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display=('title','counted_views','status','published_date')
    list_filter = ('status','author')
    search_fields = ['title','content','foreignkeyfield__auther']
    list_editable = ['status']
    list_display_links = ['title','counted_views']
    
    

admin.site.register(Post,AdminPost)
admin.site.register(Category)


