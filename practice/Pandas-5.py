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


data = pd.read_csv("Pharma.csv")

prln(data.head())
prln(data.shape)

# Prints all info about data
data.info()

prln("\nMELT (wide format to long format)")
prln(data.columns)
prln("First 6 columns:\n", data.iloc[:10, :6])

prln("pd.melt() creates new columns 'variable' and 'value' where newly added column 'variable' is existing "
     "column name and column 'value' is it's value\n", pd.melt(data, id_vars=['Date', 'Drug_Name', 'Parameter']))

prln("data.shape:", data.shape, " VS melted data shape:",
     pd.melt(data, id_vars=['Date', 'Drug_Name', 'Parameter']).shape)

data_melt = pd.melt(data,
                    id_vars=['Date', 'Drug_Name', 'Parameter'],
                    var_name='time',
                    value_name='reading')

prln(data_melt.head())

prln("PIVOT (long to wide)")
data_tidy = data_melt.pivot(index=['Date', 'Drug_Name', 'Parameter'],
                            columns='time',
                            values='reading')
prln(data_tidy)
prln(data_tidy.index)
data_tidy.reset_index(inplace=True)
prln(data_tidy.index)
prln(data_tidy)

prln("Let's use this techniques..")
prln("data_melt:\n", data_melt.head())
prln("Data here is in this    format: Date | Drug | Parameter | time | reading"
     "\nWe want to see above data as  : Date | Time | Drug | Pressure | Temperature")

data_easy = data_melt.pivot(index=['Date', 'Drug_Name', 'time'],
                            columns='Parameter',
                            values='reading')

prln("data_easy:\n", data_easy)
data_easy.reset_index(inplace=True)
prln("data_easy:\n", data_easy)

prln("PIVOT and PIVOT TABLE")
prln('https://www.scaler.com/academy/mentee-dashboard/class/125590/session?joinSession=1')

prln(data_tidy.head(20))
print("Type of NaN is:", type(np.nan))
print("Solution for removing NaN is imputation- Filling the missing values. With-mean(), median(), mode(), 0, max")

prln("isna():\n", data.iloc[:, :7].isna().head())
prln("isnull(): same as isna()\n", data.isnull().head())

prln(data.isna().sum())  # axis=0, by default
prln(data.isna().sum(axis=1))  # axis=0, by default

prln("#1: drop rows with na values")
prln(
    f"data.dropna(): works by default on a row and drops ROWS if (any) value in a row is NaN:\n{data.isna().sum(axis=1)}\n",
    data.dropna())  # works on all rows with minimum 1 NaN
prln(f"data.dropna(axis=1): Drops a COLUMN if any row in that column is missing\n{data.isna().sum()}\n",
     data.dropna(axis=1))

prln("#2: Imputation (changing the contents)")
prln("data.fillna(-1):\n", data.fillna(-1))

prln(data['3:30:00'])
prln(data['3:30:00'].fillna(-1))
mean_val = data['3:30:00'].mean()
prln(data['3:30:00'].fillna(mean_val))

prln('But, above approach is too vague.. no group by is used. ')
prln(data_easy[['Drug_Name', 'Pressure']].head(22))
'''
prln("Data with pressure as nan:\n", data_easy[['Drug_Name', 'Pressure']][data_easy['Pressure'].isna()])
prln("Groupby.head(number) gives n number of rows of EACH group:\n", data_easy.groupby('Drug_Name').head(5))
prln(data_easy.groupby('Drug_Name', group_keys=False).head())
prln(data_easy.groupby('Drug_Name', group_keys=False)['Pressure'].apply(lambda x: x.fillna('dddddddd'), include_groups=False).head(17))
'''
data_easy['Pressure'] = data_easy.groupby('Drug_Name', group_keys=False)['Pressure'].apply(lambda x: x.fillna(x.mean()),
                                                                                           include_groups=False)
prln(data_easy[['Drug_Name', 'Pressure']].head(22))

prln("Miscellaneous functions")
prln('cut function')
temp_points = [5, 20, 35, 50, 60]
temp_labels = ['low', 'medium', 'high', 'very_high']
data_easy['temp_buckets'] = pd.cut(data_easy['Temperature'],
                                   bins=temp_points,
                                   labels=temp_labels
                                   )
prln(data_easy)
data_easy['temp_buckets'] = pd.cut(data_easy['Temperature'],
                                   bins=temp_points,
                                   labels=temp_labels,
                                   right=False
                                   )
prln("Look for datatype for buckets")
data_easy.info()

prln("Date functions")
data_easy['timestamp'] = data_easy['Date'] + ' '+ data_easy['time']
data_easy.info()
data_easy['timestamp'] = pd.to_datetime(data_easy['timestamp'], dayfirst=True)
data_easy.info()
prln("With pd.to_datetime(column), datatype of column becomes datetime64. Now you can do anything that you "
     "want to do with dates")
val = data_easy['timestamp'][0]
prln(val)
prln(val.year)
d = pd.to_datetime("2020-10-15 10:30:00", yearfirst=True)
prln(f"year={d.year} and minutes={d.minute} and day of week={d.dayofweek} and day_name={d.day_name()} and  tzname={d.tzname()} \ntimetuple={d.timetuple()}")


print()
# Average 0.31723543343 seconds on Lenovo as against 0.10731649398803711 seconds on HP Pavilion
print("---Whole execution completed in %s seconds ---" % (time.time() - start_time))
