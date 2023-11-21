#!/usr/bin/python3
""" Module that contains a script do action to database"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Print state that matches argument"""
    db = MySQLdb.connect(
            host="localhost", passwd=sys.argv[2],
            user=sys.argv[1], db=sys.argv[3], port=3306
        )
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE %s  ORDER BY id ASC",
            (sys.argv[4],)
    )
    for states in cursor.fetchall():
        print(states)
