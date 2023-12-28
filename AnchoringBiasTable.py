import pandas as pd

# Laden der Daten aus der Datei
data = pd.read_csv('DuneMaster.csv')

# Berechnen des ETH-zu-USD-Kurses für jede Runde
data['eth_to_usd'] = data['deposit_usd'] / data['deposit_eth']

# Funktion, um zu überprüfen, ob ein Spieler die Bedingung für "Mental Accounting" erfüllt
def check_mental_accounting(player_group):
    for deposit_eth, eth_group in player_group.groupby('deposit_eth'):
        eth_prices = eth_group['eth_to_usd'].unique()
        if any(abs(p1 - p2) / min(p1, p2) > 0.20 for p1 in eth_prices for p2 in eth_prices if p1 != p2):
            return 1
    return 0

# Anwenden der Funktion auf jede Spielergruppe
players_mental_accounting = data.groupby('depositor').apply(check_mental_accounting)

# Hinzufügen der "Mental Accounting"-Kennzeichnung zu den Daten
data['mental_accounting'] = data['depositor'].map(players_mental_accounting)

# Filtern der Daten für Spieler, die die Bedingung erfüllen
mental_accounting_players = data[data['mental_accounting'] == 1]

# Berechnung der durchschnittlichen Wettbeträge in ETH
average_deposit = mental_accounting_players['deposit_eth'].mean()

# Berechnung des durchschnittlichen Gewinns/Verlusts
average_win_loss = mental_accounting_players.apply(
    lambda row: -row['deposit_eth'] if row['is_winner'] == 0 else (mental_accounting_players[mental_accounting_players['roundid'] == row['roundid']]['deposit_eth'].sum() - row['deposit_eth']),
    axis=1
).mean()

# Berechnung der durchschnittlichen Anzahl an gespielten Runden
average_rounds_played = mental_accounting_players.groupby('depositor')['roundid'].nunique().mean()

# Ausgabe der Ergebnisse
print("Anzahl der Spieler mit Mental Accounting:", players_mental_accounting.sum())
print("Durchschnittlicher Wettbetrag in ETH:", average_deposit)
print("Durchschnittlicher Gewinn/Verlust:", average_win_loss)
print("Durchschnittliche Anzahl gespielter Runden:", average_rounds_played)
