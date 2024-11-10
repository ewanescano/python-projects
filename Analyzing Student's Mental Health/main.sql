-- Run this code to view the data in students
SELECT * 
FROM students;

SELECT
	stay,
	COUNT(*) as count_int,
	ROUND(AVG(todep),2) as average_phq,
	ROUND(AVG(tosc),2) as average_scs,
	ROUND(AVG(toas),2) AS average_as
FROM students
WHERE 
	stay IS NOT NULL AND
	inter_dom LIKE 'Inter'
GROUP BY stay
ORDER BY stay DESC