-- 코드를 입력하세요
WITH RECURSIVE cte (n) AS
(
  SELECT 0
  UNION ALL
  SELECT n + 1 FROM cte WHERE n < 23
)

SELECT n, COUNT(ANIMAL_ID) as COUNT
from cte left join ANIMAL_OUTS on cte.n = hour(ANIMAL_OUTS.DATETIME)
group by 1
order by 1
# where 

