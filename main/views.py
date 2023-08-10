from django.shortcuts import render


def index(request):
    return render(request, 'main/index1.html')


def about(request):
    return render(request, 'main/info1.html')


def contacts(request):
    return render(request, 'main/contact.html')


def blog(request):
    return render(request, 'main/blog.html')


def ourwork(request):
    return render(request, 'main/ourwork.html')


def download(request):
    return render(request, 'main/download.html')
