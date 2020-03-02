-- script that imports a table and returns an average
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
