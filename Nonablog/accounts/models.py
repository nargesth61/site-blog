from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from .manager import AccountManager

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    data_joined = models.DateTimeField(verbose_name='data joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_image = models.ImageField(default='img/blog/cat-widget1.jpg')
 
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    
    def __str__(self):
        return self.username
    
    # یک تابع برای پرمیشن یوزر که ادمین است یا نه
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True