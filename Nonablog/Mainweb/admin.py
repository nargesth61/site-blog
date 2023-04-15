from django.contrib import admin
from .models import *
class AdminContact(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display=('name','email','created_date')
    list_filter = ('email',)
    search_fields = ['name','email']

admin.site.register(Contact,AdminContact)

