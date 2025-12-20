# Write your MySQL query statement below
select a.product_name, b.year, b.price
from Product a JOIN Sales b
ON a.product_id = b.product_id;