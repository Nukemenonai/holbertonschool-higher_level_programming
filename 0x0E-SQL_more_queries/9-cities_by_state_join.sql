-- lists all cities contained in database
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id ASC;
