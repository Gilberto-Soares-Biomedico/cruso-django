from django.urls import path
from app_cadastro import views

urlpatterns = [
    #pagina principal
    path('', views.home, name='home'),
    #relatorio de usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
