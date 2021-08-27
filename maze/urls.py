from django.urls import path
import maze.views


urlpatterns = [
    path('', maze.views.index),
]
