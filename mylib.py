import pandas as pd
import numpy as np
import plotly.graph_objects as go

def get_season_number(date_match):
    year = int(date_match[:4])
    month = int(date_match[5:7])
    season_number = year - 2014
    if (month > 6) and (year < 2020):
        season_number += 1
    return season_number

def create_match_label(h_a, team, team_a, scored, missed):
    if h_a == 'h':
        match_label = "{} {:d}:{:d} {}".format(team, scored, missed, team_a)
    else:
        match_label = "{} {:d}:{:d} {}".format(team_a, missed, scored, team)
    return match_label

def create_figure_withplot_for_league_with_season_dropdown(data_for_one_league, league_title):
    fig = go.Figure() 
    fig.update_layout(
        width=900,
        height=500,
        autosize=False,
        margin=dict(t=100, b=0, l=0, r=0),
    )
    get_season_label = {(a+1): ['14/15', '15/16', '16/17', '17/18', '18/19', '19/20'][a] for a in range(6)}
    for season_number in np.arange(1,7):
        teams_list_current_season = data_for_one_league[(data_for_one_league['season_number'] == season_number)]['team'].unique()
        teams_list_current_season = np.sort(teams_list_current_season)
        for team_name in teams_list_current_season:
            data_team = data_for_one_league[(data_for_one_league['team'] == team_name) & 
                                            (data_for_one_league['season_number'] == season_number)
                                           ][['round', 'points_after', 'match_label']]
            current_trace = go.Scatter(
                x = data_team['round'],
                y = data_team['points_after'],
                hovertemplate = '%{text}<br>' + 'Round %{x}<br>' + 'Points %{y}',
                text = data_team['match_label'],
                legendgrouptitle = dict(text=get_season_label[season_number]),
                name = team_name,
                visible = season_number==1
            )
            fig.add_trace(current_trace)
    fig.update_layout(
        updatemenus=[
            dict(
                buttons = list(
                    dict(
                        label=get_season_label[season_number],
                        method="update",
                        args=[
                            dict(visible=[get_season_label[season_number] == t.legendgrouptitle.text for t in fig.data]),
                            dict(title=league_title + ' ' + get_season_label[season_number])
                        ]
                    ) for season_number in np.arange(1,7)
                ),
                x=0.21,
                y=1.1
            )
        ]
    )
    fig.update_layout(
        annotations=[
            dict(text="<b>Season</b>", x=0.1, xref="paper", xanchor ="right", 
                 y=1.08, yref="paper", align="left", showarrow=False),
        ],
        title=dict(
            text = league_title + " 14/15",
            x=0.5,
            font=dict(size=30)
        ),
        yaxis_range=[0,105]
    )
    return fig
