from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField(verbose_name="Дійсний з")
    valid_to = models.DateTimeField(verbose_name="Дійсний до")
    discount = models.IntegerField(
        validators = [MaxValueValidator(0), MaxValueValidator(100)],
        help_text = "Відсоток знижки (від 0 дл 100)",
        verbose_name="Знижка"
    )
    active = models.BooleanField(verbose_name="Активний")

    class Meta:
        verbose_name = "Купон"
        verbose_name_plural = "Купони"
    
    def __str__(self):
        return self.code