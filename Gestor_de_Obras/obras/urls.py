from django.urls import path
from . import views

app_name = "obras"

urlpatterns = [
    path('', views.listar_obras, name='listar_obras'),
    path('criar/', views.criar_obra, name='criar_obra'),
    path('<int:obra_id>/editar/', views.editar_obra, name='editar_obra'),
    path('<int:obra_id>/excluir/', views.excluir_obra, name='excluir_obra'),
    path('buscar-cep/', views.buscar_cep, name='buscar_cep'),

]