import pandas as pd

ctr = 1


def prln(*kwargs):
    global ctr
    print(f"[{ctr}]:\n", *kwargs, "\n", sep='')
    ctr = ctr + 1


# rowCount = 2

df = pd.read_csv("mckinsey.csv")
prln("df:\n", df)
prln("\ndf.size:", df.size)
prln("df.shape (a tuple):", df.shape)
prln("df.shape[0] (rows) * df.shape[1] (columns) :", df.shape[0] * df.shape[1], "= df.size:", df.size)
prln("\ntype(df):", type(df))
prln("Series: Single row or column")

prln("DF series:", type(df['life_exp']))
prln(df['life_exp'], "\n")

prln(df.head())  # Top 5 by default
prln(df.head(2))
prln(df.tail())  # Bottom 5 by default
prln(df.tail(10))
df.info()
prln(type(df['life_exp'][0]), df['life_exp'][0])
prln(type(df['life_exp'][0:3]), df['life_exp'][0:3])
prln(df['life_exp'][10:20])

prln(df.columns)
prln(df.keys())
prln(df['life_exp'].keys(), "--this has different meaning than df.keys()")
# prln(df['country', 'year']) # Gives error
prln(df[['country', 'year']])  # Passing list of columns to df
prln(df[['country', 'year']][2:4])  # Passing list of columns to df
prln(df['country'].unique())
prln(df['country'].nunique())
prln(df['country'].values)
prln(df['country'].value_counts())
df.rename({'country': 'Country_changed'})  # Rename supports dict. "key":"value"
df_goodnames = df.rename({'country': 'Country_changed'})  # Rename supports dict. "key":"value"
prln(df_goodnames)
prln("It did not change column names .. Why?")
print('Numpy Axis: 0:col, 1:row')
print('but in Pandas, ')
print('Pandas Axis: 0: row, 1:column')
print("Let's use this concept..")
df_goodnames = df.rename({0: 2222})
prln(df_goodnames)
df_goodnames = df.rename({'country': 'Country_changed'}, axis=1)  # Rename supports dict. "key":"value"
prln(df.keys(), df_goodnames.keys(), df_goodnames)
df_goodnames = df.rename({'country': 'Country_changed', "year": 'Year_changed'},
                         axis=1)  # Rename supports dict. "key":"value"
prln(df_goodnames)
df.rename({'country': 'Country_changed', "continent": 'Continent_changed'}, axis=1, inplace=True)
prln(df)
prln("Dropping row/column")
df_goodnames.drop(0)  # Drops a ROW (you thought a column?)
prln(df_goodnames.head(2))
#df_goodnames.drop('Country_changed') # Trying to drop a column, but not successful. -- KeyError: "['Country_changed'] not found in axis"
df_goodnames_less_cols = df_goodnames.drop('Country_changed', axis=1)  # Trying to drop a column, but not successful
prln("***** ", df_goodnames.head(2), "\n\n", df_goodnames_less_cols.head(2))
df_goodnames.drop('continent', axis=1, inplace=True)  # Trying to drop a column, in place
prln(df_goodnames.head(2))

print('****** inplace is NOT used, so original remains same, but new df is created.')
df_goodnames_less_col_list = df_goodnames.drop(['Country_changed', 'Year_changed'],
                                               axis=1)  # inplace is NOT used, so original remains same, but new df is created.
prln(df_goodnames_less_col_list)
df_goodnames_less_col_list = df_goodnames.drop(['Country_changed', 'Year_changed'], axis=1,
                                               inplace=True)  # inplace IS used, so original changed, but new df is not created --None.
print('inplace IS used, so original changed, but new df is NOT created --None.')
prln(df_goodnames_less_col_list,
     "  --> df_goodnames_less_col_list is None. So anything operated on this such as .head() will give you ERROR.")  # df_goodnames_less_col_list is None. So anything operated on this such as .head() will give you ERROR.

prln("df:\n", df)
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
      "--------------------------------------------\n"
      "C o n c e p t s      o f   L O C   and   I L O C\n------------------------------------------\n\n")
prln("\nW O R K I N G     W I T H      R O W S ....\n")
prln(df.index)
df_with_new_index = df.copy()  # Deep copy by default. We mean data will not affect each other. A separate copy. See documentation
df_with_new_index.index = range(10, len(df) * 10 + 10, 10)
prln(df)  # default indexes
prln(df_with_new_index)  # default indexes are now changed to multiples of 10. just for fun.
prln("Now new index is: ", df_with_new_index.index)
prln("Using explicit index: Index visible on screen: df_with_new_index['gdp_cap'][10] -->",
     df_with_new_index['gdp_cap'][10])
prln("Using implicit index: Index which is not visible on screen: df_with_new_index['gdp_cap'].index[0] --> "
     "GIVES YOU EXPLICIT INDEX for IMPLICIT INDEX given [0] and [1]-->", df_with_new_index.index[0], " and ",
     df_with_new_index.index[1])

prln("df.head(15):\n", df.head(15))
prln("df.loc uses explicit index and all numbers are inclusive.")
prln("-- df.loc[row,col] ----- col is optional")
prln("df.loc[3:10]:\n", df.loc[3:10])
prln(df.loc[len(df)-1::-3])
prln(df.loc[[1,4,5,7]]) # Cannot simply use [,] syntax just to send rows.. it would be treated as [row, col], that's why [[rows series]]
prln(df.loc[1:7, :])
prln(df.loc[10:15, :])
prln(df.columns)
prln(df.loc[10:15, 'year':"gdp_cap"])
# prln(df.loc[10:15, 1:3]) # second item in tuple not supported for numbering directly. axis 1 has names, so need to
# give names only, not numbering
prln(df.loc[10:15, ['year', 'population']])

# Similar to np.array([2,3,4])
s = pd.Series([76, 5, 3, 7, 8, 9])
s = pd.Series([76, 5, 3, 7, 8, 9], name='Random_Series')
prln("series:s: (implicit and explicit indexes are same)\n", s)
s.index = ['a','b','c','d','e','f']
prln("Series:s ->\n",s)
prln(s.loc['b':'e']) # As this is Series, it has only row index (no column index)
prln("this does not work:['e':'b']", s.loc['e':'b'])
prln(s.loc[['c', 'a']])







