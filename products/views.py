from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Category, Product, Sub_category
from math import ceil
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from cart.models import Cart


# Create your views here.


def index(request):
    cate = Category.objects.all()
    pro = Product.objects.all()
    n = len(pro)
    nslide = n // 4 + ceil(n // 4) - (n // 4)
    page = {
        'cate': cate,
        'pro': pro,
        'nslide': nslide,
        'range': range(1, nslide)
    }
    return render(request, 'index.html', page)


class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'pro'
    ordering = ['name']

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


def card(request):
    cate = Category.objects.all()
    pro = Product.objects.all()
    page = {
        'cate': cate,
        'pro': pro
    }
    return render(request, 'card.html', page)


class ProductListView_card(ListView):
    model = Product
    template_name = 'card.html'
    context_object_name = 'pro'
    ordering = ['- name']

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView_card, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


def card1(request):
    cate = Category.objects.all()
    pro = Product.objects.all()
    page = {
        'cate': cate,
        'pro': pro
    }
    return render(request, 'card1.html', page)


class ProductListView_card1(ListView):
    model = Product
    template_name = 'card1.html'
    context_object_name = 'pro'
    ordering = ['- name']

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView_card1, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


def card2(request):
    cate = Category.objects.all()
    pro = Product.objects.all()
    page = {
        'cate': cate,
        'pro': pro
    }
    return render(request, 'card2.html', page)


class ProductListView_card2(ListView):
    model = Product
    template_name = 'card2.html'
    context_object_name = 'pro'
    ordering = ['- name']

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView_card2, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


def About_us(request):
    return render(request, 'About us.html')


def website(request):
    return render(request, 'websites.html')
