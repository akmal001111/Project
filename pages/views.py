from django.shortcuts import render

from pages.models import *


def home_page_view(request):
    new = NewModel.objects.all()
    four_galleries = GalleriesModel.objects.all()
    context = {
        'news': new,
        'four_galleries': four_galleries
    }
    return render(request, 'index.html', context=context)


def contact_page_view(request):
    return render(request, 'contact.html')


def about_page_view(request):
    return render(request, 'about-company.html')



def blog_detail(request):
    blogs = BlogModel.objects.all().order_by('-created_at')[:6]
    recent_blogs = BlogModel.objects.all().order_by('-updated_at')[:3]
    context = {
        "blogs": blogs,
        "recent_blogs": recent_blogs,
    }
    return render(request, 'blog-single.html', context)