import psycopg2


# db interaction plumbing


def new_connect(dbname):
    dbname_string = "dbname={}".format(dbname)
    return psycopg2.connect(dbname_string)


def new_dbExecuteWrapper(query_string, dbname, extra=None):
    DB = new_connect(dbname)
    c = DB.cursor()
    c.execute(query_string, extra)
    DB.commit()
    DB.close()


def new_dbExecuteRetrievalWrapper_allrows(dbname, query_string):
    DB = new_connect(dbname)
    c = DB.cursor()
    c.execute(query_string)
    rows = c.fetchall()
    DB.close()
    return rows


# SQL 'dsl' helpers

# function never used
def update_statement_string(table_name):
    tb_name = table_name
    sql_keywords = """UPDATE """
    update_statement = sql_keywords + tb_name


def keyword_statement_string(table_name, sql_keyword):
    tb_name = table_name
    sql_keywords = sql_keyword + """ """
    update_statement = sql_keywords + tb_name + """ """
    return update_statement


# deletion
def new_deleteTable(dbname, table_name):
    tb_name = table_name
    sql_keywords = """DELETE FROM """
    query = sql_keywords + tb_name
    table_nm = (table_name,)
    new_dbExecuteWrapper(query, dbname)


def deletePlayers():
    new_deleteTable("tourney_practice", "playerz")


def deleteMatches():
    new_deleteTable("tourney_practice", "matchez")


# original Python db interaction
def new_countPlayers(dbname, table_name):
    DB = new_connect(dbname)
    c = DB.cursor()
    from_statement = keyword_statement_string(table_name, """FROM""")
    query = "SELECT count(*)" + from_statement + ";"
    c.execute(query)
    row = c.fetchone()
    row_item = list(row)
    DB.close()
    return int(row_item[0])

# refactor to allow substituting column names?


def new_registerPlayer(dbname, table_name, player_name, tournament_name):
    insert_statement = keyword_statement_string(table_name, """INSERT INTO""")
    query = (insert_statement + "(player_name, tournament_name)" +
             "VALUES (%s, %s);")
    new_dbExecuteWrapper(query, dbname, (player_name, tournament_name))

# ### IMPORTANT: which table/view and which columns??


def new_playerStandings(dbname, table_name):
    from_statement = keyword_statement_string(table_name, """FROM""")
    query = ("SELECT player_id, points " +
             from_statement + "ORDER BY points DESC;")
    return new_dbExecuteRetrievalWrapper_allrows(dbname, query)


def registerMatch(dbname, table_name, tournament_name, round_of_tournament):
    insert_statement = keyword_statement_string(table_name, """INSERT INTO""")
    query = (insert_statement + "(tournament_name, round)" +
             "VALUES (%s, %s);")
    new_dbExecuteWrapper(query, dbname, (tournament_name, round_of_tournament))


# use update_statement_string(table_name)???
def registerMatchParticipants(dbname, table_name, sport, round_no, player_id1, player_id2):
    participant_insert_statement = keyword_statement_string(table_name, """INSERT INTO""")
    query2 = (participant_insert_statement + "(home, away)" + "VALUES (%s, %s);")
    new_dbExecuteWrapper(query2, dbname, (player_id1, player_id2))
    match_update_statement = keyword_statement_string("""matchez""", """UPDATE""")
    query1 = (match_update_statement +
              "SET tournament_name= (%s), round = (%s) WHERE tournament_name= 'none';")
    new_dbExecuteWrapper(query1, dbname, (sport, round_no))


def registerScores(dbname, table_name, match_no, home_score, away_score):
    insert_statement = keyword_statement_string(table_name, """INSERT INTO""")
    query = (insert_statement + "VALUES (%s, %s, %s);")
    new_dbExecuteWrapper(query, dbname, (match_no, home_score, away_score))


def log_round_results(dbname, tournament_name, round_of_tournament):
    query = "SELECT * FROM log_records(%s, %s)"
    new_dbExecuteWrapper(query, dbname, (round_of_tournament, tournament_name))

# a brittle way to obtain player ids?


def how_many_players(dbname):
    query = "select * from player_recordz;"
    return new_dbExecuteRetrievalWrapper_allrows(dbname, query)


def set_OMW(dbname, player_id):
    query = "SELECT * FROM set_omw(%s);"
    new_dbExecuteWrapper(query, dbname, (player_id,))


def set_all_OMW(dbname):
    data = how_many_players(dbname)
    playaz = [n[0] for n in data]
    [set_OMW(dbname, n) for n in playaz]
    print("done")


def new_playerStandings_alt(dbname, table_name, tournament_name):
    from_statement = keyword_statement_string(table_name, """FROM""")
    query = "SELECT * " + from_statement + "WHERE tournament_name = (%s) ORDER BY points DESC, omw DESC;"
    DB = new_connect(dbname)
    c = DB.cursor()
    c.execute(query, (tournament_name,))
    rows = c.fetchall()
    DB.close()
    return rows
#    return new_dbExecuteRetrievalWrapper_allrows(dbname, query, tournament_name)

# conatins hard-coded db and table (the wrong table originally!)

def naive_pairings(tournament_name):
    pairings = []
    tables = new_playerStandings_alt("tourney_practice", "player_tables", tournament_name)
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in tables]
    pairings = [(id1, id2), (id3, id4), (id5, id6), (id7, id8)]
    return pairings

# uses the hard-coding naive_pairings

def naive_swissPairings(round_no, tournament_name):
    next_round = naive_pairings(tournament_name)
    for pair in next_round:
        registerMatchParticipants("tourney_practice", "match_participants", tournament_name, round_no, pair[0], pair[1])
