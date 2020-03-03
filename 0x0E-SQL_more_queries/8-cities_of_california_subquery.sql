-- Lists all cities of california that can be found in database
SELECT cities.id, cities.name
FROM cities, states
WHERE state_id = (states.id=cities.state_id AND states.name = 'California')
ORDER BY cities.id ASC;
