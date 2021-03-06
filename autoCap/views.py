#Views return the request to the page and send database items
#Queries are filtered and requested here along with django classes

from django.shortcuts import render
from .models import Images
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, "index.html")

def report(request):
    return render(request, "report.html")

def tests(request):
    images = Images.objects.all().filter(split='test')
    paginator = Paginator(images, 40) # Show 40 images per page
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        images = paginator.page(paginator.num_pages)

    return render(request, "tests.html", {'images': images})

def nonelabel(request):
    images = Images.objects.all().filter(split='test', label='none')
    paginator = Paginator(images, 40) # Show 40 images per page
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        images = paginator.page(paginator.num_pages)

    return render(request, "nonelabel.html", {'images': images})