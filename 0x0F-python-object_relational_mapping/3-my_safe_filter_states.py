#!/usr/bin/python3
"""
a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
one that is safe from MySQL injections!
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE %s ORDER BY states.id",
                (argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
