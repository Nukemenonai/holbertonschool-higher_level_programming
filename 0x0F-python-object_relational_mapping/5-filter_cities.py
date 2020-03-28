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
    sql = "SELECT cities.name \
    FROM cities \
    JOIN states ON states.id = cities.state_id \
    WHERE states.name = %s"""

    cursor.execute(sql, (state,))
    rows = cursor.fetchall()

    print(', '.join([i[0] for i in rows]))

    cursor.close()
    db.close()
