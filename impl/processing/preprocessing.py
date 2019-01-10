import sqlite3
def loader(offset, db='./dataset/input.db'):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute('''SELECT * FROM CODE LIMIT %d, 5''' % offset)
    return curs

if __name__ == '__main__':
    curs = loader(2)
    print(curs.fetchall()[0][3])