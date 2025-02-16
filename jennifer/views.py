from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request = request))