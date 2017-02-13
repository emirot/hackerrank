/*
Enter your query here.
*/
SELECT
CASE WHEN ( ((A + C) > B) AND ((B + A) > C ) AND ((B + C) > A)) THEN 
    CASE WHEN (A=B AND A=C AND B=C)  THEN 'Equilateral' 
    WHEN ((A = B) or (B = C) or (A=C)) THEN 'Isosceles'
    ELSE 'Scalene' END
ELSE 'Not A Triangle' END
FROM TRIANGLES;

