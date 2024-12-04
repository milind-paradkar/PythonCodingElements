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
# pd.read_excel()
# pd.read_json()
# pd.read_xml()
'''
CSV: pd.read_csv('file.csv') 
Excel: pd.read_excel('file.xlsx') 
JSON: pd.read_json('file.json') 
HTML: pd.read_html('file.html') 
SQL: pd.read_sql('SQL_query', connection) 
Parquet: pd.read_parquet('file.parquet') 
HDF5: pd.read_hdf('file.h5') 
Feather: pd.read_feather('file.feather') 
Stata: pd.read_stata('file.dta') 
SAS: pd.read_sas('file.sas7bdat') 
SPSS: pd.read_spss('file.sav')
'''
prln("df:\n", df)
prln("\ndf.size:", df.size)
prln("df.shape (a tuple):", df.shape)
prln("df.shape[0] (rows) * df.shape[1] (columns) :", df.shape[0], "*", df.shape[1], "= df.size:", df.size)
prln("\ntype(df):", type(df))
prln("Series: Single row or column")

prln("DF series type:", type(df['life_exp']))
prln("This results naturally as Series:\n", df['life_exp'])
lst = ['life_exp']
prln("This is df with only one column:\n", df[lst])
prln("df.column_name (not a good way to access column):\n", df.life_exp)
prln(df.head())  # Top 5 by default
prln(df.head(2))
prln(df.tail())  # Bottom 5 by default
prln(df.tail(10))
print("\ndf.info() will give you:")
df.info()
prln(type(df['life_exp'][0]), df['life_exp'][0])
prln(type(df['life_exp'][0:3]), df['life_exp'][0:3])
prln(df['life_exp'][10:20])

prln("df.columns: ", df.columns)
prln("df.keys():  ", df.keys())
prln("17] series.keys():  ", df['life_exp'].keys(), "--this has different meaning than df.keys()")
# prln(df['country', 'year']) # Gives error
prln(df[['country', 'year']])  # Passing list of columns to df
prln(df[['country', 'year']][2:4])  # Passing list of columns to df
prln("22:\n", df['country'].unique())
prln("24:\n", df['country'].nunique())
prln("25:\n", df['country'].values)
prln("26:\n", len(df['country'].values))
prln("value_counts:\n", df['country'].value_counts())
prln("value_counts for Zimbabwe:\n", df['country'].value_counts()['Zimbabwe'])
df.rename({'country': 'Country_changed'})  # Rename supports dict. {"key":"value"}
df_good_names = df.rename({'country': 'Country_changed'})  # Rename supports dict. "key":"value"
prln(df_good_names)
prln("It did not change column names .. Why?")
print('Numpy Axis: 0:col, 1:row')
print('but in Pandas, ')
print('Pandas Axis: 0: row, 1:column')
print("Let's use this concept..")
df_good_names = df.rename({1: 2222})
prln("Here row with id 1(starting from 0) is changed to 2222\n", df_good_names.head())
df_good_names = df.rename({'country': 'Country_changed'}, axis=1)  # Rename supports dict. "key":"value"
prln(df_good_names)
prln("33]", df.keys(), "\n", df_good_names.keys(), '\n', df_good_names)
df_good_names = df.rename({'country': 'Country_changed', "year": 'Year_changed'},
                          axis=1)  # Rename supports dict. "key":"value"
prln(df_good_names)
df.rename({'country': 'Country_changed', "continent": 'Continent_changed'}, axis=1, inplace=True)
prln(df)
prln(df.rename(columns={"year": "year_new", "life_exp": "life_expectancy"}, inplace=True))
df.rename({"gdp_cap": "gdp_capacity"}, axis="columns", inplace=True)
prln("Dropping row/column")
df_good_names.drop(0)  # Drops a ROW (you thought a column?)
prln(df_good_names.head(2))
#df_goodnames.drop('Country_changed') # Trying to drop a column, but not successful. -- KeyError: "['Country_changed'] not found in axis"
df_good_names_less_cols = df_good_names.drop('Country_changed', axis=1)  # Trying to drop a column, but not successful
df_good_names_less_cols = df_good_names.drop(['Country_changed', 'Year_changed'],
                                             axis=1)  # Trying to drop a column, but not successful
prln(df_good_names_less_cols)
prln(df_good_names['life_exp'] + 7)
df_good_names['life_exp+7'] = df_good_names['life_exp'] + 7
prln("Added column:\n", df_good_names)

x = [i for i in range(1704)]
df_good_names['new_column_from_list'] = x
# df_good_names['new_column_from_list_short'] = x[:1701]  # ValueError: Length of values (1701) does not match length of index (1704)
prln("New column created from list:\n", df_good_names.tail())
prln("***** ", df_good_names.head(2), "\n\n", df_good_names_less_cols.head(2))
df_good_names.drop('continent', axis=1, inplace=True)  # Trying to drop a column, in place
prln(df_good_names.head(2))

print('****** inplace is NOT used, so original remains same, but new df is created.')
df_good_names_less_col_list = df_good_names.drop(['Country_changed', 'Year_changed'],
                                                 axis=1)  # inplace is NOT used, so original remains same, but new df is created.
prln(df_good_names_less_col_list)
df_good_names_less_col_list = df_good_names.drop(['Country_changed', 'Year_changed'], axis=1,
                                                 inplace=True)  # inplace IS used, so original changed, but new df is not created --None.
print('inplace IS used, so original changed, but new df is NOT created --None.')
prln("df_good_names_less_col_list:", df_good_names_less_col_list,
     "  --> df_goodnames_less_col_list is None. So anything operated on this such as .head() will give you ERROR.")  # df_goodnames_less_col_list is None. So anything operated on this such as .head() will give you ERROR.

