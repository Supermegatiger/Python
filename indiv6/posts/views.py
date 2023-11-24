from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Иди да лесом')


def test(request):
    context = {
        'title': 'мда',
        'div': 'не прошло и года',
    }
    return render(request,'index.html', context)
