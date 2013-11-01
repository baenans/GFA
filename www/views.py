# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def index(request):
	context = {}
	return render(request, 'index.htm', context)
def login(request):
	context = {}
	return render(request, 'index.htm', context)