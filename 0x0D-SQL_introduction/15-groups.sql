-- Count similar scores from second_table.
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score;

