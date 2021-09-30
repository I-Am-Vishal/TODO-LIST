from django.urls import path
from .views import RegisterPage, TaskDelete, TaskDetail, TaskList , TaskCreate, TaskUpdate,CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',TaskList.as_view(),name="tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(),name="task"),
    path('task-create/',TaskCreate.as_view(),name="task-create"),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name="task-update"),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name="task-delete"),
    path('task-login/',CustomLoginView.as_view(),name="task-login"),
    path('task-logout/',LogoutView.as_view(next_page='task-login'),name="task-logout"),
    path('task-register/',RegisterPage.as_view(),name="task-register"),
]
