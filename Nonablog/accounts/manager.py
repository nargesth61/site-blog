from django.contrib.auth.models import BaseUserManager

class AccountManager (BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email :
            raise ValueError('you need add email')
        if not username :
            raise ValueError('you need add username')       
        email = self.normalize_email(email)
        user = self.model(email = email,username = username)
        user.set_password(password)
        user.save(using =self._db)
        return user
    def create_superuser(self,email,username,password):
        email = self.normalize_email(email)
        user =self.create_user(email = email,username = username,password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using =self._db)
        return user