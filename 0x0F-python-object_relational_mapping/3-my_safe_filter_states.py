#!/usr/bin/python3
'''this script connect to a database '''
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    state = sys.argv[4]
    sql = "SELECT id, name FROM states WHERE name= %s"" ORDER BY id"
    cursor.execute(sql, (state,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
