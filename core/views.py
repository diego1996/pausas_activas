from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView

from core.models import Company, Activity, ActivePause, Prevent


class IndexTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = Company.objects.get(owner=self.request.user)
        pauses = ActivePause.objects.filter(company=company)
        context['company'] = company
        context['pauses'] = pauses
        return context


class IndexDetailView(DetailView):
    template_name = 'pause-detail.html'
    model = ActivePause
    context_object_name = 'pause'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = Company.objects.get(owner=self.request.user)
        pauses = ActivePause.objects.filter(company=company)
        context['company'] = company
        context['pauses'] = pauses
        return context
