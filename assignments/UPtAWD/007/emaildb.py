import sqlite3
import re
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


src = open('mbox.txt')
for line in src:
    if line.startswith("From "):
        email = re.findall('^From \S+@+(\S+)',line)
        cur.execute('SELECT org FROM Counts WHERE org = ? ', (email[0], ))
        if cur.fetchone() is None:
            cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( email[0], ) )
        else:
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (email[0], ))
        conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]
cur.close()

