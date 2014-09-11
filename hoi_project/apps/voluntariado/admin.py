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
from apps.voluntariado.forms import MonthlyForm, AnualForm
from django.shortcuts import render

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
    actions = ['generar_reporte_mes', 'generar_reporte_ano']

    def generar_reporte_mes(modeladmin, request, queryset):
        form = None

        if 'apply' in request.POST:

            form = MonthlyForm(request.POST)
            if form.is_valid():
                lista_organizaciones = []
                for organizacion in queryset:
                    lista_organizaciones.append(
                        (
                            organizacion.nombre,
                            organizacion.horas_mes(
                                form.cleaned_data['mes'],
                                form.cleaned_data['ano'])
                        )
                    )

                return write_pdf('pdf/organizaciones/reporte_mensual.html', {
                                 'pagesize': 'A4',
                                 'lista_organizaciones': lista_organizaciones})

        if not form:
            form = MonthlyForm(
                initial={'_selected_action':
                         request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        return render(request, 'admin/organizacion_mes.html',
                      {'items': queryset, 'form': form,
                       'title': u'Reporte mensual - Organizacion'})

    generar_reporte_mes.short_description = u"Generar reporte mensual"

    def generar_reporte_ano(modeladmin, request, queryset):
        form = None

        if 'apply' in request.POST:

            form = AnualForm(request.POST)
            if form.is_valid():
                lista_organizaciones = []
                for organizacion in queryset:
                    lista_organizaciones.append(
                        (
                            organizacion.nombre,
                            organizacion.horas_ano(
                                form.cleaned_data['ano'])
                        )
                    )

                return write_pdf('pdf/organizaciones/reporte_anual.html', {
                                 'pagesize': 'A4',
                                 'lista_organizaciones': lista_organizaciones})

        if not form:
            form = AnualForm(
                initial={'_selected_action':
                         request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        return render(request, 'admin/organizacion_ano.html',
                      {'items': queryset, 'form': form,
                       'title': u'Reporte anual - Organizacion'})

    generar_reporte_ano.short_description = u"Generar reporte anual"


class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['primer_nombre', 'apellido', 'CI', 'get_edad',
                    'institucion']
    search_fields = ['primer_nombre', 'apellido', 'lugar_nacimiento',
                     'CI', 'institucion__nombre']
    list_filter = ['primer_nombre', 'apellido', 'genero', 'lugar_nacimiento',
                   'estado_civil', 'ocupacion',
                   InstitucionFilter, 'grado_instruccion']
    actions = ['generar_reporte_mes', 'generar_reporte_ano']

    def get_edad(self, obj):
        hoy = date.today()
        fecha = obj.fecha_nacimiento
        return hoy.year - fecha.year - \
            ((hoy.month, hoy.day) < (fecha.month, fecha.day))
    get_edad.short_description = 'Edad'
    get_edad.admin_order_field = '__fecha_nacimiento'

    def generar_reporte_mes(modeladmin, request, queryset):
        form = None

        if 'apply' in request.POST:

            form = MonthlyForm(request.POST)
            if form.is_valid():
                lista_voluntarios = []
                for voluntario in queryset:
                    lista_voluntarios.append(
                        (
                            voluntario.primer_nombre +
                            " " + voluntario.apellido,
                            voluntario.horas_mes(
                                form.cleaned_data['mes'],
                                form.cleaned_data['ano'])
                        )
                    )

                return write_pdf('pdf/voluntarios/reporte_mensual.html', {
                                 'pagesize': 'A4',
                                 'lista_voluntarios': lista_voluntarios})

        if not form:
            form = MonthlyForm(
                initial={'_selected_action':
                         request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        return render(request, 'admin/organizacion_mes.html',
                      {'items': queryset, 'form': form,
                       'title': u'Reporte mensual - Voluntario'})

    generar_reporte_mes.short_description = u"Generar reporte mensual"

    def generar_reporte_ano(modeladmin, request, queryset):
        form = None

        if 'apply' in request.POST:

            form = AnualForm(request.POST)
            if form.is_valid():
                lista_voluntarios = []
                for voluntario in queryset:
                    lista_voluntarios.append(
                        (
                            voluntario.primer_nombre +
                            " " + voluntario.apellido,
                            voluntario.horas_ano(
                                form.cleaned_data['ano'])
                        )
                    )

                return write_pdf('pdf/voluntarios/reporte_anual.html', {
                                 'pagesize': 'A4',
                                 'lista_voluntarios': lista_voluntarios})

        if not form:
            form = AnualForm(
                initial={'_selected_action':
                         request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        return render(request, 'admin/organizacion_ano.html',
                      {'items': queryset, 'form': form,
                       'title': u'Reporte anual - Voluntario'})

    generar_reporte_ano.short_description = u"Generar reporte anual"


class ProyectoAdmin(admin.ModelAdmin):
    search_fields = ['titulo',
                     'especialidad', 'dependencia', 'estatus']
    list_display = ['titulo', 'especialidad', 'estatus']
    list_filter = ['titulo',
                   'especialidad', 'dependencia', 'estatus']
    actions = ['generar_reporte_mes', 'generar_reporte_ano']

    def generar_reporte_mes(modeladmin, request, queryset):
        form = None

        if 'apply' in request.POST:

            form = MonthlyForm(request.POST)
            if form.is_valid():
                lista_proyectos = []
                for proyecto in queryset:
                    lista_proyectos.append(
                        (
                            proyecto.titulo,
                            proyecto.horas_mes(
                                form.cleaned_data['mes'],
                                form.cleaned_data['ano'])
                        )
                    )

                return write_pdf('pdf/proyectos/reporte_mensual.html', {
                                 'pagesize': 'A4',
                                 'lista_proyectos': lista_proyectos})

        if not form:
            form = MonthlyForm(
                initial={'_selected_action':
                         request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        return render(request, 'admin/organizacion_mes.html',
                      {'items': queryset, 'form': form,
                       'title': u'Reporte mensual - Proyecto'})

    generar_reporte_mes.short_description = u"Generar reporte mensual"

    def generar_reporte_ano(modeladmin, request, queryset):
        form = None

        if 'apply' in request.POST:

            form = AnualForm(request.POST)
            if form.is_valid():
                lista_proyectos = []
                for proyecto in queryset:
                    lista_proyectos.append(
                        (
                            proyecto.titulo,
                            proyecto.horas_ano(
                                form.cleaned_data['ano'])
                        )
                    )

                return write_pdf('pdf/proyectos/reporte_anual.html', {
                                 'pagesize': 'A4',
                                 'lista_proyectos': lista_proyectos})

        if not form:
            form = AnualForm(
                initial={'_selected_action':
                         request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        return render(request, 'admin/organizacion_ano.html',
                      {'items': queryset, 'form': form,
                       'title': u'Reporte anual - Proyecto'})

    generar_reporte_ano.short_description = u"Generar reporte anual"

# Registers
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Voluntario, VoluntarioAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Servicio)
