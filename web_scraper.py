from bs4 import BeautifulSoup
import requests
import csv

base_url = "https://www.basketball-reference.com"

page = requests.get(base_url + "/teams")
soup = BeautifulSoup(page.content, "html.parser")
count = 0

with open("players.csv", mode="a") as csv_file:
    fieldnames = ['Player Name', 'Team', 'Season']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    rows = soup.find_all("th", {"data-stat" : "franch_name"})

    for row in list(rows):
        if (row.a != None):
            team_name = row.a.get("href")
            team = team_name.split("/")[2]

            if (team == "AND"):
                break

            team_url = base_url + team_name

            team_page = requests.get(team_url)
            team_soup = BeautifulSoup(team_page.content, "html.parser")

            season_rows = team_soup.find_all("th", {"data-stat" : "season"})

            for season_row in list(season_rows):
                if (season_row.a != None):
                    team_season = season_row.a.get("href")
                    season = team_season.split("/")[3].split(".")[0]

                    season_url = base_url + team_season

                    season_page = requests.get(season_url)
                    season_soup = BeautifulSoup(season_page.content, "html.parser")

                    player_rows = season_soup.find_all("td", {"data-stat" : "player"})

                    for player_row in list(player_rows):
                        if (player_row.a != None):
                            player_name = player_row.a.text
                            if (count == 0):
                                writer.writeheader()
                            writer.writerow({'Player Name': player_name, 'Team': team, 'Season': season})
                            count += 1
