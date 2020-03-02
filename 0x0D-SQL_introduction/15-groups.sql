-- lists number of records with same score
SELECT score FROM second_table GROUP BY COUNT(score) > 1 AS number;
