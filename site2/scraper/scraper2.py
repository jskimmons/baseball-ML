import requests
from bs4 import BeautifulSoup, Comment
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

years_list = ["2015", "2016", "2017", "2018"]

soup_list = []

# for year in years_list:

# 	url = "https://www.baseball-reference.com/leagues/MLB/{}-schedule.shtml".format(year)

# 	response = requests.get(url)

# 	soup_list.append(BeautifulSoup(response.content, "html.parser"))

# for soup in soup_list:

def scrape(g):

	url = "https://www.baseball-reference.com/leagues/MLB/2017-schedule.shtml"

	response = requests.get(url)

	soup = BeautifulSoup(response.content, "html.parser")

	# get list of links to populate datasheet with

	link_list = []

	for em in soup.find_all("em"):
		for a in em.find_all("a"):
			link_list.append(a.get("href"))

	cols = ['game_id', 'date', 't1_name', 't2_name', 't1_batAvg', 't2_batAvg', 't1_OBP', 't2_OBP', 't1_OPS', 't2_OPS', 't1_slug', 't2_slug', 't1_ERA', 't2_ERA', 't1_winner?']
	# cols2 = ['game_id', 't1_batAvg', 't2_batAvg', 't1_OBP', 't2_OBP', 't1_OPS', 't2_OPS', 't1_slug', 't2_slug', 't1_ERA', 't2_ERA', 't1_winner?']

	data = np.array([cols])
	# data2 = np.array([cols2])

	# fp = open('test.txt', 'w')

	# g = int(input("How many games? \n"))

	for i in range(0, g + 1):

		boxScore_url = "https://www.baseball-reference.com{}".format(link_list[i])

		page = requests.get(boxScore_url).text

		soup = BeautifulSoup(page, "lxml")

		# get date

		date = soup.find("div", {"class" : "scorebox_meta"}).find_all("div")[0].getText()
		
		comments=soup.find_all(string=lambda text:isinstance(text, Comment))
		
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

		# batting
		
		t = tables[1].find("tfoot")
		t1_batAvg = t.find("td", {'data-stat' : 'batting_avg'}).getText()
		t1_OBP = t.find("td", {'data-stat' : 'onbase_perc'}).getText()
		t1_slug = t.find("td", {'data-stat' : 'slugging_perc'}).getText()
		t1_OPS = t.find("td", {'data-stat' : 'onbase_plus_slugging'}).getText()

		t = tables[2].find("tfoot")
		t2_batAvg = t.find("td", {'data-stat' : 'batting_avg'}).getText()
		t2_OBP = t.find("td", {'data-stat' : 'onbase_perc'}).getText()
		t2_slug = t.find("td", {'data-stat' : 'slugging_perc'}).getText()
		t2_OPS = t.find("td", {'data-stat' : 'onbase_plus_slugging'}).getText()


		# pitching

		pitch_list = tables[3].find_all("tfoot")
		t1_era = pitch_list[0].find("td", {"data-stat" : "earned_run_avg"}).getText()
		t2_era = pitch_list[1].find("td", {"data-stat" : "earned_run_avg"}).getText()


		# build np array

		data = np.vstack([data, [i, date, t1_name, t2_name, t1_batAvg, t2_batAvg, t1_OBP, t2_OBP, t1_OPS, t2_OPS, t1_slug, t2_slug, t1_era, t2_era, t1_winner]])

		# data2 = np.vstack([data2, [i, t1_batAvg, t2_batAvg, t1_OBP, t2_OBP, t1_OPS, t2_OPS, t1_slug, t2_slug, t1_era, t2_era, t1_winner]])

		print("processing game {}...".format(i))



	df = pd.DataFrame(data=data[1:,1:],
	                  index=data[1:,0],
	                  columns=data[0,1:])
	# df2 = pd.DataFrame(data=data2[1:,1:],
	#                   index=data2[1:,0],
	#                   columns=data2[0,1:],
	#                   dtype=float)

	# print(df)
	# print(df2)

	# df['date']  = df['date']
	df['t1_batAvg'] = df['t1_batAvg'].astype(float)
	df['t2_batAvg'] = df['t2_batAvg'].astype(float)
	df['t1_OBP'] = df['t1_OBP'].astype(float)
	df['t2_OBP'] = df['t2_OBP'].astype(float)
	df['t1_OPS'] = df['t1_OPS'].astype(float)
	df['t2_OPS'] = df['t2_OPS'].astype(float)
	df['t1_slug'] = df['t1_slug'].astype(float)
	df['t2_slug'] = df['t2_slug'].astype(float)
	df['t1_ERA'] = df['t1_ERA'].astype(float)
	df['t2_ERA'] = df['t1_ERA'].astype(float)
	df['t1_winner?'] = df['t1_winner?'].astype(int)


	return df

# print(df.groupby('t1_winner?').mean())

# print(df.dtypes)

# plt.rc("font", size=14)

# sns.set(style="white")
# sns.set(style="whitegrid", color_codes=True)

# print(df['t1_winner?'].value_counts())
# sns.countplot(x='t1_winner?', data=df, palette='hls')
# plt.show()
# plt.savefig('count_plot')

if __name__ == '__main__':
	print(scrape(1))



