# Write your MySQL query statement below


SELECT t.emp_id AS employee_id
FROM (
    SELECT E.employee_id AS emp_id,
    E.manager_id AS manager_exists,
    E.salary AS salary,
    M.employee_id AS manager_exists_now
    FROM Employees E
    LEFT JOIN Employees M
    ON E.manager_id = M.employee_id
) t
WHERE t.salary < 30000 AND t.manager_exists IS NOT NULL AND t.manager_exists_now IS NULL
ORDER BY employee_id;