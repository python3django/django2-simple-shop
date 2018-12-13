from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Image
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .recommender import Recommender


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)
    paginator = Paginator(products_list, 3) # по 3 поста на каждой странице
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, отправляем первую страницу
        products = paginator.page(1)
    except EmptyPage:
        # Если страница вне диапазона отправляем последнюю страницу результатов
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                    'page': page})


"""
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request, 'shop/product/detail.html',
		{'product': product,
		 'cart_product_form': cart_product_form,
		 'recommended_products': recommended_products
		})
"""


def product_detail(request, id, slug, image_id=None):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    if image_id:
        image_title = product.images.get(id=image_id)
        images_small = product.images.exclude(id=image_id)
    else:
        try:
            image_title = product.images.all()[0]
            images_small = product.images.exclude(id=image_title.id)
        except Exception:
            image_title = None
            images_small = None
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request, 'shop/product/detail.html',
                {'product': product,
                 'cart_product_form': cart_product_form,
                 'image_title': image_title,
                 'images_small': images_small,
                 'recommended_products': recommended_products})
