
with Max_pr as (
    select CATEGORY, MAX(PRICE) as MAX_PRICE
    from FOOD_PRODUCT
    where category = '식용유' or category = '과자' or category = '김치' or category = '국'
    group by category
)
select a.CATEGORY, a.PRICE as MAX_PRICE, a.PRODUCT_NAME
from FOOD_PRODUCT as a
join Max_pr as b on a.CATEGORY = b.CATEGORY and a.PRICE = b.MAX_PRICE
order by 2 desc
# select CATEGORY, MAX(PRICE) as MAX_PRICE, PRODUCT_NAME