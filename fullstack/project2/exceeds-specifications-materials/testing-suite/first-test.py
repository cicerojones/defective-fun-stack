

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
