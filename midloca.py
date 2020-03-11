#%%
import flask
import pandas as pd
from lookup_tables import outcome, settle, fatality, hiact, hostlev, ongo2010

# Import MIDA/MIDLOCA data
#
# SQL query:
# select m.dispnum3, stabb, ccode, x.*
# from midp as m
# inner join
# (select * from midloca
# inner join mida
# on midloca.dispnum = mida.dispnum3) as x
# on m.dispnum3 = x.dispnum3
# where m.ccode in 
# (select ccode from majors2016)
# order by year asc;

df = pd.read_json('Resources/midloca_majors.json')
df.head()

#%%
df.columns

#%%
df.drop(columns=['dipsnum3', 'midloc2_howobtained', 'midloc2_precision_comment',
       'midloc2_general_comment', 'priogrid_cell', 'midloc11_location',
       'midloc11_midlocmeasuringpoint', 'midloc11_latitude',
       'midloc11_longitude', 'midloc11_precision', 'link1', 'link2', 'link3'], inplace=True)
df.head()

#%%
df.columns
#%%
df.rename(columns={'midloc2_location':'location', 'midloc2_measuringpoint':'measuringpoint', 'midloc2_xlongitude':'xlongitude', 'midloc2_ylatitude':'ylatitude', 'midloc2_precision':'precision'}, inplace=True)
df.head()


#%%
df.columns

# %%
for row in df.groupby(['dispnum3']):
    print(row)

# %%
grouped = df.groupby(['dispnum3'])

# %%
for dispute, group in grouped:
    print(dispute, group)

# %%
grouped.head()

# %%
disputes = df['dispnum3'].unique()

# %%
print(df.loc[df['dispnum3'] == 3552])

# %%
