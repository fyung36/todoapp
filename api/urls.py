from django.urls import path
from .views import apiOverview,taskList,taskDetail,createTask,taskUpdate, deleteTask

urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('all_task/', taskList, name='alltask'),
    path('task-detail/<str:pk>/', taskDetail, name='task-detail'),
    path('create_task/',createTask, name='createtask'),
    path('edit_task/<str:pk>/',taskUpdate, name='taskedit'),
    path('delete-task/<str:pk>', deleteTask, name='delete-task'),

]
