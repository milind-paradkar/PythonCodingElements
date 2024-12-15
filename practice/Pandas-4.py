import pandas as pd
import numpy as np
import time

start_time = time.time()

ctr = 1


def prln(*kwargs):
    global ctr
    print(f"[{ctr}]:\n", *kwargs, "\n", sep='')
    ctr = ctr + 1


def e():
    exit()


movies = pd.read_csv("movies.csv")
prln(movies)
movies = pd.read_csv("movies.csv", index_col=0)
prln(movies)
prln(movies.columns)

directors = pd.read_csv('directors.csv', index_col=0)
prln("Directors:\n", directors)

prln('Total movies:', movies.shape[0], " Unique directors:", movies['director_id'].nunique())
prln('Total Directors:', directors.shape[0], " Unique Directors:", directors['id'].nunique())

dirAvailable = movies['director_id'].isin(directors['id'])
prln("Director id availability in director's id: isin() :\n", dirAvailable)
prln("All director ids are present in director:", np.all(dirAvailable))

moviesWithDirectors = movies.merge(directors, how='left', left_on='director_id', right_on='id', suffixes=('_mv', '_dr'))
moviesWithDirectors.drop('id_dr', axis='columns', inplace=True)
prln(moviesWithDirectors)
prln(moviesWithDirectors.columns)

prln("[WAY 1] Using agg() or aggregate() over multiple columns with simple LIST syntax")
prln(moviesWithDirectors.groupby('director_id')[['title', 'year']].agg(['min', 'max']))
prln(moviesWithDirectors.groupby('director_id')[['title', 'year']].agg(['min', 'max']).columns)

prln(moviesWithDirectors.groupby('director_name')['title'].agg('count').sort_values(ascending=False))
prln("[WAY 2] Using agg() or aggregate() over multiple columns with good DICTIONARY syntax")
data_agg = moviesWithDirectors.groupby('director_name').agg({'title': ['count'], 'year': ['min', 'max']})
prln("NEW: sort_values(by=('title', 'count') because agg with title and 'count' creates multi-index at axis=1")
print(moviesWithDirectors.groupby('director_name')
      .agg({'title': ['count'], 'year': ['min', 'max']})
      .sort_values(by=('title', 'count'), ascending=False))

prln("Columns for multiple aggregate functions:\n", data_agg.columns)
prln("data_agg is multi-index at column level, so getting year:\n", data_agg.year)
prln(
    "data_agg is multi-index at column level, so getting title (gives 'count' as column along with 'director_name' as index:\n",
    data_agg.title)
prln(data_agg.title.loc['Alex Proyas'])
prln("Directly resetting index on multi-index data:\n", data_agg.reset_index(col_level=0, col_fill='_'))

new_columns = ['_'.join(col) for col in data_agg.columns]
prln("new column_names we want to create:", new_columns)
data_agg.columns = new_columns
prln("new_columns assigned to columns:\n", data_agg)
data_agg.reset_index(inplace=True)
prln("Reset index always adds index data as new column (director_name here) and index is unnamed int series:\n",
     data_agg)

prln("[WAY 3] Using agg() or aggregate() over multiple columns with better tuple syntax, I guess uses *kwargs")
prln(moviesWithDirectors.groupby('director_name')[['title', 'year']].agg(movie_count=("title", "count"),
                                                                         first_year=('year', 'min'),
                                                                         last_year=('year', 'max')))
print(
    "Above creates single index columns instead of multi-index columns created in DICT syntax with columns\nColumns created by *kwargs tuple syntax:",
    moviesWithDirectors.groupby('director_name')[['title', 'year']].agg(movie_count=("title", "count"),
                                                                        first_year=('year', 'min'),
                                                                        last_year=('year', 'max')).columns,
    "\nVs\nMultiIndex([('title', 'count'),\n"
    "\t\t( 'year',   'min'),\n"
    "\t\t( 'year',   'max')],\n"
    "\t)")

# data_agg['active_years'] = data_agg.apply(lambda x: x['year_min'] + x['year_max'])
data_agg['active_years'] = data_agg.year_max - data_agg.year_min + 1  # 2020 2020 should come as 1 year both years inclusive
print(data_agg.sort_values(by='active_years', ascending=False))

data_agg['movies_per_yr'] = data_agg['title_count'] / data_agg['active_years']
prln(data_agg.sort_values(by='movies_per_yr', ascending=False))
prln("Top 5 most productive directors\n", data_agg.sort_values(by='movies_per_yr', ascending=False).iloc[:4])

print()
# Average 0.49590563774108887 seconds on Lenovo as against 0. seconds on HP Pavilion
print("---Whole execution completed in %s seconds ---" % (time.time() - start_time))
