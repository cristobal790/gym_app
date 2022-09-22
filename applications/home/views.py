from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView
)


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    login_url = reverse_lazy('user_app:login')
