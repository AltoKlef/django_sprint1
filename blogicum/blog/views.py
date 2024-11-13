from django.shortcuts import render


def index(request):
    template_name = 'blog/index.html'
    return render(request, template_name) 


def post_detail(request, pk):
    template_name = 'blog/detail.html'
    return render(request, template_name) 


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    return render(request, template_name) 