import requests
from bs4 import BeautifulSoup, Comment
import numpy as np
import pandas as pd
import re


def todayGames():

    year = 2018
    
    url = "https://www.baseball-reference.com/leagues/MLB/{}-schedule.shtml".format(year)

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # get list of links to populate datasheet with

    link_list = []

    today_div = soup.find("span", {"id": "today"}).parent.parent

    today_soup = BeautifulSoup(str(today_div), "html.parser")

    for em in today_soup.find_all("em"):
	    for a in em.find_all("a"):
		    link_list.append(a.get("href"))

    cols = ['game_id', 't1_name', 't2_name', 't1_batAvg', 't2_batAvg', 't1_OBP', 't2_OBP', 't1_OPS', 't2_OPS', 't1_slug', 't2_slug', 't1_ERA', 't2_ERA']

    data = np.array([cols])

    i = 1

    for link in link_list:

        boxScore_url = "https://www.baseball-reference.com{}".format(link)

        page = requests.get(boxScore_url).text

        soup = BeautifulSoup(page, "lxml")

        total_headers = soup.find_all("strong", text='TOTAL')

        tables = []

        # table order: t1_batters, t2_pitcher, t2_batters, t1_pitchers

        for header in total_headers:
            tables.append(header.parent.parent)

        # get statatatatattatatats

        team_list = soup.find_all("h2", text=re.compile("Last 10 Games"))

        t1_name = team_list[0].getText()[0:4]
        t2_name = team_list[1].getText()[0:4]

	    # batting
		
        td_list = tables[0].find_all("td")
        t1_batAvg = td_list[3].getText()
        t1_OBP = td_list[4].getText()
        t1_slug = td_list[5].getText()
        t1_OPS = td_list[6].getText()

        td_list = tables[2].find_all("td")
        t2_batAvg = td_list[3].getText()
        t2_OBP = td_list[4].getText()
        t2_slug = td_list[5].getText()
        t2_OPS = td_list[6].getText()


    	# pitching

        td_list = tables[3].find_all("td")
        t1_era = td_list[4].getText()

        td_list = tables[1].find_all("td")
        t2_era = td_list[4].getText()


		# build np array

        data = np.vstack([data, [i, t1_name, t2_name, t1_batAvg, t2_batAvg, t1_OBP, t2_OBP, t1_OPS, t2_OPS, t1_slug, t2_slug, t1_era, t2_era]])

        # print("processing game {}...".format(i))

        i+=1



    df = pd.DataFrame(data=data[1:,1:],
                    index=data[1:,0],
                    columns=data[0,1:])

    df['t1_batAvg'] = df['t1_batAvg'].astype(float)
    df['t2_batAvg'] = df['t2_batAvg'].astype(float)
    df['t1_OBP'] = df['t1_OBP'].astype(float)
    df['t2_OBP'] = df['t2_OBP'].astype(float)
    df['t1_OPS'] = df['t1_OPS'].astype(float)
    df['t2_OPS'] = df['t2_OPS'].astype(float)
    df['t1_slug'] = df['t1_slug'].astype(float)
    df['t2_slug'] = df['t2_slug'].astype(float)
    df['t1_ERA'] = df['t1_ERA'].astype(float)
    df['t2_ERA'] = df['t2_ERA'].astype(float)


    return df

if __name__ == '__main__':
	print(todayGames())



