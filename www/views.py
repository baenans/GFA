# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from www.models import Planta, TipoSuelo
from django.core.context_processors import csrf

# Create your views here.

@login_required(login_url='/login/')
def index(request):
	if request.method=='POST':
		if request.POST['tipoDeSuelo'] == 'other':
			suelo = TipoSuelo(nombre=request.POST['sueloOther'])
			suelo.save()
		else:
			suelo = TipoSuelo.objects.get(nombre=request.POST['tipoDeSuelo'])

		nuevaPlanta = Planta(
			nombreComun=request.POST['cname'],
			nombreCientifico=request.POST['scname'],
			distribucion=request.POST['dist'],
			longitud=request.POST['longitud'],
			altitud=request.POST['altitud'],
			tipoDeSuelo=suelo,
			creador=request.user)
		nuevaPlanta.save()
		
	plantas = Planta.objects.all()
	tiposSuelo = TipoSuelo.objects.all()
	context = {	'plantas':plantas,
				'tiposSuelo':tiposSuelo}
	context.update(csrf(request))
	return render(request, 'index.htm', context)

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