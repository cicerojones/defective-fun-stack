#!/usr/bin/env python
#
# Test cases for tournament.py
# Old satisfies requirements mixed with exceeds
# result of messy tangling

from final_project import *

def testDeleteMatches():
    deleteMatches()
    print "1. Old matches can be deleted."


def testDelete():
    deleteMatches()
    deletePlayers()
    print "2. Player records can be deleted."


def testCount():
    deleteMatches()
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3. After deleting, countPlayers() returns zero."


def testRegister():
    deleteMatches()
    deletePlayers()
    registerPlayer("Chandra Nalaar")
    c = countPlayers()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4. After registering a player, countPlayers() returns 1."


def testRegisterCountDelete():
    deleteMatches()
    deletePlayers()
    registerPlayer("Markov Chaney")
    registerPlayer("Joe Malik")
    registerPlayer("Mao Tsu-hsi")
    registerPlayer("Atlanta Hope")
    c = countPlayers()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = countPlayers()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. Players can be registered and deleted."


def testStandingsBeforeMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("Melpomene Murray")
    registerPlayer("Randy Schwartz")
    standings = playerStandings()
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "6. Newly registered players appear in the standings with no matches."


def testReportMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("Bruno Walton")
    registerPlayer("Boots O'Neal")
    registerPlayer("Cathy Burton")
    registerPlayer("Diane Grant")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    standings = playerStandings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, players have updated standings."


def testPairings():
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Fluttershy")
    registerPlayer("Applejack")
    registerPlayer("Pinkie Pie")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    pairings = swissPairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."


if __name__ == '__main__':
    testDeleteMatches()
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testStandingsBeforeMatches()
    testReportMatches()
    testPairings()
    print "Success!  All tests pass!"

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


# refactor to use connect() for final version
def dbExecuteWrapper(query_string, extra=None):
    DB = connect()
    c = DB.cursor()
    c.execute(query_string, extra)
    DB.commit()
    DB.close()


def dbExecuteRetrievalWrapper_allrows(query_string):
    DB = connect()
    c = DB.cursor()
    c.execute(query_string)
    rows = c.fetchall()
    return rows
    DB.close()


# refactor all queries into a variable that is then passed to execute
def deleteMatches():
    query = """DELETE FROM matches;"""
    dbExecuteWrapper(query)


def deletePlayers():
    query = """DELETE FROM players;"""
    dbExecuteWrapper(query)


def countPlayers():
    DB = connect()
    c = DB.cursor()
    query = "SELECT count(*) FROM players;"
    c.execute(query)
    row = c.fetchone()
    row_item = list(row)
    return int(row_item[0])
    DB.close()


def registerPlayer(name):
    query = ("INSERT INTO players (player_name, wins, matches)"
             "VALUES (%s, %s, %s);")
    dbExecuteWrapper(query, (name, 0, 0))


# Some kind of problem using _allrows with multiline string formatting
def playerStandings():
    query = ("SELECT id, player_name, wins, matches "
             "FROM players ORDER BY wins DESC;")
    return dbExecuteRetrievalWrapper_allrows(query)


def reportMatch(winner, loser):
    query1 = ("INSERT INTO matches VALUES (%s, %s) ;")
    query2 = ("UPDATE players SET wins = wins + 1"
              "FROM matches WHERE players.id = (%s) ;")
    query3 = ("UPDATE players SET matches = matches + 1"
              "FROM matches WHERE players.id = (%s) OR players.id = (%s);")
    dbExecuteWrapper(query1, (winner, loser))
    dbExecuteWrapper(query2, (winner,))
    dbExecuteWrapper(query3, (winner, loser))


def swissPairings():
    query = ("SELECT a.id, a.player_name, b.id, b.player_name "
             "FROM players as a, players as b "
             "WHERE a.wins = b.wins "
             "AND a.player_name != b.player_name "
             "AND a.id < b.id")
    return dbExecuteRetrievalWrapper_allrows(query)

new_registerPlayer("tourney_practice", "playerz", 'a', "tennis")
new_registerPlayer("tourney_practice", "playerz", 'b', "tennis")
new_registerPlayer("tourney_practice", "playerz", 'c', "tennis")
new_registerPlayer("tourney_practice", "playerz", 'd', "tennis")
new_registerPlayer("tourney_practice", "playerz", 'e', "tennis")
new_registerPlayer("tourney_practice", "playerz", 'f', "tennis")
new_registerPlayer("tourney_practice", "playerz", 'g', "tennis")
new_registerPlayer("tourney_practice", "playerz", 'h', "tennis")

