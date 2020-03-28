#!/usr/bin/python3
'''first inner join '''
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
    sql = "SELECT \
    cities.id, cities.name, states.name \
    FROM cities \
    JOIN states ON states.id = cities.state_id \
    ORDER BY cities.id ASC"

    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
