from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name = 'home_index'),
    path('resumo/',views.resumo_view,name = 'home_resumo'),
    path('sobre/',views.sobre_view,name = 'home_sobre'),
]

