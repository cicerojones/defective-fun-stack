import psycopg2


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


def new_deleteTable(dbname, table_name):
    tb_name = table_name
    sql_keywords = """DELETE FROM """
    query = sql_keywords + tb_name
#    table_nm = (table_name,)
    new_dbExecuteWrapper(query, dbname)


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


def keyword_statement_string(table_name, sql_keyword):
    tb_name = table_name
    sql_keywords = sql_keyword + """ """
    update_statement = sql_keywords + tb_name + """ """
    return update_statement


def new_registerPlayer(dbname, table_name, player_name):
    insert_statement = keyword_statement_string(table_name, """INSERT INTO""")
    query = (insert_statement + "(player_name, wins, matchez)" +
             "VALUES (%s, %s, %s);")
    new_dbExecuteWrapper(query, dbname, (player_name, 0, 0))


def new_playerStandings(table_name):
    from_statement = keyword_statement_string(table_name, """FROM""")
    query = ("SELECT id, player_name, wins, matchez " +
             from_statement + "ORDER BY wins DESC;")
    return new_dbExecuteRetrievalWrapper_allrows("tourney_practice", query)


def new_reportMatch(dbname, table1, table2, winner, loser):
    q1_insert = keyword_statement_string(table2, """INSERT INTO""")
    q2_update = keyword_statement_string(table1, """UPDATE""")
    q2_from = keyword_statement_string(table2, """FROM""")
    query1 = (q1_insert + "VALUES (%s, %s) ;")
    query2 = (q2_update + "SET wins = wins + 1" +
              q2_from + "WHERE playerz.id = (%s);")
    query3 = (q2_update + "SET matchez = matchez + 1" +
              q2_from + "WHERE playerz.id = (%s) OR playerz.id = (%s);")
    new_dbExecuteWrapper(query1, dbname, (winner, loser))
    new_dbExecuteWrapper(query2, dbname, (winner,))
    new_dbExecuteWrapper(query3, dbname, (winner, loser))
