# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
from datetime import date
from apps.voluntariado.views import write_pdf
from apps.voluntariado.models import (
    Organizacion,
    Voluntario,
    Proyecto,
    Servicio
)

# Filters


class InstitucionFilter(SimpleListFilter):
    title = _('Institucion')
    parameter_name = 'institucion'

    def lookups(self, request, model_admin):
        queryset = Organizacion.objects.all()
        return queryset.values_list('id', 'nombre')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(institucion=self.value())

# Admin Models


class OrganizacionAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    actions = ['get_report']

    def get_report(self, request, queryset):
        return write_pdf('pdf/pdf.html', {
                         'pagesize': 'A4',
                         'article': 'this is the article'})


class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['primer_nombre', 'apellido', 'CI', 'get_edad',
                    'institucion']
    search_fields = ['primer_nombre', 'apellido', 'lugar_nacimiento',
                     'CI', 'institucion__nombre']
    list_filter = ['primer_nombre', 'apellido', 'genero', 'lugar_nacimiento',
                   'estado_civil', 'ocupacion',
                   InstitucionFilter, 'grado_instruccion']

    def get_edad(self, obj):
        hoy = date.today()
        fecha = obj.fecha_nacimiento
        return hoy.year - fecha.year - \
            ((hoy.month, hoy.day) < (fecha.month, fecha.day))
    get_edad.short_description = 'Edad'
    get_edad.admin_order_field = '__fecha_nacimiento'


class ProyectoAdmin(admin.ModelAdmin):
    search_fields = ['titulo',
                     'especialidad', 'dependencia', 'estatus']
    list_display = ['titulo', 'especialidad', 'estatus']
    list_filter = ['titulo',
                   'especialidad', 'dependencia', 'estatus']

# Registers
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Voluntario, VoluntarioAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Servicio)
