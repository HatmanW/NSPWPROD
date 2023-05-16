from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    """View function for home page of site."""
    num_products = Product.objects.all().count()
    num_categories = Category.objects.all().count()

    context = {
        'num_products': num_products,
        'num_categories': num_categories,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'shop/product/index.html', context=context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def mens_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(name__istartswith = "Men's")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/mens_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def womens_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(name__icontains = "Women's")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/womens_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def kids_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(name__icontains = "Kids'")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/kids_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def search_list(request):
    if request.GET.get('query'):
        search_slug = request.GET.get('query')
        products = Product.objects.filter(Q(name__istartswith=search_slug) | Q(name__istartswith=search_slug))
        products = products.order_by('name')
        return render(request, 'shop/product/search_list.html', {'products': products})
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/search_list.html', {'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product


class ProductCategoryView(LoginRequiredMixin, generic.ListView):
    model = Category
