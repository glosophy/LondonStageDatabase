import pandas as pd
import datetime
import numpy as np

# read csv
df = pd.read_csv('LondonStageFull.csv', on_bad_lines='skip')  # get rid of tokenizing data error

# see columns
print(df.columns)
print(7 * '--------')

# print head
print(df.head)
print(7 * '--------')

# see shape
print('df shape:', df.shape)
print(7 * '--------')

# number of unique values for each column
print('Unique values for each column:')
print(df.nunique(axis=0))
print(7 * '--------')

# check for missing values
print('Missing values:')
print(df.isnull().sum())
print(7 * '--------')

# count number of occurrences for performers: many performers are included in a list.
performers = df['c_Performer'].value_counts()
print(performers)
print(7 * '--------')

# keep rows where 'c_Performer' is not NaN
df = df[df['c_Performer'].notna()]
print('Length after dropping NaN:', len(df['c_Performer']))
print(7 * '--------')

# separate list of comma-separate performers into elements of list
df['c_Performer'] = [i.split(',') for i in df['c_Performer']]

# # deconstruct list so occurrences are accurate
df = df.explode('c_Performer')
performers_clean = df['c_Performer'].value_counts()
performers_clean_names = df['c_Performer'].value_counts().index.tolist()
print(performers_clean)
print('Length with explode:', len(df['c_Performer']))
print(7 * '--------')

# type of performance
p_type = df['p_PType'].value_counts()
print(p_type)
print(7 * '--------')

# handle dates
df['e_EventDate'] = df['e_EventDate'].astype(str)
df = df[df['e_EventDate'].notna()]

year_df = []
month_df = []
day_df = []
for i in df['e_EventDate']:
    splitat = 4
    year, rest = i[:splitat], i[splitat:]
    month, day = rest[:splitat - 2], rest[splitat - 2:]

    year_df.append(year)
    month_df.append(month)
    day_df.append(day)

# turn list elements into integers
year_df, month_df, day_df = [int(x) for x in year_df], [int(x) for x in month_df], [int(x) for x in day_df]

# add years to df
df['e_Year'] = year_df

# filter by top 10 plays
play_clean = df['p_PerfTitleClean'].value_counts()
play_clean_names = df['p_PerfTitleClean'].value_counts().index.tolist()
play_clean_names_top10 = play_clean_names[:10]
print(play_clean)
print(7 * '--------')
print('Top 10 plays:')
print(play_clean_names_top10)
print(7 * '--------')

# filter by the top 10 plays: keep rows based on conditions
top10_df = df[df['p_PerfTitleClean'].isin(play_clean_names_top10)]
top10 = df[df['c_Performer'].isin(performers_clean_names[:10])]
print(top10)

# top10.to_csv('top10.csv', index=False)