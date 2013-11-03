# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from www.models import Planta, TipoSuelo
from django.core.context_processors import csrf
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombreCientifico','altitud','nombreComun','foto','detalleHoja','distribucion','longitud']
        widgets = {
            'nombreCientifico': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreComun': forms.TextInput(attrs={'class': 'form-control'}),
            'distribucion': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control'}),
            'altitud': forms.TextInput(attrs={'class': 'form-control'}),
        }


@login_required(login_url='/login/')
def index(request):
	if request.method == 'POST': # If the form has been submitted...
		form = PlantaForm(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			obj = form.save(commit=False)
			obj.creador = request.user
			if request.POST['tipoDeSuelo'] == 'other':
				suelo = TipoSuelo(nombre=request.POST['sueloOther'])
				suelo.save()
			else:
				suelo = TipoSuelo.objects.get(nombre=request.POST['tipoDeSuelo'])
			obj.tipoDeSuelo = suelo
			obj.save()

	form = PlantaForm() # An unbound form
	tiposSuelo = TipoSuelo.objects.all()
	plantas = Planta.objects.all()
	context = {	'form':form,
				'plantas':plantas,
				'tiposSuelo': tiposSuelo};

	return render(request, 'index.htm', context)

def detail(request, planta_id):
	planta = get_object_or_404(Planta, pk=planta_id)
	context = {'planta': planta,}
	return render(request, 'planta.htm', context)

def loginView(request):
	if request.user.is_authenticated():
		return redirect('/')
	else:
		if request.method=='POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					# Redirect to a success page.
					return redirect('/')
				else:
					# Return a 'disabled account' error message
					error = 'Su cuenta ha sido deshabilitada.'
					context = {'error': error}
					context.update(csrf(request))
					return render(request, 'login.htm', context)
			else:
				error = 'Su nombre de usuario o contraseña son incorrectos'
				context = {'error': error}
				context.update(csrf(request))
				return render(request, 'login.htm', context)
		else:
			context = {}
			context.update(csrf(request))
			return render(request, 'login.htm', context)

def logoutView(request):
	logout(request)
	return redirect('/login/')