from django.core.mail import send_mail, BadHeaderError
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .models import Portfolio
from .forms import ContactForm

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

class ReelsView(generic.TemplateView):
    template_name = 'finearts/reels.html'

def contactview(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['mishajohn@protonmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'finearts/contact_success.html')
    return render(request, 'finearts/contact.html', {'form': form})