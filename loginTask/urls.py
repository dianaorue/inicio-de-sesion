from django.contrib import admin
from django.urls import path, include
from tasks.views import base  # Importa la vista base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Asumiendo que tienes un `urls.py` en la app `task`
    path('', base, name='base'),  # Agrega esta línea
    path('accounts/', include('accounts.urls')), # 追記
]
