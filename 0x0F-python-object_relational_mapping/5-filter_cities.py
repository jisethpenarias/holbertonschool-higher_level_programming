#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    # cur.execute return the number of states
    cur.execute("SELECT cities.name FROM cities " +
                " INNER JOIN states " +
                " ON cities.state_id = states.id " +
                " WHERE states.name = %s ORDER BY cities.id ASC", (state,))
    rows = cur.fetchall()
    for idx, row in enumerate(rows):
        for col in row:
            if (idx < len(rows) - 1):
                print (col, end=", ")
            else:
                print (col, end="")
    print()
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
