from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from . models import MODELS
# Create your views here.

def index(request):
    model = MODELS.objects.all().values()
    context = {'models':model}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request = request, context = context))

def general(request):
    model = MODELS.objects.all().values()
    context = {'model':model}
    template = loader.get_template('general.html')
    return HttpResponse(template.render(request = request, context = context))

def movie(request, movie_id):
    movie = MODELS.objects.get(id = movie_id)
    context = {'movie':movie}
    template = loader.get_template('movie.html')
    return HttpResponse(template.render(request = request, context = context))