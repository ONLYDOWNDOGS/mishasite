from django.views import generic
from django.shortcuts import render
from django.db.models import Q

from .models import Portfolio

class HomePageView(generic.TemplateView):
    template_name = 'finearts/homepage.html'
    
class SearchResultsView(generic.ListView):
    model = Portfolio
    template_name = 'finearts/search_results.html'
    context_object_name = 'object_list'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Portfolio.objects.filter(
            Q(artstyle__icontains=query)
        )
        return object_list

class ContactView(generic.TemplateView):
    template_name = 'finearts/contact.html'

class ReelsView(generic.ListView):
    template_name = 'finearts/reels.html'