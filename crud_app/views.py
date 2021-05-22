from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Blog

# Create your views here.


def main(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'main.html', context)


def detail(request, id):
    detail_data = get_object_or_404(Blog, pk=id)
    context = {
        'title': detail_data.title,
        'writer': detail_data.writer,
        'address': detail_data.address,
        'pay': detail_data.pay,
        'pub_date': detail_data.pub_date,
        'body': detail_data.body,
        'number': detail_data.number,
        'id': id,
    }
    return render(request, 'detail.html', context)


def apply(request, id):
    detail_data = get_object_or_404(Blog, pk=id)
    detail_data.number += 1
    detail_data.save()
    context = {
        'title': detail_data.title,
        'writer': detail_data.writer,
        'address': detail_data.address,
        'pay': detail_data.pay,
        'pub_date': detail_data.pub_date,
        'body': detail_data.body,
        'number': detail_data.number,
        'id': id,
    }
    return render(request, 'detail.html', context)


def create_page(request):
    return render(request, 'create.html')


def create(request):
    new_data = Blog()
    new_data.title = request.POST['title']
    new_data.writer = request.POST['writer']
    new_data.address = request.POST['address']
    new_data.pay = request.POST['pay']
    new_data.pub_date = timezone.now()
    new_data.body = request.POST['body']
    new_data.save()
    return redirect('main')


def update_page(request, id):
    update_data = get_object_or_404(Blog, pk=id)
    context = {
        'id': id,
        'title': update_data.title,
        'writer': update_data.writer,
        'address': update_data.address,
        'pay': update_data.pay,
        'body': update_data.body,
    }
    return render(request, 'update.html', context)


def update(request, id):
    update_data = get_object_or_404(Blog, pk=id)
    update_data.title = request.POST['title']
    update_data.writer = request.POST['writer']
    update_data.address = request.POST['address']
    update_data.pay = request.POST['pay']
    update_data.pub_date = timezone.now()
    update_data.body = request.POST['body']
    update_data.save()
    return redirect('main')


def delete(request, id):
    delete_data = get_object_or_404(Blog, pk=id)
    delete_data.delete()
    return redirect('main')
