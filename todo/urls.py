from django.urls import path
from . import views

urlpatterns = [
    #add task feature
    path('addTask/',views.addTask,name='addTask'),
    
    #mark as done feature
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    
    #mark as undone feature
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
    
    #edit task feature
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    
    #delete task feature
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
]
