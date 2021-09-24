from django.views import generic
from django.shortcuts import render

from . import models

class HomePageView(generic.ListView):
    model = models.Portfolio
    template_name = 'finearts/homepage.html'
    context_object_name = 'pics_list'
