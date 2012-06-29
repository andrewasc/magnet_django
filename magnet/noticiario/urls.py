# coding: utf-8

from django.conf.urls import patterns, include, url
from django.views.generic import DetailView

from .views import HomeView, ListaSecaoView
from .views import Noticia

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<secao>\w+)/$', HomeView.as_view(), name='capa-secao'),
    url(r'^(?P<secao>\w+)/todas/$', ListaSecaoView.as_view(), name='lista-secao'),
    url(r'^news/(?P<pk>\d+)$', DetailView.as_view(model=Noticia), name='noticia-detalhe'),
)
