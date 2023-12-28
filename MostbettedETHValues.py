import pandas as pd

# Daten laden
df = pd.read_csv('DuneMaster.csv')

# Zählen, wie oft jeder ETH-Betrag insgesamt gesetzt wurde
bet_counts = df['deposit_eth'].value_counts()

# Zählen, wie viele einzigartige Spieler jeden ETH-Betrag gesetzt haben
unique_player_counts = df.groupby('deposit_eth')['depositor'].nunique()

# Zusammenführen der beiden Statistiken in einem DataFrame
bet_stats_df = pd.DataFrame({
    'Gesamtanzahl der Einsätze': bet_counts,
    'Anzahl einzigartiger Spieler': unique_player_counts
}).reset_index()

bet_stats_df.columns = ['Einsatz (ETH)', 'Gesamtanzahl der Einsätze', 'Anzahl einzigartiger Spieler']

# Sortieren der Daten nach der Häufigkeit der Einsätze und Auswahl der Top 20
bet_stats_sorted_df = bet_stats_df.sort_values(by='Gesamtanzahl der Einsätze', ascending=False).head(20)
bet_stats_sorted_df.reset_index(drop=True, inplace=True)

print(bet_stats_sorted_df)
