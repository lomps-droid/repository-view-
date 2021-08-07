from django.urls import path
from django.urls.resolvers import URLPattern

from .views import index, contato, update_page

urlpatterns = [
    path('', index),
    path('contato/', contato, name='contato'),
    path('updates/', update_page),

]