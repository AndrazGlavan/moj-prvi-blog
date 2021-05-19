from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist, name='potni_list'),
]