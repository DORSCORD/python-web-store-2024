from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Користувач"))
    birthdate = models.DateField(blank=True, null=True, verbose_name=_("Дата народження"))
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, verbose_name=_("Фотографія"))

    class Meta:
        verbose_name = _("Профіль")
        verbose_name_plural = _("Профілі")

    def __str__(self):
        return f"{_('Profile of')} {self.user.username}"
    