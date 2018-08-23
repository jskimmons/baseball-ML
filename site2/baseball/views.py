from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Game
from .models import TodayGame

from scraper.scraper2 import scrape
from scraper.presentGames import todayGames
import dill as pickle
import numpy as np
import datetime

def index(request):
	return HttpResponse("Hey!")

def load(request, num_games):
	
	df = scrape(num_games)

	for row in df.itertuples(index=True, name='Pandas'):

		q = Game(
			date=getattr(row, 'date'),
			t1_name=getattr(row, 't1_name'), 
			t2_name=getattr(row, 't2_name'), 
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
			t1_winner=row[14]) # TODO clear db and fix t1_winner? bug, wHY 14?

		q.save()

	return HttpResponse("Database loaded with {} games :)".format(num_games))

def detail(request):

	games_list = Game.objects.all()

	context = { 'games_list': games_list }

	return render(request, 'baseball/detail.html', context)

def specific(request, game_id):

	game = Game.objects.get(pk = game_id)

	context = {'game' : game}

	return render(request, 'baseball/specific.html', context)

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

		winner = t1Name if loaded_model.predict(a) else t2Name

		q = TodayGame(
			date=str(datetime.datetime.now()),
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
			prediction=winner)

		q.save()
	
	games_list = TodayGame.objects.all()

	context = { 'games_list': games_list }

	return render(request, 'baseball/predictions.html', context)
	




	
