#!/usr/bin/python3
'''finds all states starting by N'''

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
    sql = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