registerMatchParticipants("tourney_practice", "match_participants", "tennis", 1, 1, 2)
registerMatchParticipants("tourney_practice", "match_participants", "tennis", 1, 3, 4)
registerMatchParticipants("tourney_practice", "match_participants", "tennis", 1, 5, 6)
registerMatchParticipants("tourney_practice", "match_participants", "tennis", 1, 7, 8)

registerScores("tourney_practice", "score_results", 1, 1, 0)
registerScores("tourney_practice", "score_results", 2, 0, 1)
registerScores("tourney_practice", "score_results", 3, 1, 0)
registerScores("tourney_practice", "score_results", 4, 0, 1)

log_round_results("tourney_practice", "tennis", 1)
set_all_OMW('tourney_practice')

naive_swissPairings(2, "tennis")

registerScores("tourney_practice", "score_results", 5, 1, 0)
registerScores("tourney_practice", "score_results", 6, 0, 1)
registerScores("tourney_practice", "score_results", 7, 1, 0)
registerScores("tourney_practice", "score_results", 8, 0, 1)

log_round_results("tourney_practice", "tennis", 2)
set_all_OMW('tourney_practice')

naive_swissPairings(3, "tennis")

registerScores("tourney_practice", "score_results", 9, 1, 0)
registerScores("tourney_practice", "score_results", 10, 0, 1)
registerScores("tourney_practice", "score_results", 11, 1, 0)
registerScores("tourney_practice", "score_results", 12, 0, 1)

log_round_results("tourney_practice", "tennis", 3)
set_all_OMW('tourney_practice')

new_registerPlayer("tourney_practice", "playerz", 'allen', "soccer")
new_registerPlayer("tourney_practice", "playerz", 'beverly', "soccer")
new_registerPlayer("tourney_practice", "playerz", 'cleanth', "soccer")
new_registerPlayer("tourney_practice", "playerz", 'devon', "soccer")
# new_registerPlayer("tourney_practice", "playerz", 'eldridge', "soccer")
1 + 1
new_registerPlayer("tourney_practice", "playerz", 'eldridge', "soccer")
new_registerPlayer("tourney_practice", "playerz", 'fatool', "soccer")
new_registerPlayer("tourney_practice", "playerz", 'g-money', "soccer")
new_registerPlayer("tourney_practice", "playerz", 'harold', "soccer")

1 + 1
# registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 9, 10)
# registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 11, 12)
# registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 13, 14)
# registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 15, 16)


registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 9, 10)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 11, 12)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 13, 14)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 15, 16)

registerScores("tourney_practice", "score_results", 13, 1, 0)
registerScores("tourney_practice", "score_results", 14, 0, 1)
registerScores("tourney_practice", "score_results", 15, 1, 0)
registerScores("tourney_practice", "score_results", 16, 0, 1)

log_round_results("tourney_practice", "soccer", 1)
set_all_OMW('tourney_practice')

naive_swissPairings(2, "soccer")


## 
registerScores("tourney_practice", "score_results", 17, 1, 1)
registerScores("tourney_practice", "score_results", 18, 0, 1)
registerScores("tourney_practice", "score_results", 19, 1, 0)
registerScores("tourney_practice", "score_results", 20, 0, 1)

log_round_results("tourney_practice", "soccer", 2)
set_all_OMW('tourney_practice')

naive_swissPairings(3, "soccer")

registerScores("tourney_practice", "score_results", 21, 1, 0)
registerScores("tourney_practice", "score_results", 22, 0, 1)
registerScores("tourney_practice", "score_results", 23, 1, 0)
registerScores("tourney_practice", "score_results", 24, 0, 1)

log_round_results("tourney_practice", "soccer", 3)
set_all_OMW('tourney_practice')

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

# deletion
def new_deleteTable(dbname, table_name):
    tb_name = table_name
    sql_keywords = """DELETE FROM """
    query = sql_keywords + tb_name
    table_nm = (table_name,)
    new_dbExecuteWrapper(query, dbname)

