from apps.voluntarios.models import Voluntario


class VoluntarioForm(forms.ModelForm):
	class Meta:
	    model = Voluntario
