"""55 | P a g e
Day 46: Create a DataFrame
Create a Dataframe using pandas. You are going to create a
code to put the following into a Dataframe. You will use the
information in the table below. Basically, you are going to
recreate this table using pandas. Use the information in the table
to recreate the table.
year Title genre
2009 Brothers Drama
2002 Spider-Man Sci-fi
2009 WatchMen Drama
2010 Inception Sci-fi
2009 Avatar Fantasy
Extra Challenge: Website Data with Pandas
Create a code that extracts data from a website. You will extract a
table from the website. And from that table you will extract columns
about the data types in Python and their mutability. You will extract
information from the following website:
https://en.wikipedia.org/wiki/Python_(programming_language)"""

import pandas as pd

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

tables = pd.read_html(url)

df = tables[1].iloc[:, :2]

print(df)