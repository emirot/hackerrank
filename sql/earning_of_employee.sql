SET @my_var = (SELECT MAX(tmp.earnings) 
FROM ( 
SELECT employee_id, name, months, salary , months * salary as earnings
FROM Employee ) tmp);

SET @my_var2 = (
    SELECT COUNT(*)
FROM (SELECT employee_id, name, months, salary , months * salary as earnings FROM employee) tmp
WHERE tmp.earnings = @my_var); 

SELECT @my_var, @my_var2;
