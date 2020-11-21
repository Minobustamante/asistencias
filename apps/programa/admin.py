from django.contrib import admin
from apps.programa.models import Programa, TipoAsistencia, AsignacionBeneficio
# Register your models here.

admin.site.register(Programa)
admin.site.register(TipoAsistencia)
admin.site.register(AsignacionBeneficio)