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

# replace Hamlet occurrences
hamlet = []
for i in df['p_PerfTitleClean']:
    if 'Hamlet' in i:
        hamlet.append(i)

hamlet_unique = set(hamlet)  # get unique values of set

for i in hamlet_unique:
    df['p_PerfTitleClean'] = df['p_PerfTitleClean'].replace(regex=i, value='Hamlet')

# filter by top 5 plays
df_unique = df.groupby('p_PerfTitleClean')['e_EventId'].nunique()

df_unique = df_unique.reset_index()
df_unique = df_unique.sort_values(by=['e_EventId'], ascending=False)
print(df_unique)
print(7 * '--------')

top_5 = df_unique['p_PerfTitleClean'][:5].to_list()
print('Top 5 plays:')
print(top_5)
print(7 * '--------')

df_unique.to_csv('unique_plays.csv', index=False)

# filter new df by plays to analyze and drop unnecessary columns
df = df.drop(['e_Season', 'e_Volume', 'e_Hathi', 'e_CommentC', 'e_Phase1', 'e_Phase2',
              'e_CommentCClean', 'e_BookPDF', 't_Volume', 'p_CommentP',
              'p_CastAsListed', 'p_DetailedComment', 'p_WorkId', 'p_CommentPClean'], axis=1)

df_clean = df[df['p_PerfTitleClean'].isin(top_5)]
df_clean.to_csv('top_5.csv', index=False)
