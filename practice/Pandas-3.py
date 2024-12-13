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


# rowCount = 2

df = pd.read_csv("mckinsey.csv", index_col=0)  # First column Country becomes index
prln(df)
df = pd.read_csv("mckinsey.csv")

print(df)
prln("No. of unique countries:\n", df['country'].nunique())
prln("countries count:\n", df['country'].value_counts())
prln("No. of unique years:\n", df['year'].nunique())
prln("years count:\n", df['year'].value_counts())

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
prln("Director id availability in director's id :\n", dirAvailable)
prln("All director ids are present in director:", np.all(dirAvailable))

moviesWithDirectors = movies.merge(directors, how='left', left_on='director_id', right_on='id')
prln(moviesWithDirectors)
moviesWithDirectors = movies.merge(directors, how='left', left_on='director_id', right_on='id', suffixes=('_mv', '_dr'))
prln(moviesWithDirectors)
prln(moviesWithDirectors.columns)

directorsWithMovies = directors.merge(movies, how='left', left_on='id', right_on='director_id')
prln(directorsWithMovies)
prln(directorsWithMovies.columns)

moviesWithDirectors.drop(['director_id', 'id_dr'], axis=1, inplace=True)
prln(moviesWithDirectors)

prln('----------------------------\n.apply() function\n----------------------------')


def encodeGender(x):
    if x == 'Male':
        return 'M'
    elif x == 'Female':
        return 'F'
    else:
        return 'O'


moviesWithDirectors['gender_encoded'] = moviesWithDirectors['gender'].apply(encodeGender)
prln("Added new column:'gender_encoded' (you can replace original column instead):\n", moviesWithDirectors)
''' 
moviesWithDirectors['gender'] = moviesWithDirectors['gender'].apply(encodeGender)
prln("Replaces column:'gender':\n", moviesWithDirectors)
'''
prln("NOTE:value_counts does not show NaN value counts, so be aware to use it directly..\n",
     moviesWithDirectors['gender'].value_counts())
prln(moviesWithDirectors['gender_encoded'].value_counts())

prln(moviesWithDirectors[['revenue', 'budget']])
prln("Applying function on multiple columns: (at this time, no use of this)\n",
     moviesWithDirectors[['revenue', 'budget']].apply(np.sum))
prln("Applying function on multiple columns: (axis=1 does operation between columns)\n",
     moviesWithDirectors[['revenue', 'budget']].apply(np.sum, axis=1))

prln(
    "When applying lambda in .apply(), consider x as row, so this is correct for axis=1 (to work across horizontal direction)\n"
    ": lambda x: x['revenue'] + x['budget']")
# moviesWithDirectors['profit'] = moviesWithDirectors[['revenue', 'budget']].apply(lambda x: x['revenue'] + x['budget'], axis=1)
moviesWithDirectors['profit'] = moviesWithDirectors.apply(lambda x: x['revenue'] + x['budget'], axis=1)
prln(moviesWithDirectors[['revenue', 'budget', 'profit']])

prln(moviesWithDirectors['director_name'] == 'James Cameron')
prln("Movies directed by James Cameron:\n", moviesWithDirectors[moviesWithDirectors.director_name == 'James Cameron'])
prln("Movies directed by James Cameron:\n",
     moviesWithDirectors[moviesWithDirectors['director_name'] == 'James Cameron'])
prln("---------GROUP BY---------")
prln("no meaning found:\n", moviesWithDirectors.groupby('director_name').head())
prln("No. of Groups:", moviesWithDirectors.groupby('director_name').ngroups)
prln("Actual Groups: {'group_name1':[ilocs of rows], 'group_name2':[ilocs of rows]}:\n",
     moviesWithDirectors.groupby('director_name').groups)
prln("Get individual group:\n", moviesWithDirectors.groupby('director_name').get_group('Adam McKay'))

