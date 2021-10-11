from django.shortcuts import render


# Create your views here .
def index(request):
    return render(request, 'index.html')


def registration(request):
    return render(request, 'registration.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def membership(request):
    return render(request, 'membership.html')


def trainers(request):
    return render(request, 'trainers.html')
