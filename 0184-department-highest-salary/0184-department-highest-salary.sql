# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
SELECT d.name AS Department, 
e.name AS Employee,
e.salary AS Salary,
RANK() OVER(PARTITION BY departmentID ORDER BY Salary DESC) AS rnk
FROM Employee e LEFT JOIN Department d
ON e.departmentID = d.id
) t
WHERE t.rnk = 1;