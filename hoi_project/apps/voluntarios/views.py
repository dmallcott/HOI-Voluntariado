from django.shortcuts import render
from apps.voluntarios.models import Voluntario

def consultar_voluntarios(request):
	voluntarios = Voluntario.objects.all().order_by('primer_nombre')
	return render(request, 'consultas/consultarVoluntarios.html', {'voluntarios': voluntarios})


def add_voluntario(request):
    VoluntarioFormSet = modelformset_factory(Voluntario)
    if request.method == 'POST':
        formset = VoluntarioFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return agregar_voluntario(request)
    else:
        formset = VoluntarioFormSet(queryset=Voluntario.objects.none())
        
    return render(request, "templates/agregarVoluntario.html", {
        "formset": formset,
    })
