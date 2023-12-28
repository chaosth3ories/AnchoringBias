import pandas as pd
import matplotlib.pyplot as plt

# Daten laden
df = pd.read_csv('DuneMaster.csv')

# Nächsten Einsatz für jede Runde berechnen
df['next_bet'] = df.groupby('depositor')['deposit_eth'].shift(-1)

# Gewinnrunden identifizieren
winners = df[df['is_winner'] == 1]

# Überprüfen, ob der nächste Einsatz gleich dem Gewinneinsatz ist
winners['same_bet'] = winners['deposit_eth'] == winners['next_bet']

# Durchschnittliche Häufigkeit des gleichen Einsatzes nach einem Gewinn pro Spieler berechnen
average_same_bet = winners.groupby('depositor')['same_bet'].mean()

# Durchschnittswert über alle Gewinner berechnen
overall_average_same_bet = average_same_bet.mean()
print(f"Durchschnittliche Häufigkeit des gleichen Einsatzes nach einem Gewinn pro Spieler: {overall_average_same_bet:.2f}")

# Histogramm der durchschnittlichen Häufigkeiten
plt.figure(figsize=(8, 6))
average_same_bet.hist(bins=30)
plt.title('Durchschnittliche Häufigkeit des gleichen Einsatzes nach einem Gewinn pro Spieler')
plt.xlabel('Durchschnittliche Häufigkeit des gleichen Einsatzes')
plt.ylabel('Anzahl der Spieler')
plt.show()
