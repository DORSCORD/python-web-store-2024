from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name=_("Код"))
    valid_from = models.DateTimeField(verbose_name=_("Дійсний з"))
    valid_to = models.DateTimeField(verbose_name=_("Дійсний до"))
    discount = models.IntegerField(
        validators = [MaxValueValidator(0), MaxValueValidator(100)],
        help_text = _("Відсоток знижки (від 0 дл 100)"),
        verbose_name=_("Знижка")
    )
    active = models.BooleanField(verbose_name=_("Активний"))

    class Meta:
        verbose_name = _("Купон")
        verbose_name_plural = _("Купони")
    
    def __str__(self):
        return self.code