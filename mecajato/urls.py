from django.contrib import admin
from django.urls import path, include
from servicos.views import listar_servico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_servico),
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls')),
]
