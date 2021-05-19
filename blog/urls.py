from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('prazna/', views.prazna_stran, name="prazna_stran")
]