prln(moviesWithDirectors.groupby('director_name').count())
prln(moviesWithDirectors.groupby('director_name')['title'].count())
prln("NOTE: Group By aggregate functions does not work on NaN columns... See examples:")
prln(moviesWithDirectors.groupby('director_name')[['gender', 'title']].count())
prln("Difference between gender count and title count:\n",
     moviesWithDirectors.groupby('director_name').get_group('Alexander Payne')[['gender', 'title']].count())
prln("Actual Gender and titles for 'Alexander Payne':\n",
     moviesWithDirectors.groupby('director_name').get_group('Alexander Payne')[['gender', 'title']])

prln("Applying multiple aggregate functions:\n",
     moviesWithDirectors.groupby('director_name')['year'].agg(['min', 'max']))
prln("Applying multiple aggregate functions, reset_index:\n",
     moviesWithDirectors.groupby('director_name')['year'].agg(['min', 'max']).reset_index())

print("Applying MULTIPLE aggregate functions on vote_average and year group on Director\n", moviesWithDirectors.groupby('director_name').agg({'vote_average': ['mean', 'min', 'max'], 'year': ['min', 'max']}))

prln("-------Group based filtering-------")
prln("High Budget Director: Director whose at least one movie has budget more than 1M.")
prln(moviesWithDirectors.groupby('director_name')['budget'].max())
prln(moviesWithDirectors.groupby('director_name')['budget'].max().reset_index())

data_director_budget = moviesWithDirectors.groupby('director_name')['budget'].max().reset_index()
print(data_director_budget.loc[data_director_budget['budget'] > 100000000])
names = data_director_budget.loc[data_director_budget['budget'] > 100000000]['director_name']
print("All Movies of high budget directors :\n",
      moviesWithDirectors.loc[moviesWithDirectors['director_name'].isin(names)])
# Alternatively
prln("Alternatively ...")
data_director_budget = moviesWithDirectors.groupby('director_name')['budget'].max()  #This is Series
prln(data_director_budget.loc[data_director_budget > 100000000])  #Using Series without any column name
names = data_director_budget.loc[data_director_budget > 100000000]
prln(names.index)
print("All Movies of high budget directors :\n",
      moviesWithDirectors.loc[moviesWithDirectors['director_name'].isin(names.index)])

prln("SOME GOOD, DIRECT WAY.... use filter() on groupby()")
# prln(moviesWithDirectors.filter()) # Here, Subset the dataframe rows or columns according to the specified index labels.  Note that this routine does not filter a dataframe on its contents. The filter is applied to the labels of the index.
prln("All Movies rows of high budget directors :\n",
     moviesWithDirectors.groupby('director_name').filter(lambda row: row['budget'].max() > 100000000))

prln("SOME GOOD use case of GROUP BY based apply()")
prln(
    "Problem statement: Filter risky movies, whose budget was even higher than the average revenue of the director from his other movies.\n")
print("Steps:")
print(" Find average revenue of director avgForGroup.")
print(" Find movies (.apply() on rows) revenue > avgForGroup")
print()
avgForGroup = moviesWithDirectors.groupby('director_name')['revenue'].mean()
print(avgForGroup)


def func(group):
    group['risky'] = group['budget'] > group['revenue'].mean()
    group['avg_revenue'] = group['revenue'].mean()
    return group


prln("output 1:\n", moviesWithDirectors.groupby('director_name').apply(func))
prln("output 2:\n", moviesWithDirectors.groupby('director_name').apply(func, include_groups=False))
prln("output 3:\n",
     moviesWithDirectors.groupby('director_name', group_keys=False).apply(func, include_groups=False))
data = moviesWithDirectors.groupby('director_name', group_keys=False).apply(func, include_groups=False)
prln("Final output: Filter risky movies, whose budget was even higher than the average revenue of the director from his other movies\n", data.loc[data['risky'] == True])



print()
# Average 1.021676778793335 seconds on Lenovo as against 0. seconds on HP Pavilion
print("---Whole execution completed in %s seconds ---" % (time.time() - start_time))
