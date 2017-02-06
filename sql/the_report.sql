/*
Enter your query here.
*/
SELECT 
CASE WHEN (g.grade) < 8 THEN 'NULL' ELSE s.name END,  
 g.grade, s.marks
FROM Students s
INNER JOIN GRADES g
ON s.marks >= g.min_mark and s.marks <= g.max_mark 
order by g.grade desc, s.name asc, s.marks asc
