from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Models

# Create your views here.

def index(request):
    model = Models.objects.all().values()
    context = {'model':model}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request = request, context = context))