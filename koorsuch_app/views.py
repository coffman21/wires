from django.shortcuts import render


def index(request):

    context = {}
    return render(request, 'koorsuch/index.html', context)
