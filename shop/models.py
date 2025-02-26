from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.

class Category(models.Model):
    """Категорія товарів"""

    name = models.CharField(max_length=200, verbose_name=_("Назва"))
    slug = models.SlugField(max_length=200, unique=True)

    class Mets:
        orddering = ["name"]
        indexes = [
            models.Index(fields = ["name"]),
        ]
        verbose_name = _("Категорія")
        verbose_name_plural = _("Категорії")

    def __str__(self) -> str:
        """Повертає назву об'єкта"""
        return self.name
    
    def get_absolute_url(self) -> str:
        return reverse("shop:product_list_by_category", kwargs={"category_slug": self.slug})
    
    

class Product(models.Model):
    """Товар"""

    category = models.ForeignKey(Category, related_name = "products", on_delete=models.CASCADE, verbose_name=_("Категорія"))
    name = models.CharField(max_length=200, verbose_name=_("Назва"))
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to="products/%Y/%m%d", blank=True, verbose_name=_("Зображення"))
    description = models.TextField(blank=True, verbose_name=_("Опис"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Ціна"))
    available = models.BooleanField(default=True, verbose_name=_("Наявність"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Створити"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Оновити"))

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]
        verbose_name = _("Товар")
        verbose_name_plural = _("Товари")

    def __str__(self) -> str:
        """Повертає назву об'єкта"""
        return self.name
    
    def get_absolute_url(self) -> str:
        return reverse("shop:product_detail", kwargs={"id": self.id, "slug": self.slug})
    