from django.urls import path
2
from . import views
3
 
4
urlpatterns = [
5
path('hello/', views.hello),
6
]
