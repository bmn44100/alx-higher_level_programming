#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
