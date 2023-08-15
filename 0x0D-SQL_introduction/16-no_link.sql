-- Lists all records of the second_table having a name value ordred by score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
