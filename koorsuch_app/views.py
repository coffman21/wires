from django.shortcuts import render


def index(request):
    s = "!!!"
    context = {
        "???": s
    }
    return render(request, 'koorsuch/index.html', context)
