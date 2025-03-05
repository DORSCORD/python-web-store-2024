from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

def product_list(request: HttpRequest, category_slug: str=None) -> HttpResponse:
    """View для списку товарів"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(
            Category, 
            translations__language_code=language,
            translations__slug=category_slug
        )
        products = products.filter(category=category)
    if query := request.GET.get('search'):
        products = products.filter(translations__name__contains=query) | products.filter(translations__description__contains=query)
    return render(
        request,
        "shop/product/list.html",
        {"category": category,
        "categories": categories,
        "products": products}
    )

def product_detail(request: HttpRequest, id: int, slug: str) -> HttpResponse:
    """View для одного товару"""
    language = request.LANGUAGE_CODE
    product = Product.objects.filter(id=id, translations__slug=slug, available=True).first()
    product.set_current_language(language)
    cart_product_form = CartAddProductForm()
    return render(request, "shop/product/detail.html", {"product": product, "cart_product_form": cart_product_form})
