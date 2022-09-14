import csv
from db_control import DB

con = DB().db_connect()
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS \
    test_table (date DATE primary key, name VARCHAR(255), num INTEGER(10))')
cur.execute('DELETE FROM test_table')

with open('test_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        cur.execute(f'INSERT INTO test_table(date, name, num) \
            VALUES ("{r[0]}", "{r[1]}", {r[2]})')

cur.execute(f'SELECT * FROM test_table')
print(cur.fetchall())

con.commit()
con.close()

