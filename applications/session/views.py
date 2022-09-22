import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,)

from .forms import (AddSessionForm,
                    EditSessionForm,
                    AddTimeSessionForm,
                    EditTimeSessionForm,
                    )

from .models import Session, TimeSession


# Create your views here.
class SessionsList(LoginRequiredMixin, ListView):
    template_name = 'session/list_all.html'
    paginate_by = 10
    ordering = 'id'
    model = Session
    login_url = reverse_lazy('users_app:login')


class AddSessionView(LoginRequiredMixin, CreateView):
    template_name = 'session/add_session.html'
    model = Session
    form_class = AddSessionForm
    success_url = reverse_lazy('sessions_app:all_sessions')
    login_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        form.cleaned_data["uploading_time"] = datetime.datetime.now()
        return super(AddSessionView, self).form_valid(form)


class EditSessionView(LoginRequiredMixin, UpdateView):
    template_name = 'session/edit_session.html'
    model = Session
    form_class = EditSessionForm
    success_url = reverse_lazy('sessions_app:all_sessions')
    login_url = reverse_lazy('users_app:login')


class AddTimeSessionView(LoginRequiredMixin, CreateView):
    template_name = 'session/add_time_session.html'
    model = TimeSession
    form_class = AddTimeSessionForm
    success_url = reverse_lazy('sessions_app:all_sessions')
    login_url = reverse_lazy('users_app:login')


class EditTimeSessionView(LoginRequiredMixin, UpdateView):
    template_name = 'session/edit_time_session.html'
    model = TimeSession
    form_class = EditTimeSessionForm
    success_url = reverse_lazy('sessions_app:all_sessions')
    login_url = reverse_lazy('users_app:login')
