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

print()
# Average 0. seconds on Lenovo as against 0. seconds on HP Pavilion
print("---Whole execution completed in %s seconds ---" % (time.time() - start_time))
