from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL for the task list
    path('add_task/', views.add_task, name='add_task'),  # URL for adding a task
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),  # URL for deleting a task
    path('mark_done/<int:task_id>/', views.mark_done, name='mark_done'),  # URL for marking a task as done
]

