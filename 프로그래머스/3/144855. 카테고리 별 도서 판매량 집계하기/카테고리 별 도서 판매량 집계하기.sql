select category, sum(SALES) as TOTAL_SALES
from BOOK_SALES
join BOOK on BOOK_SALES.BOOK_ID = BOOK.BOOK_ID
where year(sales_date) = 2022 and month(sales_date) = 1
group by category
order by CATEGORY