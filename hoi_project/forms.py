from django import forms

class ReportForm(forms.Form):
    fecha = forms.DateField(label="Fecha", input_formats=['%m/%Y'])
    
