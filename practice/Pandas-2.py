import pandas as pd
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

df = pd.read_csv("mckinsey.csv")

prln(df)

prln("WAY 1:")
new_row = {"country": "India", "year": 2024, "population": 1223322, 'continent': "Asia", "life_exp": 89,
           "gdp_cap": 767677}
row0 = pd.DataFrame([new_row])
prln(f"new_row:\n{new_row}\n\nrow0:\n", row0)

df1 = pd.concat([df, row0])
df1 = pd.concat([df1, row0])
prln("When concatenating, index is not correctly added.", df1.tail())

df1 = pd.concat([df1, row0], ignore_index=True)
prln("When concatenating, now index is correctly added due to ignore_index=true flag\n", df1.tail())

prln("WAY 2:")
# df1.loc[len(df1.index)] = row0   # raise ValueError("cannot set a row with mismatched columns")
df1.loc[len(df1.index)] = ['India', 2015, 1234567, 'Asia', 60, 7654321]
print("->:\n", df1.tail())

# df1.loc[len(df1.index)] = ['India', 2015, 1234567, 'Asia', 60]  # ValueError: cannot set a row with mismatched columns

prln(
    "loc can be used to update as well as insert single row. BUT, iloc can be used to update any row and cannot be used to insert a row")
# df1.iloc[len(df1.index)] = ['India', 2015, 1234567, 'Asia', 60, 7654321] # IndexError: iloc cannot enlarge its target object

prln("df.drop uses explicit index. Redoing drop will give you keyerror")
print(df.drop(2, axis=0))  # explicit index
print(df.drop("continent", axis=1))

prln("df.index[implicit_index] gives you explicit index")

prln(df.drop([2, 3, 5], axis=0).head())

df1 = df.head()
df1.index = [1, 2, 2, 3, 2]
prln(df1)
print("df1.drop(2) will remove all matching rows because drop(explicit_index):\n\n", df1.drop(2))
# print(df1.drop([2,3,5], axis=0).reset_index()) # KeyError: '[2 3 5] not found in axis'

prln(
    "df.reset_index() -always reset an index and also bring back removed column (if used set_index(column1) then column1) or ORIGINAL index back as a column")
print(df.reset_index().head())
print(df.reset_index(drop=True).head())
# print(df.reset_index(drop=True, inplace=True).head())

prln("df.duplicated() checks if row is duplicate (considering all columns, by default)\n", df.duplicated())
prln(
    "df.duplicated('country') checks if row is duplicate (by country), but gives False for first occurrence and True for next occurrence\n",
    df.duplicated("country").head(20))
prln(
    "So using .duplicated() with Trues and Falses, we can see multiple LINES/ ROWS using loc:df.loc[df.duplicated('country')]: --> Shows all duplicate rows (missing loc=0 and 12 because it is first unique country) \n",
    df.loc[df.duplicated("country")].head(20))
# print(df.loc[not df.duplicated("country")].head(20)) # Not possible
prln(df.drop_duplicates('country'))
prln(df.drop_duplicates('country').reset_index())
prln(df.drop_duplicates('country').reset_index(drop=True))
prln(df.drop_duplicates('country'))
prln(df.drop_duplicates('country', keep='last'))
prln(df.drop_duplicates('country', keep=False))  # - ``False`` : Drop all duplicates.

prln('df.duplicated("country", "year") checks if row is duplicate (considering "country", "year")\n',
     df.duplicated(["country", "year"]))

prln("iloc works with column numbers also:\n", df.iloc[0:3, 1:3])
# prln("loc does not work with column numbers:\n", df.loc[0:3, 1:3])

le = df['life_exp']
prln(le)
prln("sum():", le.sum())
prln("mean():", le.mean())
prln("min():", le.min())
prln("count():", le.count())

prln(df.sort_values(['life_exp'], ascending=False))
prln(df.sort_values(['country', 'life_exp'], ascending=False))
prln(df.sort_values(['country', 'life_exp'], ascending=[True, False]))

users = pd.DataFrame({"userId": [1, 2, 3, 4, 5], "name": ["Milind", "Mohan", "Manasi", "Malu", "Mayuri"]})
msgs = pd.DataFrame({"userId": [1, 3, 2, 1, 1, 10], "msgs": ["Hm", 'Ha', 'Achcha', "Oh!", "Ok.", "No, let's do it"]})
chat = pd.concat([users, msgs])
prln("Chat:\n", chat)
chat = pd.concat([users, msgs], ignore_index=True)
prln("Chat:\n", chat)

chat = pd.concat([users, msgs], axis=1)
prln("Chat:\n", chat)

chat = pd.concat([users, msgs], axis=1, ignore_index=True)
prln("Chat:\n", chat)

prln("Instead of using pd.concat(), let's use df.merge()")
chat = users.merge(msgs, on='userId')
prln("Merge uses only matching rows (FULL INNER JOIN) by default, Mayuri is missing:\n", chat)

chat = users.merge(msgs, on='userId', how='outer')
prln("FULL OUTER JOIN using how='outer':\n", chat)

chat = users.merge(msgs, on='userId', how='left')
prln("LEFT OUTER JOIN using how='left':\n", chat)

chat = users.merge(msgs, on='userId', how='right')
prln("RIGHT OUTER JOIN using how='right':\n", chat)

users.rename(columns={"userId": "id"}, inplace=True)
prln(users)

chat = users.merge(msgs, left_on='id', right_on='userId')
prln("Matching 2 random column names, but showing both columns:\n", chat)

df1 = pd.DataFrame({'A': [10, 30], 'B': [20, 40], 'C': [30, 60]})
df2 = pd.DataFrame({'A': [10, 30], 'C': [30, 50]})
prln("What would be the shape of the output dataframe? for- df2.merge(df1, on = 'A', how = 'outer')")
print(df1)
print("and\n", df2)
merged = df2.merge(df1, on='A', how='outer')
print('\nOutput:\n', merged)
merged = df2.merge(df1, on='A', how='outer', suffixes=('_left', '_right'))
print('\nOutput:\n', merged)

print()
# Average 0.6331555843353271 seconds on Lenovo as against 0. seconds on HP Pavilion
print("---Whole execution completed in %s seconds ---" % (time.time() - start_time))
