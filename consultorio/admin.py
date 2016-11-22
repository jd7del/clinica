from django.contrib import admin
from consultorio.models import Usuario,Profesional,Cita_medica

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Profesional)
admin.site.register(Cita_medica)
