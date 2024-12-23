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


pd.set_option('display.width', 600)
pd.set_option('display.max_columns', 20)
mf = pd.read_csv('20241223_MFPFDetails.csv')
mf.drop('Unnamed: 15', inplace=True, axis=1)
mf.drop([14, 18], inplace=True)
# Profit / Loss in csv is not showing negative values, so made them correct sign
mf['Profit/ Loss %'] = mf['Profit/ Loss %'] * (mf['Profit/ Loss'] / abs(mf['Profit/ Loss']))

mf.info()
print('\n\nRemoving PSU funds..')
mf_PSU = mf[mf['Scheme'].str.contains('PSU')]
mf = mf[~mf['Scheme'].str.contains('PSU')]
print(f'Shape:{mf.shape}\n', mf)
cols = ['Scheme', 'Average Cost Price', 'Value At Cost', 'Last Recorded NAV *', 'Value at NAV', 'Realized Profit/Loss',
        'Profit/ Loss', 'Profit/ Loss %']
mf = mf[cols]
renamedCols = {'Average Cost Price': 'Avg Cost', 'Value At Cost': 'Latest_Value', 'Last Recorded NAV *': 'Latest_NAV',
               'Value at NAV': 'Original_Value', 'Realized Profit/Loss': 'Realized_Profit', 'Profit/ Loss': 'Profit',
               'Profit/ Loss %': "Profit %"}
mf.rename(columns=renamedCols, inplace=True)
print("\n\nBy Average cost..")
print(mf.sort_values(by='Avg Cost'))

print("\n\nBy Simple Profit..")
print(mf.sort_values(by='Profit', ascending=False))
mf['Profit Scale'] = mf['Profit %'] / mf['Avg Cost'] * 100
#mf_PSU['Profit Scale'] = mf_PSU['Profit/ Loss %'] / mf_PSU['Average Cost Price'] * 100

mf_navSorted = mf.sort_values(by='Latest_NAV')
mf_navSorted['NAV_Rating'] = range(1, mf.shape[0] + 1)
mf['NAV_Rating'] = mf_navSorted['NAV_Rating']

mf_profitScaleSorted = mf.sort_values(by='Profit Scale', ascending=False)
mf_profitScaleSorted['Profit_Scale_Rating'] = range(1, mf.shape[0] + 1)
mf['Profit_Scale_Rating'] = mf_profitScaleSorted['Profit_Scale_Rating']

mf_valueAtCostSorted = mf.sort_values(by='Latest_Value', ascending=False)
mf_valueAtCostSorted['Value_Rating'] = range(1, mf.shape[0] + 1)
mf['Value_Rating'] = mf_valueAtCostSorted['Value_Rating']

print("\n\nBy NAV..")
print(mf.sort_values(by='NAV_Rating'))
print("\n\nBy Profit Scale..")
print(mf.sort_values(by='Profit_Scale_Rating'))
print('\n\nBy Latest Value..')
print(mf.sort_values(by='Value_Rating'))
'''
print("\n\n---------\nPSU funds\n---------")
print(mf_PSU[cols].sort_values(by='Profit/ Loss %', ascending=False))
print("\n\nBy Profit Scale..")
print(mf_PSU[cols].sort_values(by='Profit Scale', ascending=False).head(7))
print('\n\nBy Value At Cost..')
print(mf_PSU[cols].sort_values(by='Value At Cost', ascending=False).head(7))
'''



print("\n\n")
# Average 0.04640340805053711 seconds on Lenovo as against 0. seconds on HP Pavilion
print("---Whole execution completed in %s seconds ---" % (time.time() - start_time))
