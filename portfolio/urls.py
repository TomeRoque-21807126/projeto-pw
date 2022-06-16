#  portfolio/urls.py

from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.hero_page_view, name='hero'),
    path('home', views.about_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('quizz', views.quizz, name='quizz'),

    path('blog', views.blog_page_view, name='blog'),
    path('novo/', views.novo_comentario_view, name='novo'),
    path('edita/<int:comentario_id>', views.edita_comentario_view, name='edita'),
    path('apaga/<int:comentario_id>', views.apaga_comentario_view, name='apaga'),
]
