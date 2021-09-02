from django.urls import path
import maze.views


urlpatterns = [
    path('', maze.views.signin, name='login'),
    path('game/', maze.views.game, name='game'),
    path('signup/', maze.views.signup, name='signup'),
    path('logout/', maze.views.logout, name='logout')


]
