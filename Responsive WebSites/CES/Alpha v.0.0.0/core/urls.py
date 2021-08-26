from django.db.models.indexes import Index
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import IndexView, NoticiasView, NewsView, ContatoView, EventosView, AlunoAreaView, ListNoticiaView, UpdateNoticiaView, DeleteNoticiaView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('news/', NewsView.as_view(), name='news'),
    path('noticias/<slug:slug_id>', NoticiasView.as_view(), name='noticias'),
    path('noticias/administration/news', ListNoticiaView.as_view(), name='listar_noticia'),
    path('noticias/administration/news/<int:pk>', UpdateNoticiaView.as_view(), name='update_noticia'),
    path('noticias/administration/news/delete/<int:pk>', DeleteNoticiaView.as_view(), name='delete_noticia'),
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('contas/logado/aluno/<slug:slug_id>', AlunoAreaView.as_view(), name='aluno'),

]