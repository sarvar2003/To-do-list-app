from django.urls import path

from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name = 'delete_task'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name = 'update_task'),
    path('new/', TaskCreateView.as_view(), name = 'new_task'),
    path('', TaskListView.as_view(), name = 'task_list'),
]