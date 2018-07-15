from scraper2 import scrape

import pandas as pd

df = scrape(1000)

df.to_csv('games.csv', sep=',')