from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import View
from shop.models import Product


def search(request):
    q = request.GET.get('q')

    print(q)
    if q:
        products = Product.objects.filter(name__icontains=q)

        products_images = ProductImage.objects.filter(product_id__in=[pr.id for pr in products], is_active=True,
                                                      is_main=True,
                                                      product__is_active=True, )
        paginator = Paginator(products_images, 12)

        page_number = request.GET.get('page')

        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?q=' + q + '&page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?q=' + q + '&page={}'.format(page.next_page_number())
        else:
            next_url = ''

        context = {
            'products_images': products_images,
            'q': q,
            'page_object': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url
        }
    else:
        context = {}



    return render(
        request, 'search/search.html'
        , context
    )


def index(request):
    return render(
        request,
        'index.html',
        # context={'num_books': num_books, 'num_instances': num_instances,
        #          'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


def products(request, slug_text_cat=None):
    # products_list = Product.objects.all()

    # context_dict = {'products': products_list}

    if slug_text_cat is None:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    else:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True,
                                                      product__category__slug=slug_text_cat)

    # products_images_product = products_images.filter(product__category_id=2)
    paginator = Paginator(products_images, 12)

    page_number = request.GET.get('page')

    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    # products_images_products = paginator.get_page(page)

    context = {
        # 'products_images_product': products_images_product,
        'products_images': products_images,
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(
        request,
        'shop/Category/products.html', context=context
    )


def product(request, slug_text):

    product = Product.objects.filter(slug=slug_text)
    if product.exists():
        product = product.first()
    else:
        return HttpResponse('Page not found')

    productq = product.productimage_set.all()

    for it in productq:
        if it.is_main == True:
            main = it.image

    count = product.productimage_set.count()

    return render(
        request,
        'shop/Category/product.html', locals()
    )
