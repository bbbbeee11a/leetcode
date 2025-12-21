-- # Write your MySQL query statement below
-- SELECT
--   id,
--   recordDate,
--   temperature,
--   LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp
-- FROM Weather;

SELECT DISTINCT(num) AS ConsecutiveNums
FROM (SELECT id, num, LAG(num) OVER (ORDER BY id) AS num1, LAG(num, 2) OVER (ORDER BY id) AS num2
FROM Logs) t
WHERE num = num1 and num1 = num2;
 
