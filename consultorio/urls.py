"""final_jd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from consultorio.views import index, RegistroUsuario, add_cita, Listar_cita, editar_cita, cancelar_cita
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^user_add', login_required(RegistroUsuario), name='user_add'),
    url(r'^add_cita', login_required(add_cita), name='add_cita'),
    url(r'^listar_citas', login_required(Listar_cita.as_view()), name='list_c'),
    url(r'^editar_cita/(?P<id_cita>\d+)/$', editar_cita, name='edt_c'),
    url(r'^cancelar_cita/(?P<id_cita>\d+)/$', cancelar_cita, name='del_c'),
]
