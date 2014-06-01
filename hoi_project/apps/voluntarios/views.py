from django.shortcuts import render
from apps.voluntarios.models import Voluntario

def consultar_voluntarios(request):
	voluntarios = Voluntario.objects.all().order_by('primer_nombre')
	return render(request, 'consultas/consultarVoluntarios.html', {'voluntarios': voluntarios})
