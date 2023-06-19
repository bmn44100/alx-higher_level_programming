#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
script should take 3 arguments:
mysql username, mysql password and database name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
