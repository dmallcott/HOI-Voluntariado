from django.contrib import admin
from apps.proyectos.models import Proyecto
from apps.proyectos.models import ProyectoVoluntario


class ProyectoAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'institucion',
                     'especialidad', 'dependencia', 'estatus']
    list_display = ['titulo', 'institucion', 'estatus']
    list_filter = ['titulo', 'institucion',
                   'especialidad', 'dependencia', 'estatus']


class InstitucionFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ('Institucion')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'institucion'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        result = []
        for proyecto in Proyecto.objects.all():
            temp = (proyecto.institucion, proyecto.institucion)
            if not temp in result:
                result.append(temp)

        return result

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        return queryset.filter(Institucion=self.value())


class ProyectoVoluntarioAdmin(admin.ModelAdmin):
    search_fields = ['proyecto', 'voluntario']
    list_display = [
        'get_proyecto', 'get_institucion', 'voluntario', 'get_CI', 'horas']
    #list_filter = ['get_proyecto']

    def get_proyecto(self, obj):
        return obj.proyecto.titulo
    get_proyecto.short_description = 'Proyecto'
    get_proyecto.admin_order_field = 'proyecto__titulo'

    def get_institucion(self, obj):
        return obj.proyecto.institucion
    get_institucion.short_description = 'Institucion'
    get_institucion.admin_order_field = 'proyecto__institucion'

    def get_CI(self, obj):
        return obj.voluntario.CI
    get_CI.short_description = 'Cedula'
    get_CI.admin_order_field = 'voluntario__CI'


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(ProyectoVoluntario, ProyectoVoluntarioAdmin)
