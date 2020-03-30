from django.shortcuts import render

# Create your views here.
from .models import Quote
from django.views.generic import ListView, DetailView
import random

class HomePageView(ListView):
    model = Quote
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list'

class QuotePageView(DetailView):
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'
    def get_object(self):
        all_quotes = Quote.objects.all()
        r = random.randint(0, len(all_quotes))
        q = all_quotes[r]
        return q 
