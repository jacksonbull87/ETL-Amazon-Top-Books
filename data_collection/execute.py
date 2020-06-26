from top_books_scraper import get_top_books_data

import pandas as pd

df = get_top_books_data()

print(df)

df.to_csv('test')