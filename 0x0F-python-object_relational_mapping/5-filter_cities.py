#!/usr/bin/python3
'''Filters states by user input from MySQL database hbtn_0e_0_usa'''
import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    state = sys.argv[4]
    query = "SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s"
    cur = db.cursor()
    cur.execute(query, (state, ))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
