from django.contrib import admin
from datetime import date
from apps.voluntarios.models import Voluntario


class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['primer_nombre', 'apellido', 'CI', 'get_edad',
                    'institucion']
    search_fields = ['primer_nombre', 'apellido', 'lugar_nacimiento',
                     'CI', 'institucion']
    list_filter = ['primer_nombre', 'apellido', 'lugar_nacimiento',
                   'institucion', 'genero', 'ocupacion',
                   'estado_civil', 'grado_instruccion']

    def get_edad(self, obj):
        hoy = date.today()
        fecha = obj.fecha_nacimiento
        return hoy.year - fecha.year - \
            ((hoy.month, hoy.day) < (fecha.month, fecha.day))
    get_edad.short_description = 'Edad'
    get_edad.admin_order_field = '__fecha_nacimiento'

admin.site.register(Voluntario, VoluntarioAdmin)
