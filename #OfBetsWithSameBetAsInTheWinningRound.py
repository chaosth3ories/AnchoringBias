import pandas as pd

# Daten laden
df = pd.read_csv('DuneMaster.csv')

# Nächsten Einsatz für jede Runde berechnen
df['next_bet'] = df.groupby('depositor')['deposit_eth'].shift(-1)

# Gewinnrunden identifizieren
winners = df[df['is_winner'] == 1]

# Überprüfen, ob der nächste Einsatz gleich dem Gewinneinsatz ist
winners['same_bet'] = winners['deposit_eth'] == winners['next_bet']

# Anzahl der Gewinnrunden, in denen der gleiche Betrag gesetzt wurde
same_bet_count = winners['same_bet'].sum()

# Gesamtanzahl der Gewinnrunden
total_win_count = winners.shape[0]

# Prozentsatz der Gewinnrunden mit gleichem Einsatz berechnen
percentage_same_bet = (same_bet_count / total_win_count) * 100

print(f"Prozentsatz der Gewinnrunden, in denen der gleiche Betrag noch einmal gesetzt wurde: {percentage_same_bet:.2f}%")

