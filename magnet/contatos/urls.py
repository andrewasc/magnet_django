# coding: utf-8

from django.conf.urls import patterns, include, url

from .views import contato_simples, contato_fones
from .views import contato_simples_com_modelform
from .views import contato_fones_com_modelform
from .views import lista_contatos, editar_contato

urlpatterns = patterns('',
    url(r'^simples/$', contato_simples, name='form-contato-simples'),
    url(r'^simplesmf/$', contato_simples_com_modelform, name='modelform-form-contato-simples'),
    url(r'^fones/$', contato_fones, name='form-contato-fones'),
    url(r'^fonesmf/$', contato_fones_com_modelform, name='modelform-form-contato-fones'),
    url(r'^listar/$', lista_contatos, name='lista-contatos'),
    url(r'^editar/(\d+)/$', editar_contato, name='editar-contato'),
)
