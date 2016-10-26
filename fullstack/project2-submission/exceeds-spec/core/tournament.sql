CREATE TABLE playerz (
       player_id serial PRIMARY KEY,
       player_name text not null,
       tournament_name text);


CREATE TABLE match_participants (
       match_id serial PRIMARY KEY,
       home int REFERENCES playerz (player_id),
       away int REFERENCES playerz (player_id));

CREATE TABLE matchez(
       match_id int REFERENCES match_participants (match_id),
       tournament_name text DEFAULT 'none',
       round int); 


CREATE TABLE score_results (
       match_id int REFERENCES match_participants (match_id),
       home_score int,
       away_score int);

CREATE TABLE player_recordz (
       player_id int REFERENCES playerz (player_id),
       tournament_name text,
       wins int DEFAULT 0,
       losses int DEFAULT 0,
       draws int DEFAULT 0,
       points int DEFAULT 0,
       OMW int DEFAULT 0);

CREATE VIEW tournament_matches AS
select a.match_id, a.tournament_name, a.round, b.home, b.away, c.home_score, c.away_score
from matchez as a, match_participants as b, score_results as c
where a.match_id = b.match_id
AND b.match_id = c.match_id;

CREATE VIEW player_tables AS
select a.player_id, a.player_name, a.tournament_name, b.wins, b.losses, b.draws, b.points, b.OMW
from playerz as a, player_recordz as b
where a.player_id = b.player_id;

CREATE OR REPLACE FUNCTION initialize_player_rec() RETURNS TRIGGER AS $$
       BEGIN
	INSERT INTO player_recordz (player_id) VALUES (NEW.player_id);
	RETURN NEW;
       END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER initialize_player_rec
       AFTER INSERT ON playerz FOR EACH row EXECUTE PROCEDURE
       initialize_player_rec();

CREATE OR REPLACE FUNCTION initialize_matchez() RETURNS TRIGGER AS $$
       BEGIN
	INSERT INTO matchez (match_id) VALUES (NEW.match_id);
	RETURN NEW;
       END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER initialize_match_participants
       AFTER INSERT ON match_participants FOR EACH row EXECUTE PROCEDURE
       initialize_matchez();

CREATE OR REPLACE FUNCTION log_draws(round_no integer, tournament_name text) RETURNS VOID AS $$
       UPDATE player_recordz SET draws = draws + 1
       from tournament_matches as a 
       WHERE a.home_score = a.away_score
       AND (a.home = player_id OR a.away = player_id)
       AND a.round = $1 AND a.tournament_name = $2
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION log_away_wins(round_no integer, tournament_name text) RETURNS VOID AS $$
       UPDATE player_recordz SET wins = wins + 1
       from tournament_matches as a 
       WHERE a.home_score < a.away_score
       AND a.away = player_id
       AND a.round = $1 AND a.tournament_name = $2
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION log_away_losses(round_no integer, tournament_name text) RETURNS VOID AS $$
       UPDATE player_recordz SET losses = losses + 1
       from tournament_matches as a 
       WHERE a.home_score > a.away_score
       AND a.away = player_id
       AND a.round = $1 AND a.tournament_name = $2
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION log_home_wins(round_no integer, tournament_name text) RETURNS VOID AS $$
       UPDATE player_recordz SET wins = wins + 1
       from tournament_matches as a 
       WHERE a.home_score > a.away_score
       AND a.home = player_id
       AND a.round = $1 AND a.tournament_name = $2
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION log_home_losses(round_no integer, tournament_name text) RETURNS VOID AS $$
       UPDATE player_recordz SET losses = losses + 1
       from tournament_matches as a 
       WHERE a.home_score < a.away_score
       AND a.home = player_id
       AND a.round = $1 AND a.tournament_name = $2
$$ LANGUAGE SQL;


CREATE OR REPLACE FUNCTION update_points() RETURNS VOID AS $$
       UPDATE player_recordz 
       SET points = (wins * 3) + draws;
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION players_matches (integer) RETURNS TABLE (opposing_player int) AS $$
       select 
       	      CASE WHEN a.away = $1 THEN a.home
	      	   WHEN a.home = $1 THEN a.away
		   ELSE NULL
		END as opposing_player
FROM match_participants as a;
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION player_OMW (integer) RETURNS TABLE (opponent int, opponent_OMW int) AS $$
       select opposing_player, a.points FROM players_matches($1) JOIN player_tables as A
       ON opposing_player = player_id
       WHERE opposing_player IS NOT NULL;
$$ LANGUAGE SQL;


CREATE OR REPLACE FUNCTION set_omw (integer) RETURNS VOID AS $$
       UPDATE player_recordz SET omw = (select sum(opponent_OMW) FROM player_omw($1))
       WHERE player_id = $1;
$$ LANGUAGE SQL;







































CREATE OR REPLACE FUNCTION log_records(round_no integer, tournament_name text) RETURNS VOID as $$
       SELECT log_home_losses($1, $2);
       SELECT log_home_wins($1, $2);
       SELECT log_away_losses($1, $2);
       SELECT log_away_wins($1, $2);
       SELECT log_draws($1, $2);
       SELECT update_points();
$$ LANGUAGE SQL;


