from django.urls import path
from .views import CauchView

urlpatterns = [
    path('team', CauchView.as_view()),
]