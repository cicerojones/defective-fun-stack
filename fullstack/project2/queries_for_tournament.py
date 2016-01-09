import psycopg2


def doDB():
    DB = psycopg2.connect("dbname=tourney_practice")
    c = DB.cursor()
    query = "select pid, player_name from players1;"
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print row
    DB.close()

doDB()
