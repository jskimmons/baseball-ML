from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import TodayGame

from scraper.presentGames import todayGames
import dill as pickle
import numpy as np

from rest_framework import viewsets
from .serializers import TodayGameSerializer

class TodayGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows today's games to be viewed or edited.
    """
    queryset = TodayGame.objects.all()
    serializer_class = TodayGameSerializer


def getPredictions(request):

	games_list = TodayGame.objects.all()

	context = { 'games_list': games_list }

	return render(request, 'baseball/predictions.html', context)


def predict(request):

	TodayGame.objects.all().delete()

	df = todayGames()

	with open("model/model_v1.pk" ,'rb') as f:
		loaded_model = pickle.load(f)

	for row in df.itertuples(index=True, name='Pandas'):

		t1Name=getattr(row, 't1_name')
		t2Name=getattr(row, 't2_name')

		li = [
			getattr(row, 't1_batAvg'), 
			getattr(row, 't2_batAvg'),
			getattr(row, 't1_OBP'), 
			getattr(row, 't2_OBP'), 
			getattr(row, 't1_OPS'), 
			getattr(row, 't2_OPS'),
			getattr(row, 't1_slug'), 
			getattr(row, 't2_slug'),
			getattr(row, 't1_ERA'), 
			getattr(row, 't2_ERA'), 
			]

		a = np.reshape(li, (1, -1))

		t1_winner = loaded_model.predict(a)

		winner = t1Name if loaded_model.predict(a) else t2Name

		q = TodayGame(
			t1_name=t1Name, 
			t2_name=t2Name, 
			t1_batAvg=getattr(row, 't1_batAvg'), 
			t2_batAvg=getattr(row, 't2_batAvg'),
			t1_OBP=getattr(row, 't1_OBP'), 
			t2_OBP=getattr(row, 't2_OBP'), 
			t1_OPS=getattr(row, 't1_OPS'), 
			t2_OPS=getattr(row, 't2_OPS'),
			t1_slug=getattr(row, 't1_slug'), 
			t2_slug=getattr(row, 't2_slug'),
			t1_ERA=getattr(row, 't1_ERA'),
			t2_ERA=getattr(row, 't2_ERA'),
			predictionTeam=winner,
			predictionInt=t1_winner)

		q.save()
	
	games_list = TodayGame.objects.all()

	context = { 'games_list': games_list }

	return HttpResponse("Predictions made boi")





	
