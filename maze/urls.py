from django.urls import path
import maze.views


urlpatterns = [
    path('', maze.views.index, name='index'),
    path("gameover/", maze.views.gameover, name='gameover'),
    path("2/", maze.views.two, name='two'),
    path("6/", maze.views.six, name='six'),
    path("7/", maze.views.seven, name='seven'),
    path("end/", maze.views.end, name='end'),
]
