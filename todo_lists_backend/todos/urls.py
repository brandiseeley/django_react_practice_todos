from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:list_id>/", views.todo_list, name="todo_list"),
    path("<int:list_id>/new/", views.new, name="new"),
    path("<int:list_id>/todo/<int:todo_id>/edit/", views.edit_todo, name="edit_todo"),
    path("api/lists/", views.api_lists, name="api_lists"),
    path("api/list/<int:list_id>", views.api_list, name="api_list"),
]