#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
script should take 4 arguments:
mysql username, mysql password, database name and state name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id",
                (argv[4], ))
    cities = cur.fetchall()
    index = 0
    for city in cities:
        if index != 0:
            print(", ", end="")
        print("%s" % city, end="")
        index += 1
    print("")
    cur.close()
    db.close()
