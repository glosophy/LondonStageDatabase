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

