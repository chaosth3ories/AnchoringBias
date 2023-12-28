import pandas as pd

# Annahme: Du hast bereits die CSV-Datei in ein DataFrame geladen, nennen wir es 'df'.
df = pd.read_csv('DuneMaster.csv')

# Schritt 1: Filtere die Daten nach Gewinnern der vorherigen Runde
winners_previous_round = df[df['is_winner'] == 1]

# Schritt 2: Erstelle ein leeres DataFrame, um die Anzahl der Spiele pro Spieler zu speichern
games_count_df = pd.DataFrame(columns=['player', 'games_count'])

# Schritt 3: Iteriere über die Gewinner und zähle die Spiele pro Spieler und Betrag
for index, winner_row in winners_previous_round.iterrows():
    player = winner_row['depositor']
    eth_amount = winner_row['deposit_eth']
    
    # Filtere die Spiele des Gewinners mit dem gleichen Betrag in der nächsten Runde
    matching_games = df[(df['depositor'] == player) & (df['deposit_eth'] == eth_amount) & (df['roundid'] > winner_row['roundid'])]
    
    # Zähle die Anzahl der Spiele und füge sie zum DataFrame hinzu
    games_count = len(matching_games)
    games_count_df.loc[len(games_count_df)] = [player, games_count]

# Schritt 4: Berechne den Median der Spiele pro Spieler
median_games_count = games_count_df['games_count'].median()

print("Median der Anzahl der Spiele nach einem Gewinn mit dem gleichen Betrag in ETH:", median_games_count)
