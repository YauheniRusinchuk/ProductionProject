from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth import get_user_model


User = get_user_model()


class Account(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    slug         = models.SlugField(unique=True)
    avatar       = models.ImageField(upload_to='avatar/', blank=True, null=True)


    def __str__(self):
        return f"Это аккаунт юзера {self.user.username}"


    def get_absolute_url(self):
        return reverse('home:account:account_page', kwargs={'slug' : self.slug})


def pre_save_account_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.user.username)
    instance.slug = slug

pre_save.connect(pre_save_account_receiver, sender=Account)
