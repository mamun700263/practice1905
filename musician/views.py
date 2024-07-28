from django.shortcuts import render
from . import models,forms
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class MusicianFormView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'forms.html'
    success_url = reverse_lazy('home')


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class MusicianEditFormView(UpdateView):
    model= models.Musician
    form_class = forms.MusicianForm
    template_name = 'forms.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['page']='update'
        return context
