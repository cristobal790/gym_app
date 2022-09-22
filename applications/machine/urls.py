from django.urls import path

from . import views

app_name = 'machines_app'

urlpatterns = [
    path(
        '',
        views.MachinesList.as_view(),
        name='all_machines'
        ),
    path('nueva_maquina/',
         views.AddMachineView.as_view(),
         name="add_machine"
         ),
    path('editar_maquina/<pk>/',
         views.EditMachineView.as_view(),
         name="edit_machine"
    ),
]