def update_statement_string(table_name):
    tb_name = table_name
    sql_keywords = """UPDATE """
    update_statement = sql_keywords + tb_name

# used in registerMatchParticipants
def keyword_statement_string(table_name, sql_keyword):
    tb_name = table_name
    sql_keywords = sql_keyword + """ """
    update_statement = sql_keywords + tb_name + """ """
    return update_statement

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

def new_registerPlayer(dbname, table_name, player_name, tournament_name):
    insert_statement = keyword_statement_string(table_name, """INSERT INTO""")
    query = (insert_statement + "(player_name, tournament_name)" +
             "VALUES (%s, %s);")
    new_dbExecuteWrapper(query, dbname, (player_name, tournament_name))

def myTestRegister():
    deleteMatches()
    deletePlayers()
    registerPlayer("tourney_practice", "playerz", "Chandra Nalaar", "polo")
    c = new_countPlayers("tourney_practice", "playerz")
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4. After registering a player, countPlayers() returns 1."

def registerMatchParticipants(dbname, table_name, sport, round_no, player_id1, player_id2):
    participant_insert_statement = keyword_statement_string(table_name, """INSERT INTO""")
    query2 = (participant_insert_statement + "(home, away)" + "VALUES (%s, %s);")
    new_dbExecuteWrapper(query2, dbname, (player_id1, player_id2))
    match_update_statement = keyword_statement_string("""matchez""", """UPDATE""")
    query1 = (match_update_statement +
              "SET tournament_name= (%s), round = (%s) WHERE tournament_name= 'none';")
    new_dbExecuteWrapper(query1, dbname, (sport, round_no))

def testRegisterCountDelete():
    deleteMatches()
    deletePlayers()
    registerPlayer("tourney_practice", "playerz", "Markov Chaney", "polo")
    registerPlayer("tourney_practice", "playerz", "Joe Malik", "polo")
    registerPlayer("tourney_practice", "playerz", "Mao Tsu-hsi", "polo")
    registerPlayer("tourney_practice", "playerz", "Atlanta Hope", "polo")
    c = new_countPlayers("tourney_practice", "playerz")
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = new_countPlayers("tourney_practice", "playerz")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. Players can be registered and deleted."

    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
        raise ValueError("Each playerStandings row should have four columns.")

new_registerPlayer("tourney_practice", "playerz", "Melpomene Murray", "polo")
new_registerPlayer("tourney_practice", "playerz", "Randy Schwartz", "polo")
standings = new_playerStandings_alt("tourney_practice", "player_tables", "polo")
len(standings[0])

def testStandingsBeforeMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("tourney_practice", "playerz", "Melpomene Murray", "polo")
    registerPlayer("tourney_practice", "playerz", "Randy Schwartz", "polo")
    standings = new_playerStandings_alt("tourney_practice", "player_tables", "polo")
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "6. Newly registered players appear in the standings with no matches."

def registerScores(dbname, table_name, match_no, home_score, away_score):
    insert_statement = keyword_statement_string(table_name, """INSERT INTO""")
    query = (insert_statement + "VALUES (%s, %s, %s);")
    new_dbExecuteWrapper(query, dbname, (match_no, home_score, away_score))

def testReportMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("tourney_practice", "playerz", "Bruno Walton", "knock-hockey")
    registerPlayer("tourney_practice", "playerz", "Boots O'Neal", "knock-hockey")
    registerPlayer("tourney_practice", "playerz", "Cathy Burton", "knock-hockey")
    registerPlayer("tourney_practice", "playerz", "Diane Grant", "knock-hockey")
    standings = new_playerStandings_alt("tourney_practice", "player_tables", "knock-hockey")
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    standings = new_playerStandings_alt("tourney_practice", "player_tables", "knock-hockey")
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, players have updated standings."

def log_round_results(dbname, tournament_name, round_of_tournament):
    query = "SELECT * FROM log_records(%s, %s)"
    new_dbExecuteWrapper(query, dbname, (round_of_tournament, tournament_name))

# note 
def set_all_OMW(dbname):
    data = how_many_players(dbname)
    playaz = [n[0] for n in data]
    [set_OMW(dbname, n) for n in playaz]
    print("done")

def how_many_players(dbname):
    query = "select * from player_recordz;"
    return new_dbExecuteRetrievalWrapper_allrows(dbname, query)


