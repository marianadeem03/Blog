from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_field):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email is must"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have 'is_staff=True'"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have 'is_superuser=True'"))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    USER_TYPES = [
        ("USER", "User"),
        ("AUTHOR", "Author"),
    ]
    username = models.CharField(max_length=50, null=True, blank=True, unique=False)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=50)
    role_types = models.CharField(max_length=26, choices=USER_TYPES, default="User")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.email
