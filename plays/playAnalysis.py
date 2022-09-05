import pandas as pd

top = pd.read_csv('/Users/guillermina/Pycharm/LondonStageDatabase/top_5.csv')

# filter by plays
plays = top['p_PerfTitleClean'].unique()
print(plays, '\n', 7*'---------')

# get individual dataframes for each play
hamlet = top[top['p_PerfTitleClean'] == plays[0]]
macbeth = top[top['p_PerfTitleClean'] == plays[1]]
stratagem = top[top['p_PerfTitleClean'] == plays[2]]
beggars = top[top['p_PerfTitleClean'] == plays[3]]
devil = top[top['p_PerfTitleClean'] == plays[4]]

dfs = [hamlet, macbeth, stratagem, beggars, devil]

# get timeline for number of plays over time
for i in range(len(dfs)):
    time = dfs[i].groupby('e_Year')['e_EventId'].nunique()
    time = time.reset_index()
    time.to_csv('{}_overTime.csv'.format(str(plays[i]).replace(' ', '')), index=False)


# get performers count for alluvial diagram
# filter by top 5 plays
top_performer = top.groupby('p_PerfTitleClean')['e_EventId'].nunique()

df_unique = df_unique.reset_index()
df_unique = df_unique.sort_values(by=['e_EventId'], ascending=False)
print(df_unique)
print(7 * '--------')

top_5 = df_unique['p_PerfTitleClean'][:5].to_list()
print('Top 5 plays:')
print(top_5)
print(7 * '--------')