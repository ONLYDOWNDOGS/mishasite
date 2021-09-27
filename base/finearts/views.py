from django.views import generic
from django.shortcuts import render
from django.db.models import Q

from . import models

class HomePageView(generic.TemplateView):
    template_name = 'finearts/homepage.html'

class SearchResultsView(generic.ListView):
    model = models.Portfolio
    template_name = 'finearts/search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = models.Portfolio.objects.filter(
            Q(title__icontains=query)
        )
        return object_list