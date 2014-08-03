from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^consultar/voluntario$', 'voluntarios.views.consultar_voluntarios', name='consultar_voluntarios'),
    url(r'^agregar/voluntario$', 'voluntarios.views.add_voluntario', name='add_voluntario'),
)