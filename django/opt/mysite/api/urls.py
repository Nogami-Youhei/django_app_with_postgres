from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path("register_choice/", views.register_choice, name="api_register_choice"),
]