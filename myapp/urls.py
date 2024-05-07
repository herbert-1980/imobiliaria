from django.urls import path, include
from myapp import views
from .views import subscribe

urlpatterns = [
    path('', views.lista_locacao, name='lista_locacao'), 
    path('form_cliente/', views.form_cliente, name='cliente_create'), 
    path('form_imovel/', views.form_imovel, name='imovel_create'),
    path('form_locacao/<int:id>', views.form_locacao, name='locacao_create'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('subscribe/', subscribe, name='newsletter_success'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]
