# Write your MySQL query statement below
select v.customer_id , count(v.visit_id) count_no_trans
from Visits v left join transactions t
using(visit_id)
where t.transaction_id is null
group by customer_id