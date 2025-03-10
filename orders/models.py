from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from coupons.models import Coupon
from shop.models import Product

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_("Ім'я"))
    last_name = models.CharField(max_length=50, verbose_name=_("Прізвище"))
    email = models.EmailField(verbose_name=_("E-mail"))
    address = models.CharField(max_length=250, verbose_name=_("Адреса"))
    postal_code = models.CharField(max_length=7, null=True, blank=True, verbose_name=_("Індекс"))
    city = models.CharField(max_length=50, verbose_name=_("Місто"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Створено"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Оновлено"))
    paid = models.BooleanField(default=False, verbose_name=_("Оплачено"))
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Купон"))
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
    
    def __str__(self):
        return f"Замовлення №{self.id}"
    
    def get_total_cost(self):
        total_cost = self.get_total_cost_before_discount()
        return total_cost - self.get_discount()
    
    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_discount(self):
        total_cost = self.get_total_cost_before_discount()
        if self.discount:
            return total_cost * (self.discount / Decimal(100))
        return Decimal(0)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name=_("Замовлення"))
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.RESTRICT, verbose_name=_("Товар"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Ціна"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Кількість"))

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    