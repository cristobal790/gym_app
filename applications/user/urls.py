from django.urls import path

from .views import redirect_view

app_name = "user_app"

urlpatterns = [
    path('', redirect_view)

]
