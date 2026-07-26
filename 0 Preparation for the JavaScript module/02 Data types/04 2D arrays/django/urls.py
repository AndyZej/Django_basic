from django.urls import path
from . import views

urlpatterns = [
    path("arrays/", views.arrays, name="arrays"),
]