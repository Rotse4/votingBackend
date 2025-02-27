from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, regNo, username, password=None):
        if not regNo:
            raise ValueError("Users must have a registration number")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            regNo=regNo,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, regNo, username, password):
        user = self.create_user(
            regNo=regNo,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    regNo = models.CharField(verbose_name='registration number', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'regNo'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()


    def __str__(self):
        return self.regNo + ' ' + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_lebel):
        return True
