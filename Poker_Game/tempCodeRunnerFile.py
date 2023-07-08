
conn = sqlite3.connect("statistic.db")
curr=conn.cursor()
conn.commit()
table = curr.execute("create table if not exists urun (urunKodu int, urunAdi text, birimFiyati int)")
conn.commit()