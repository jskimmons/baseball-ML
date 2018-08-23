from django.urls import path

from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'games', views.TodayGameViewSet)

urlpatterns = [
	path('predict/', views.predict, name='predict'),
	path('results/', views.getPredictions, name='results'),
	url(r'^', include(router.urls)),
]
