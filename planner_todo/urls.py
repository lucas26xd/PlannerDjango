from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner_list, name='planner_list'),
]
