from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError(_("Email should provaide "))
        email = self.normalize_email(email)
        new_user = self.model(email=email, **extrafields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self, email, password, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_active', True)
        if extrafields.get('is_stuff') is not True:
            raise ValueError("Not stuff")
        if extrafields.get('is_superuser') is not True:
            raise ValueError("Not superuser")
        if extrafields.get('is_active') is not True:
            raise ValueError("Not active")
        return self.create_user(email, password, **extrafields)


class User(AbstractUser):
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True, db_index=True)
    password = models.CharField(max_length=100)
    img = models.ImageField(null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    def __str__(self):
        return self.email+str(self.id)
