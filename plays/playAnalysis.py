import pandas as pd

beggars = pd.read_csv('Beggars.csv')
print(len(beggars['e_EventId'].unique()))