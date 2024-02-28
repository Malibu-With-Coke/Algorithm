select fh.FLAVOR
from FIRST_HALF as fh
join JULY as j on fh.FLAVOR = j.FLAVOR
group by fh.FLAVOR
order by (fh.TOTAL_ORDER + sum(j.TOTAL_ORDER)) desc
limit 3