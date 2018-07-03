import requests
from bs4 import BeautifulSoup, Comment
import numpy as np
import pandas as pd
import dataAnalysis

years_list = ["2015", "2016", "2017", "2018"]

soup_list = []

# for year in years_list:

# 	url = "https://www.baseball-reference.com/leagues/MLB/{}-schedule.shtml".format(year)

# 	response = requests.get(url)

# 	soup_list.append(BeautifulSoup(response.content, "html.parser"))

# for soup in soup_list:

url = "https://www.baseball-reference.com/leagues/MLB/2017-schedule.shtml"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# get list of links to populate datasheet with

link_list = []

for em in soup.find_all("em"):
	for a in em.find_all("a"):
		link_list.append(a.get("href"))

cols = ['game_id', 't1_name', 't2_name', 't1_batAvg', 't2_batAvg', 't1_OBP', 't2_OBP', 't1_winner?']

data = np.array([cols])

for i in range(0, 2):

	boxScore_url = "https://www.baseball-reference.com{}".format(link_list[i])

	page = requests.get(boxScore_url).text

	com_soup = BeautifulSoup(page, "lxml")
	
	comments=com_soup.find_all(string=lambda text:isinstance(text, Comment))
	
	tables = []
	
	for comment in comments:
		tmpSoup = BeautifulSoup(str(comment), "lxml")
		if tmpSoup.find("table"):
			tables.append(tmpSoup)

	# batting in [1] and [2]
	# pitching in [3]

	team_list = tables[0].find("div", {"class" : "game_summary nohover current"}).find_all("td")
	t1_name = team_list[0].find("a").getText()
	t2_name = team_list[3].find("a").getText()

	winner_list = tables[0].find("div", {"class" : "game_summary nohover current"}).find("tr", {"class" : "winner"}).find_all("td")

	winner = winner_list[0].find("a").getText()

	t1_winner = 0
	if winner == t1_name:
		t1_winner = 1
	
	t = tables[1].find("tfoot")
	t1_batAvg = t.find("td", {'data-stat' : 'batting_avg'}).getText()
	t1_OBP = t.find("td", {'data-stat' : 'onbase_perc'}).getText()

	t = tables[2].find("tfoot")
	t2_batAvg = t.find("td", {'data-stat' : 'batting_avg'}).getText()
	t2_OBP = t.find("td", {'data-stat' : 'onbase_perc'}).getText()


	# build np array

	data = np.vstack([data, [i, t1_name, t2_name, float(t1_batAvg), float(t2_batAvg), float(t1_OBP), float(t2_OBP), int(t1_winner)]])

	print(i)



df = pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:])

dA = dataAnalysis(df)


print(dA.data)