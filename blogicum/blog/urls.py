from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id>/', views.post_detail),
    path('<slug:category_slug>/', views.category_posts)
]