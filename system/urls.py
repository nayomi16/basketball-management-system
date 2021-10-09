from django.urls import path
from .views import HomeView, PlayerView

urlpatterns = [
    path('home', HomeView.as_view()),
    # path('login/<string:user>', LoginView.as_view())
    path('player/<int:user>', PlayerView)
]