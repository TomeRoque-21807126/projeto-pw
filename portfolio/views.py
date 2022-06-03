#  hello/views.py

from django.shortcuts import render
import datetime


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }
    return render(request, 'home.html', context)


def about_page_view(request):
    return render(request, 'about.html')


def licenciatura_page_view(request):
    return render(request, 'licenciatura.html')


def projetos_page_view(request):
    return render(request, 'projetos.html')

