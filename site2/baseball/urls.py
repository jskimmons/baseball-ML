from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:num_games>/', views.load, name='load'),
	path('games/', views.detail, name='detail'),
	path('games/<int:game_id>/', views.specific, name='specific'),
]
