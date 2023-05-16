-- script that lists all records of the table second_table in MySQL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
