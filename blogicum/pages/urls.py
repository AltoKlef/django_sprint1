
from django.urls import path  # type: ignore

from . import views


urlpatterns = [
    path('about/', views.about),
    path('rules/', views.rules)
]