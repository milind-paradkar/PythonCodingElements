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

prln(data.isna().sum()) # axis=0, by default
prln(data.isna().sum(axis=1))  # axis=0, by default

prln("#1: drop rows with na values")
prln(f"data.dropna(): works by default on a row and drops ROWS if (any) value in a row is NaN:\n{data.isna().sum(axis=1)}\n", data.dropna())  # works on all rows with minimum 1 NaN
prln(f"data.dropna(axis=1): Drops a COLUMN if any row in that column is missing\n{data.isna().sum()}\n", data.dropna(axis=1))

prln("#2: Imputation (changing the contents)")
prln("data.fillna(-1):\n", data.fillna(-1))

prln(data['3:30:00'])
prln(data['3:30:00'].fillna(-1))
mean_val = data['3:30:00'].mean()
prln(data['3:30:00'].fillna(mean_val))

prln('But, above approach is too vague.. no group by is used. ')
prln(data_easy['Pressure'][data_easy['Pressure'].isna()])
prln(data_easy.groupby('Drug_Name')['Pressure'].head())
prln(data_easy.groupby('Drug_Name', group_keys=False)['Pressure'].apply(lambda x: x.fillna(x.mean()), include_groups=False).head(15))
prln(data_easy.groupby('Drug_Name', group_keys=False)['Pressure'].apply(lambda x: x.fillna(-11), include_groups=False).head(15))
data_easy['Pressure'] = data_easy.groupby('Drug_Name', group_keys=False)['Pressure'].apply(lambda x: x.fillna(-11), include_groups=False).head(15)
prln(data_easy['Pressure'].head(15))


print()
# Average 0. seconds on Lenovo as against 0.08533406257629395 seconds on HP Pavilion
print("---Whole execution completed in %s seconds ---" % (time.time() - start_time))
