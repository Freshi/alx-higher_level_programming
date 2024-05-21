-- Select all records except where name is null.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
