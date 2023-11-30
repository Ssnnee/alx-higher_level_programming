#!/usr/bin/python3
""" Module that contains a script do action to database"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Print state that matches argument"""
    db = MySQLdb.connect(
        host="localhost",
        passwd=sys.argv[2],
        user=sys.argv[1],
        db=sys.argv[3],
        port=3306,
    )
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    for city_id, cities, states in cursor.fetchall():
        print("({}, '{}', '{}')".format(city_id, cities, states))
