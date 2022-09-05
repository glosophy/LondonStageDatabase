import pandas as pd

top = pd.read_csv('/Users/guillermina/Pycharm/LondonStageDatabase/top_5.csv')

# filter by plays
plays = top['p_PerfTitleClean'].unique()
print(plays, '\n', 7 * '---------')

# get individual dataframes for each play
hamlet = top[top['p_PerfTitleClean'] == plays[0]]
macbeth = top[top['p_PerfTitleClean'] == plays[1]]
stratagem = top[top['p_PerfTitleClean'] == plays[2]]
beggars = top[top['p_PerfTitleClean'] == plays[3]]
devil = top[top['p_PerfTitleClean'] == plays[4]]

dfs = [hamlet, macbeth, stratagem, beggars, devil]

plays_timeline = []
# get timeline for number of plays over time
for i in range(len(dfs)):
    time = dfs[i].groupby('e_Year')['e_EventId'].nunique()
    time = time.reset_index()
    time.to_csv('{}_overTime.csv'.format(str(plays[i]).replace(' ', '')), index=False)
    plays_timeline.append(time)

play_columns = top.columns
print(play_columns, '\n', 7 * '---------')

steamGraph = top.drop(['e_EventDate', 'e_TheatreCode', 'e_TheatreId',
                       't_TheatreId', 't_TheatreCode', 't_TheatreName', 'p_PerformanceId',
                       'p_EventId', 'p_PerformanceOrder', 'p_PType', 'p_PerformanceTitle', 'c_PerformerClean', 'c_CastId', 'c_PerformanceId', 'c_Role',
                       'c_Performer', 'c_RoleClean'], axis=1)
group = steamGraph.groupby(['e_Year', 'p_PerfTitleClean'])['e_EventId'].nunique()
group = group.reset_index()
group.to_csv('steamGraph.csv', index=False)
