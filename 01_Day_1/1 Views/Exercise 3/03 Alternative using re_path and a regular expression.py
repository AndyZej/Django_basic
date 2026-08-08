from django.urls import re_path
2
from . import views
3
 
4
urlpatterns = [
5
re_path(r'^hello/$', views.hello),
6
]
