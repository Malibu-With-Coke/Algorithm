-- 코드를 입력하세요
# with TS as 
# (
#     SELECT BOOK_ID, sum(SALES * SALES_DATE) as TOTAL_SALES
#     FROM BOOK_SALES  as bs
#     where year(SALES_DATE) = 2022 and month(SALES_DATE) = 1
#     group by BOOK_ID
# )

select BOOK.AUTHOR_ID, AUTHOR.AUTHOR_NAME, BOOK.CATEGORY, sum(SALES* PRICE) as TOTAL_SALES
from BOOK 
left join AUTHOR on BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
left join BOOK_SALES on BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
where year(SALES_DATE) = 2022 and month(SALES_DATE) = 1
group by BOOK.AUTHOR_ID, BOOK.CATEGORY
order by AUTHOR_ID, CATEGORY DESC

# BOOK.author_id as AUTHOR_ID, AUTHOR.author_name as AUTHOR_NAME