def set_OMW(dbname, player_id):
    query = "SELECT * FROM set_omw(%s);"
    new_dbExecuteWrapper(query, dbname, (player_id,))

def naive_swissPairings(round_no, tournament_name):
    next_round = naive_pairings(tournament_name)
    for pair in next_round:
        registerMatchParticipants("tourney_practice", "match_participants", tournament_name, round_no, pair[0], pair[1])

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

def testPairings():
    deleteMatches()
    deletePlayers()
    registerPlayer("tourney_practice", "playerz", "Twilight Sparkle", "polo")
    registerPlayer("tourney_practice", "playerz", "Fluttershy", "polo")
    registerPlayer("tourney_practice", "playerz", "Applejack", "polo")
    registerPlayer("tourney_practice", "playerz", "Pinkie Pie", "polo")
    standings = new_playerStandings_alt("tourney_practice", "player_tables", "polo")
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    registerMatchParticipants(
    registerScores(
    registerScores(
    log_round_results("tourney_practice", "tennis", 1)
    set_all_OMW('tourney_practice')
    
    pairings = swissPairings()

    naive_swissPairings(2, "tennis")
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."

def testDeleteMatches():

def testDelete():

def testCount():

def testRegister():

def testRegisterCountDelete():

def testStandingsBeforeMatches():

def testReportMatches():

def testPairings():

# def deletePlayers():
#    new_deleteTable("tourney_practice", "playerz")


# def deleteMatches():
#     new_deleteTable("tourney_practice", "matchez")

def allowsTies_test():
# register four teams/players for a soccer tournament
new_registerPlayer("tourney_practice", "playerz", 'a', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'b', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'c', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'd', "soccer");

# create two matches for these four participants
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 1, 2)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 3, 4)

# register scores for the given matches, with one being a tie
registerScores("tourney_practice", "score_results", 1, 1, 1)
registerScores("tourney_practice", "score_results", 2, 0, 1)

 
print "9. Allows ties"

print "10. Supports more than one tournament in database"

# registering a player also inserts a row for that player's record
new_registerPlayer("tourney_practice", "playerz", 'a', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'b', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'c', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'd', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'e', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'f', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'g', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'h', "tennis");


# must register the participants of the first match.
# after that, the pairings of players will be determined by 
# running naive_swissPairings, the results of which will
# be used when reporting the next match results between those players
registerMatchParticipants("tourney_practice", "match_participants", "tennis", 1, 1, 2)
registerMatchParticipants("tourney_practice", "match_participants", "tennis", 1, 3, 4)
registerMatchParticipants("tourney_practice", "match_participants", "tennis", 1, 5, 6)
registerMatchParticipants("tourney_practice", "match_participants", "tennis", 1, 7, 8)

# scores are reported for a match number and for the notion of
# home vs. away players
registerScores("tourney_practice", "score_results", 1, 1, 0)
registerScores("tourney_practice", "score_results", 2, 0, 1)
registerScores("tourney_practice", "score_results", 3, 1, 0)
registerScores("tourney_practice", "score_results", 4, 0, 1)

# calculate the stats for the given tournament
log_round_results("tourney_practice", "tennis", 1)
set_all_OMW('tourney_practice')

# determine the pairings for the next round of the given tournament,
# both of which (the round number and the tournament name) are given
# as arguments
naive_swissPairings(2, "tennis")

new_registerPlayer("tourney_practice", "playerz", 'allen', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'beverly', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'cleanth', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'devon', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'eldridge', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'fatool', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'g-money', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'harold', "soccer");

# setup the first round with predetermined matches
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 9, 10)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 11, 12)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 13, 14)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 15, 16)

registerScores("tourney_practice", "score_results", 13, 1, 0)
registerScores("tourney_practice", "score_results", 14, 0, 1)
registerScores("tourney_practice", "score_results", 15, 1, 0)
registerScores("tourney_practice", "score_results", 16, 0, 1)

log_round_results("tourney_practice", "soccer", 1)
set_all_OMW('tourney_practice')

naive_swissPairings(2, "soccer")

print "11. Uses Opponent Match Points as criteria for breaking ties in ranking"

new_registerPlayer("tourney_practice", "playerz", 'aaaa', "foosball")
