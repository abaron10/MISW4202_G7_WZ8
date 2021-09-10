import sqlite3

conn = sqlite3.connect('patient_payments.db')
cur = conn.cursor()

def create_database():
    cur.execute('DROP TABLE IF EXISTS payments')
    cur.execute('''
    CREATE TABLE payments (id INTEGER, name TEXT,lastname TEXT, email TEXT, phone_number TEXT, billing INTEGER, exit_granted BOOLEAN)''')
    cur.close()
# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     email2 = email.split("@")
#     email3 = email2[1]
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (email3,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#                 VALUES (?, 1)''', (email3,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#                     (email3,))
#     conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])


