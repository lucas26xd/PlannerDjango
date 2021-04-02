from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner_list, name='planner_list'),  # get request to retrieve and display all records
    # path('<int:id>/', views.employee_form, name='employee_update'),  # get and post request for update operation
    # path('delete/<int:id>/', views.employee_delete, name='employee_delete'),  # get e post request for delete operation
    # path('list/', views.employee_list, name='employee_list'),  # get request to retrieve and display all records
]