prln("df:\n", df)
df.rename({'year_new': "year"}, axis=1, inplace=True)
prln(df['year'] + 1000)
df['newColumn'] = df['year'] + 1000
prln(df)
df.rename({"newColumn": "thousand_years_later"}, inplace=True, axis=1)
prln(df)
prln(df.columns)
prln(df.drop(df.columns[-1],
             axis=1))  # Last column index -1 dropped and new df can be captured (inplace=False by default
prln(df.drop(df.columns[[2, 4]],
             axis=1))  # Giving multiple columns by multiple index is tricky, you cannot use columns[2,3] as it is syntax for 2d array

print("\n\n"
      "--------------------------------------------------\n"
      "C o n c e p t s      o f   L O C   and   I L O C\n--------------------------------------------------\n\n")
prln("\nW O R K I N G     W I T H      R O W S ....\n")
prln(df.index)
df_with_new_index = df.copy()  # Deep copy by default. We mean data will not affect each other. A separate copy. See documentation
df_with_new_index.index = range(10, len(df) * 10 + 10, 10)
prln(df)  # default indexes
prln(df_with_new_index)  # default indexes are now changed to multiples of 10. just for fun.
prln("Now new index is: ", df_with_new_index.index)
prln("First 10 records:df:\n", df[:10])
prln("First 10 records:df_with_new_index (uses first 10 elements, ignores explicit index 10, 20, 30 like this):\n",
     df_with_new_index[:10])
prln(
    f"[61]: Index (explicit or given) of df_with_new_index[2] (2 is implicit index):{df_with_new_index.index[2]} and df_with_new_index[3] (3 is implicit index):{df_with_new_index.index[3]}")
prln(
    "Using explicit index: Index visible on screen: df_with_new_index['gdp_capacity'][10] (uses explicit index numbers 10, 20 -->",
    df_with_new_index['gdp_capacity'][10], " and ",
    df_with_new_index['gdp_capacity'][20])
prln("General syntax: df.index[implicit] and df[explicit] gets accounted")
sample = df.head()
prln("sample DF:\n", sample)
sample.index = ['a', 'b', 'c', 'd', 'e']
prln("[65] sample DF:\n", sample)
print(
    f"sample.index[0]:{sample.index[0]} and sample.year['a']:{sample.year['a']} or sample['year']['a']:{sample['year']['a']} "
    f"\nor\nsample['year'][0] (expecting 0 as implicit index):{sample['year'][0]} <-- Gives this warning:"
    f"FutureWarning: Series.__getitem__ treating keys as positions \n"
    f"is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame "
    f"behavior). To access a value by position, use `ser.iloc[pos]`")

# prln(df_with_new_index['gdp_capacity'][2]) ValueError: 2 is not in range.

prln("Using implicit index: Index which is not visible on screen: df_with_new_index['gdp_cap'].index[0] --> "
     "GIVES YOU EXPLICIT INDEX for IMPLICIT INDEX given [0] and [1]-->", df_with_new_index.index[0], " and ",
     df_with_new_index.index[1])

prln("df.head(15):\n", df.head(15))
prln("df.loc uses explicit index and all numbers are inclusive.")
prln("-- df.loc[row,col] ----- col is optional")
prln("df.loc[3:10] :\n", df.loc[3:10])
prln("df_with_new_index.loc[3:100](in slicing, errors such as non-existing index 3 is ignored) "
     "(this works because slicing is used and only matching indexed items are shown):\n", df_with_new_index.loc[3:100])
# prln("df_with_new_index.loc[3:100] (this works because slicing is used and only matching indexed items are shown):\n", df_with_new_index.loc[[3,100]]) # KeyError: '[3] not in index'
prln("df_with_new_index.loc[[10,100] (this gives only 2 items because only matching indexed items are shown):\n",
     df_with_new_index.loc[[10, 100]])

prln("df.loc[len(df) - 1::-3]:", df.loc[len(df) - 1::-3])
prln("df.loc[[1, 4, 5,7]]:", df.loc[[1, 4, 5,
                                     7]])  # Cannot simply use [,] syntax just to send rows.. it would be treated as [row, col], that's why [[rows series]]
prln("df.loc[1:7, :]:\n", df.loc[1:7, :])
prln("df.loc[10:15, :]:\n", df.loc[10:15, :])

prln("df.columns:\n", df.columns)
prln("df.loc[10:15, 'year':'gdp_capacity']\n", df.loc[10:15, 'year':"gdp_capacity"])

# prln(df.loc[10:15, 1:3]) # second item in tuple not supported for numbering directly. axis 1 has names, so need to
# give names only, not numbering
prln(df.loc[10:15, ['year', 'population']])

# Similar to np.array([2,3,4])
s = pd.Series([76, 5, 3, 7, 8, 9])
s = pd.Series([76, 5, 3, 7, 8, 9], name='Random_Series')
prln("series:s: (implicit and explicit indexes are same)\n", s)
s.index = ['a', 'b', 'c', 'd', 'e', 'f']
prln("Series:s ->\n", s)

prln(s.loc['b':'e'])  # As this is Series, it has only row index (no column index)
prln("this does not work:['e':'b']", s.loc['e':'b'])
prln(s.loc[['c', 'a']])

# Average 0.9480547904968262 seconds on Lenovo as against 0.14931440353393555 seconds on HP Pavillion
print("---Whole execution completed in %s seconds ---" % (time.time() - start_time))
