from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=223)
    
    def __str__(self) :
        return self.name

class Post(models.Model):
    image = models.ImageField(default='img/blog/cat-widget1.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = 
    category =models.ManyToManyField(Category) 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title