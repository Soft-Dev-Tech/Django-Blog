from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    email = models.EmailField(unique=True)

    is_author = models.BooleanField(default=False)
    special_user = models.DateTimeField(default=timezone.now)

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = "Special user status"

    def is_Author(self):
        pass
    is_Author.short_description = "Author status"