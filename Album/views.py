from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,FormView,UpdateView,DeleteView
from django.views.generic import TemplateView
from .models import AlbumModle
from .forms import AlbumForm,RegistrationForm,User,AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout,login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
# Create your views here.


class HomeView(ListView):
    model = AlbumModle
    template_name = 'home.html'
    context_object_name = 'album'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['page']='Home Page'
        context['title']='Albums'
        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class AlbumFormView(CreateView):
    model = AlbumModle
    form_class = AlbumForm
    template_name='forms.html'
    success_url = reverse_lazy('home')



@method_decorator(login_required(login_url='login'), name='dispatch')
class AlbumEditFormView(UpdateView):
    model = AlbumModle
    form_class = AlbumForm
    template_name='forms.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['page'] = 'update'
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class AlbumDeleteFormView(DeleteView):
    model = AlbumModle
    template_name='forms.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['page'] = 'delete'
        return context


class RegistrationFormView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name='forms.html'
    success_url = reverse_lazy('home')




class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'forms.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

