import sqlite3
conn = sqlite3.connect('example.db')
#Write :memory: to create a database in RAM.

c = conn.cursor()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()

conn = sqlite3.connect('example.db')
c = conn.cursor()
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchone()
conn.commit()
conn.close()


conn = sqlite3.connect('example.db')
c = conn.cursor()
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
conn.commit()
conn.close()


conn = sqlite3.connect('example.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print row
conn.commit()
conn.close()
