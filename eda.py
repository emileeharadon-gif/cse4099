import soccerdata as sd
import pandas as pd

understat = sd.Understat(
    leagues="ESP-La Liga",
    seasons=["2018/2019", "2019/2020", "2020/2021"]
)

# Retrieve datasets
teams = understat.read_team_match_stats()
players = understat.read_player_season_stats()
shots = understat.read_shot_events()

# Dataset overview
datasets = {
    "Teams": teams,
    "Players": players,
    "Shots": shots
}

for name, df in datasets.items():
    print(f"\n{'=' * 40}")
    print(f"{name.upper()} DATA")
    print(f"{'=' * 40}")

    print("Shape:", df.shape)
    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nData types:")
    print(df.dtypes)

    print("\nSample:")
    print(df.head())

# Save datasets
teams.to_csv("team_stats.csv")
players.to_csv("player_stats.csv")
shots.to_csv("shot_events.csv")

print("\nEDA data collection complete.")