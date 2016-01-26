SET @A := (SELECT  AVG(salary) FROM employees);

SET @B := (SELECT AVG(fl.sal) FROM(
SELECT CONVERT(REPLACE(CONVERT(SALARY, CHAR),'0',''), UNSIGNED INTEGER)  as sal
FROM employees) fl);

SELECT ROUND(CEIL(@A - @B));
