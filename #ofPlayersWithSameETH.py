import pandas as pd

df = pd.read_csv('DuneMaster.csv')

# Schritt 1: Beträge in ETH pro Spieler zu speichern
eth_amount_per_player = {}

# Schritt 2: Iterieren über alle Spieler und speichere den Betrag in ETH pro Spieler
for index, row in df.iterrows():
    player = row['depositor']
    eth_amount = row['deposit_eth']
    
    # Überprüfen, ob der Spieler bereits einen Betrag in ETH gespielt hat
    if player in eth_amount_per_player:
        # Wenn der Spieler zuvor mit einem anderen Betrag gespielt hat, markiere ihn als nicht interessant
        if eth_amount_per_player[player] != eth_amount:
            eth_amount_per_player[player] = None
    else:
        eth_amount_per_player[player] = eth_amount

# Schritt 3: Zählen der Spieler, die immer mit dem gleichen Betrag in ETH gespielt haben
players_with_same_eth_amount = list(filter(lambda x: x is not None, eth_amount_per_player.values()))
num_players_with_same_eth_amount = len(players_with_same_eth_amount)

# Schritt 4: Berechnung der Prozentanzahl
total_players = df['depositor'].nunique()
percentage_players_with_same_eth = (num_players_with_same_eth_amount / total_players) * 100

print("Anzahl der Spieler, die immer mit dem gleichen Betrag in ETH gespielt haben:", num_players_with_same_eth_amount)
print("Prozentanzahl der Spieler, die immer mit dem gleichen Betrag in ETH gespielt haben:", percentage_players_with_same_eth, "%")
