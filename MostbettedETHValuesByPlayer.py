import pandas as pd

# Daten laden
df = pd.read_csv('DuneMaster.csv')

# Gruppieren nach Spieler und Einsatz, dann Zählen der Häufigkeit jedes Einsatzes pro Spieler
player_bet_counts = df.groupby(['depositor', 'deposit_eth']).size().reset_index(name='Anzahl der Einsätze')

# Sortieren der Daten nach der Häufigkeit der Einsätze und Auswahl der Top 30
top_30_player_bets = player_bet_counts.sort_values(by='Anzahl der Einsätze', ascending=False).head(30)
top_30_player_bets.reset_index(drop=True, inplace=True)

print(top_30_player_bets)
