from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Account(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    slug         = models.SlugField(unique=True)
    avatar       = models.ImageField(upload_to='avatar/', blank=True, null=True)


    def __str__(self):
        return f"Это аккаунт юзера {self.user.username}"
