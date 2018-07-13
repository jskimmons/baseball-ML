from scraper2 import scrape

import pandas as pd

df = scrape(200)

df.to_csv('games.csv', sep=',')