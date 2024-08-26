from django.urls import path
from . import views

urlpatterns = [
    path("", views.display),
    path('vista1/',views.vista1)
]