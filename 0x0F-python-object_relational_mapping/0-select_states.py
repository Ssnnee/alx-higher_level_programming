#!/usr/bin/python3
""" Module that contains a script do action to database"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Print all states of database """
    db = MySQLdb.connect(host="localhost" user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3] port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
