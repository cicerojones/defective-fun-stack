from final_project import *

# registering a player also inserts a row for that player's record
new_registerPlayer("tourney_practice", "playerz", 'albert', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'beverly', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'cleanth', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'devon', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'eldridge', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'fatool', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'g-money', "tennis");
new_registerPlayer("tourney_practice", "playerz", 'harold', "tennis");



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
determine_top_two("tourney_practice", "player_tables", "tennis")

naive_swissPairings(2, "tennis")


registerScores("tourney_practice", "score_results", 5, 1, 0)
registerScores("tourney_practice", "score_results", 6, 0, 1)
registerScores("tourney_practice", "score_results", 7, 1, 0)
registerScores("tourney_practice", "score_results", 8, 0, 1)

log_round_results("tourney_practice", "tennis", 2)
set_all_OMW('tourney_practice')
determine_top_two("tourney_practice", "player_tables", "tennis")

naive_swissPairings(3, "tennis")

registerScores("tourney_practice", "score_results", 9, 1, 0)
registerScores("tourney_practice", "score_results", 10, 0, 1)
registerScores("tourney_practice", "score_results", 11, 1, 0)
registerScores("tourney_practice", "score_results", 12, 0, 1)

log_round_results("tourney_practice", "tennis", 3)
set_all_OMW('tourney_practice')

determine_top_two("tourney_practice", "player_tables", "tennis")
determine_winner("tourney_practice", "player_tables", "tennis")


### register players for soccer tournament
new_registerPlayer("tourney_practice", "playerz", 'aztecs', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'beards', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'choirs', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'devils', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'ejects', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'freaks', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'gomers', "soccer");
new_registerPlayer("tourney_practice", "playerz", 'homers', "soccer");

registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 9, 10)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 11, 12)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 13, 14)
registerMatchParticipants("tourney_practice", "match_participants", "soccer", 1, 15, 16)

## watch out for ties in the first round
registerScores("tourney_practice", "score_results", 13, 1, 0)
registerScores("tourney_practice", "score_results", 14, 0, 1)
registerScores("tourney_practice", "score_results", 15, 1, 0)
registerScores("tourney_practice", "score_results", 16, 0, 1)

log_round_results("tourney_practice", "soccer", 1)
set_all_OMW('tourney_practice')
determine_top_two("tourney_practice", "player_tables", "soccer")

naive_swissPairings(2, "soccer")

# one tie! 
registerScores("tourney_practice", "score_results", 17, 1, 0)
registerScores("tourney_practice", "score_results", 18, 0, 1)
registerScores("tourney_practice", "score_results", 19, 1, 0)
registerScores("tourney_practice", "score_results", 20, 0, 1)

log_round_results("tourney_practice", "soccer", 2)
set_all_OMW('tourney_practice')
determine_top_two("tourney_practice", "player_tables", "soccer")

naive_swissPairings(3, "soccer")

registerScores("tourney_practice", "score_results", 21, 1, 1)
registerScores("tourney_practice", "score_results", 22, 0, 1)
registerScores("tourney_practice", "score_results", 23, 1, 0)
registerScores("tourney_practice", "score_results", 24, 0, 1)

log_round_results("tourney_practice", "soccer", 3)
set_all_OMW('tourney_practice')

determine_top_two("tourney_practice", "player_tables", "soccer")
determine_winner("tourney_practice", "player_tables", "soccer")

### register players for mahjong tournament
new_registerPlayer("tourney_practice", "playerz", 'aleph', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'betel', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'colon', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'dippy', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'eeker', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'fubar', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'gonad', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'hilly', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'isomr', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'joker', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'lossy', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'mamie', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'nadir', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'oopsy', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'pappi', "mahjong");
new_registerPlayer("tourney_practice", "playerz", 'quail', "mahjong");

registerMatchParticipants("tourney_practice", "match_participants", "mahjong", 1, 17, 18)
registerMatchParticipants("tourney_practice", "match_participants", "mahjong", 1, 19, 20)
registerMatchParticipants("tourney_practice", "match_participants", "mahjong", 1, 21, 22)
registerMatchParticipants("tourney_practice", "match_participants", "mahjong", 1, 23, 24)
registerMatchParticipants("tourney_practice", "match_participants", "mahjong", 1, 25, 26)
registerMatchParticipants("tourney_practice", "match_participants", "mahjong", 1, 27, 28)
registerMatchParticipants("tourney_practice", "match_participants", "mahjong", 1, 29, 30)
registerMatchParticipants("tourney_practice", "match_participants", "mahjong", 1, 31, 32)

## watch out for ties in the first round
registerScores("tourney_practice", "score_results", 25, 1, 0)
registerScores("tourney_practice", "score_results", 26, 0, 1)
registerScores("tourney_practice", "score_results", 27, 1, 0)
registerScores("tourney_practice", "score_results", 28, 0, 1)
registerScores("tourney_practice", "score_results", 29, 1, 0)
registerScores("tourney_practice", "score_results", 30, 0, 1)
registerScores("tourney_practice", "score_results", 31, 1, 0)
registerScores("tourney_practice", "score_results", 32, 0, 1)

log_round_results("tourney_practice", "mahjong", 1)
set_all_OMW('tourney_practice')
determine_top_two("tourney_practice", "player_tables", "mahjong")

naive_swissPairings(2, "mahjong")

# # one tie! 
# registerScores("tourney_practice", "score_results", 21, 1, 0)
# registerScores("tourney_practice", "score_results", 22, 0, 1)
# registerScores("tourney_practice", "score_results", 23, 1, 0)
# registerScores("tourney_practice", "score_results", 20, 0, 1)

# log_round_results("tourney_practice", "mahjong", 2)
# set_all_OMW('tourney_practice')
# determine_top_two("tourney_practice", "player_tables", "mahjong")

# naive_swissPairings(3, "mahjong")

# registerScores("tourney_practice", "score_results", 21, 1, 1)
# registerScores("tourney_practice", "score_results", 22, 0, 1)
# registerScores("tourney_practice", "score_results", 23, 1, 0)
# registerScores("tourney_practice", "score_results", 24, 0, 1)

# log_round_results("tourney_practice", "mahjong", 3)
# set_all_OMW('tourney_practice')

# determine_top_two("tourney_practice", "player_tables", "mahjong")
# determine_winner("tourney_practice", "player_tables", "mahjong")

