from django.views import generic
from django.shortcuts import render
from django.db.models import Q

from .models import Portfolio

class HomePageView(generic.ListView):
    model = Portfolio
    context_object_name = 'object_list'
    template_name = 'finearts/homepage.html'
    queryset = Portfolio.objects.filter(status=1).order_by('-pub_date')

class SearchResultsView(generic.ListView):
    model = Portfolio
    template_name = 'finearts/search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Portfolio.objects.filter(
            Q(title__icontains=query)
        )
        return object_list