from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Користувач")
    birthdate = models.DateField(blank=True, null=True, verbose_name="Дата народження")
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, verbose_name="Фотографія")

    def __str__(self):
        return f"Profile of {self.user.username}"
    