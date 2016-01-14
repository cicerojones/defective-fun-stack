import psycopg2

# refactor to use connect() for final version
def dbExecuteWrapper(query_string, extra=None):
    DB = psycopg2.connect("dbname=tourney_practice")
    c = DB.cursor()
    c.execute(query_string, extra)
    DB.commit()
    DB.close()


def dbExecuteRetrievalWrapper_allrows(query_string):
    DB = psycopg2.connect("dbname=tourney_practice")
    c = DB.cursor()
    c.execute(query_string)
    rows = c.fetchall()
    return rows
    DB.close()


def dbExecuteWrapper_noparameter(query_string):
    DB = psycopg2.connect("dbname=tourney_practice")
    c = DB.cursor()
    c.execute(query_string)
    DB.commit()
    DB.close()


def deleteMatches():
    dbExecuteWrapper("""delete from matches2;""")


def deletePlayers():
    dbExecuteWrapper("""delete from players2;""")


def countPlayers():
    DB = psycopg2.connect("dbname=tourney_practice")
    c = DB.cursor()
    # refactor to use a query parameter
    c.execute("select count(*) from players2;")
    row = c.fetchone()
    row_item = list(row)
    return int(row_item[0])
    DB.close()


def registerPlayer(name):
    dbExecuteWrapper("""INSERT INTO players2 (player_name, wins, matches) VALUES (%s, %s, %s);""", (name, 0, 0))


def playerStandings():
    return dbExecuteRetrievalWrapper_allrows("""select id, player_name, wins, matches from players2 order by wins desc;""")


def reportMatch(winner, loser):
    dbExecuteWrapper("""INSERT INTO matches2 VALUES (%s, %s) ;""", (winner, loser))
    # dbExecuteWrapper_noparameter("""update players2 set wins = wins + 1  from matches2 where players2.id = matches2.winner;""")
    dbExecuteWrapper("""update players2 set wins = wins + 1  from matches2 where players2.id = matches2.winner;""")
    # dbExecuteWrapper_noparameter("""update players2 set matches = matches + 1  from matches2 where players2.id = matches2.winner OR players2.id = matches2.loser;""")
    dbExecuteWrapper("""update players2 set matches = matches + 1  from matches2 where players2.id = matches2.winner OR players2.id = matches2.loser;""")


    def swissPairings():
    return dbExecuteRetrievalWrapper_allrows("select a.id, a.player_name, b.id, b.player_name from players2 as a, players2 as b where a.wins = b.wins and a.player_name != b.player_name and a.id < b.id")
