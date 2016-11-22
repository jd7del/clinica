from django import forms
from consultorio.models import Cita_medica,Usuario


class Form_cita(forms.ModelForm):

	class Meta:
		model = Cita_medica
		
		fields = [
			'fecha_programada',
			'hora_programada',
			'profesional',
			'usuario',
			'observacion',
		]

		labels = {
			'fecha_programada': 'Fecha:',
			'hora_programada': 'Hora:',
			'profesional': 'Profesional:',
			'usuario': 'Usuario:',
			'observacion': 'Observacion:',
		}

		widgets = {
			'fecha_programada': forms.TextInput(attrs={'class':'form-control'}),
			'hora_programada': forms.TextInput(attrs={'class':'form-control'}),
			'profesional': forms.Select(attrs={'class':'form-control'}),
			'usuario': forms.Select(attrs={'class':'form-control'}),
			'observacion': forms.TextInput(attrs={'class':'form-control'}),
		}

class Form_Usuario(forms.ModelForm):
	class Meta:
		model = Usuario
		
		fields = [
			'cedula',
			'nombres',
			'apellidos',
			'passowrd',
		]

		labels = {
			'cedula': 'Cedula:',
			'nombres': 'Nombres:',
			'apellidos': 'Apellidos',
			'passowrd': 'Password:',
		}

		widgets = {
			'cedula': forms.TextInput(attrs={'class':'form-control'}),
			'nombres': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'passowrd': forms.PasswordInput(),
		}
