import requests
from bs4 import BeautifulSoup, Comment
import numpy as np
import pandas as pd

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

print(len(link_list))
print(link_list[0])


f = open("SanFran.txt", "w")

boxScore_url = "https://www.baseball-reference.com{}".format(link_list[0])


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

tSelect = int(input("Which table?\n"))

while tSelect != 0:
	
	statSelect = input("Which stat?\n")

	for t in tables[tSelect].find_all("tfoot"):
		try:
			print(t.find("td", {'data-stat' : statSelect}).getText())
		except AttributeError as e:
			print("Stat not found")

	tSelect = int(input("Which table?\n"))


# build np array

data = np.array([['game_id', 't1_batAvg', 't2_batAvg']])

data = np.vstack(data, [])