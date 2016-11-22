from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView

from consultorio.models import Cita_medica,Usuario
from consultorio.forms import Form_cita,Form_Usuario
from django.utils.encoding import smart_str
import bcrypt

	#RegistroUsuario(CreateView):
	#model = User
	#fields = fields = ['first_name','last_name','email','username','password']
	#template_name = "consultorio/form_add_user.html"
	#from_class = UserCreationForm
	#success_url = reverse_lazy('consultorio:index')
# Create your views here.

def index(request):
	return render(request, "consultorio/index.html")

def RegistroUsuario(request):
	if request.method == 'POST':
		form = Form_Usuario(request.POST)
		if form.is_valid():
			clearPassNoHash = form.cleaned_data['passowrd']
			form.passowrd = bcrypt.hashpw(clearPassNoHash.encode("utf-8"), bcrypt.gensalt(14) )
			form.save()
		return redirect('consultorio:index')
	else:
		form = Form_Usuario()

	return render(request, 'consultorio/form_add_user.html', {'form':form})


def add_cita(request):
	if request.method == 'POST':
		form = Form_cita(request.POST)
		if form.is_valid():
			form.save()
			return redirect('consultorio:index')
	else:
		form = Form_cita()

	return render(request, 'consultorio/form_add_cita.html', {'form':form})

class Listar_cita(ListView):
	model = Cita_medica
	template_name = 'consultorio/list_citas.html'

def editar_cita(request, id_cita):
	cita = Cita_medica.objects.get(id=id_cita)
	if request.method == "GET":
		form = Form_cita(instance=cita)
	else:
		form = Form_cita(request.POST, instance=cita)
		if form.is_valid():
			form.save()
		return redirect('consultorio:list_c')
	return render(request, 'consultorio/form_add_cita.html', {'form':form})

def cancelar_cita(request, id_cita):
	cita = Cita_medica.objects.get(id=id_cita)
	if request.method == "POST":
		cita.delete()
		return redirect('consultorio:list_c')
	return render(request, 'consultorio/cancelar_cita.html', {'cita':cita})
