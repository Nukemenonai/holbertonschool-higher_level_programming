-- Lists all cities of california that can be found in database
SELECT * FROM cities WHERE (
       SELECT *
       FROM states
       WHERE name = 'California'
) ORDER BY cities.id ASC;
