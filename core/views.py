from django.shortcuts import render
from django.views import generic
# from .models import nomeDoModels
# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'