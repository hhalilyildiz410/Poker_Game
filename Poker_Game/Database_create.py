import sqlite3
import itertools
from winner_check import Game

combinations = list(itertools.combinations(Game().deck_create(), 2))
combinations = [list(combination) for combination in combinations]
# print(sorted(combinations))
conn = sqlite3.connect('statistic.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS PokerStatistics
                (hands TEXT, hand_count INT, win_count INT)''')

cursor.execute("CREATE INDEX index_cards ON PokerStatistics(hands)")

for combination in combinations:
    hands = ' '.join(sorted(combination))
    cursor.execute("INSERT INTO PokerStatistics (hands, hand_count, win_count) VALUES (?, 0, 0)", (hands,))

conn.commit()
conn.close()
