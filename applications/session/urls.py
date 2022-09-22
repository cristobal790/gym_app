from django.urls import path

from . import views

app_name = 'sessions_app'

urlpatterns = [
    path(
        '',
        views.SessionsList.as_view(),
        name='all_sessions'
    ),
    path('nueva_session/',
         views.AddSessionView.as_view(),
         name="add_sessions"
    ),
    path('editar_session/<pk>/',
         views.EditSessionView.as_view(),
         name="edit_sessions"
    ),
    path('nueva_sesion_de_tiempo/',
         views.AddTimeSessionView.as_view(),
         name="add_time_sessions"
    ),
]
