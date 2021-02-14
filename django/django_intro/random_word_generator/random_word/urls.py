from django.urls import path
from . import views

urlpatterns = [
    path('random_word/', views.index),
    path('reset/', views.reset)
]