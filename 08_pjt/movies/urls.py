from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
    path('<int:movie_pk>/like/', views.movie_like, name='movie_like'),
]
