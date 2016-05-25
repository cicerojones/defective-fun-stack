def myTestRegister():
    deleteMatches()
    deletePlayers()
    registerPlayer("tourney_practice", "playerz", "Chandra Nalaar", "polo")
    c = new_countPlayers("tourney_practice", "playerz")
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4. After registering a player, countPlayers() returns 1."


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
    # registerMatchParticipants(
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


# Previous testing code unaltered
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
