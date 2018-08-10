import csv
import pandas as pd
import itertools


df = pd.read_csv('players.csv', names=['Player Name', 'Team', 'Season'], skiprows = 1)

grouped = df.groupby(["Team", "Season"])
count = 0

with open("edges_with_duplicates.csv", mode="w") as csv_file:
    for name, team_df in grouped:
        roster = []

        for i in range(team_df.shape[0]):
            roster.append(team_df.iloc[i]["Player Name"])

        fieldnames = ['Player1', 'Player2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        for (player1, player2) in list(itertools.combinations(roster, 2)):
            if (count > 0):
                writer.writerow({'Player1': player1, 'Player2': player2})
            count += 1

df2 = pd.read_csv('edges_with_duplicates.csv', names=["Player1", "Player2"], skiprows = 1)

df3 = df2.drop_duplicates()
df3.to_csv('player_edges.csv', index = False)
