from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, TemplateView, CreateView, UpdateView
)

from .models import Machine
from .forms import AddMachineForm, EditMachineForm

# Create your views here.


class AddMachineView(LoginRequiredMixin, CreateView):
    template_name = 'machine/add_machine.html'
    model = Machine
    form_class = AddMachineForm
    success_url = reverse_lazy('machines_app:all_machines')
    login_url = reverse_lazy('users_app:login')

class EditMachineView(LoginRequiredMixin, UpdateView):
    template_name = 'machine/edit_machine.html'
    model = Machine
    form_class = AddMachineForm
    success_url = reverse_lazy('machines_app:all_machines')
    login_url = reverse_lazy('users_app:login')



class MachinesList(LoginRequiredMixin, ListView):
    template_name = 'machine/list_all.html'
    paginate_by = 10
    ordering = 'name'
    model = Machine
    login_url = reverse_lazy('users_app:login')