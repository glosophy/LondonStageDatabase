import pandas as pd

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

# separate list of comma-separate performers into elements of list
df['c_Performer'] = [i.split(',') for i in df['c_Performer']]

# # deconstruct list so occurrences are accurate
df = df.explode('c_Performer')
performers_clean = df['c_Performer'].value_counts()
print(performers_clean)
print(7 * '--------')

