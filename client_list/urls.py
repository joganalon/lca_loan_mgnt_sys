from django.urls import path
from . import views

urlpatterns = [
    path("", views.client_list, name="clients"),
    path('create/', views.client_create, name='client_create'),
]
