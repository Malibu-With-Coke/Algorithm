select year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, GENDER, count(distinct(info.USER_ID)) as USERS
from USER_INFO as info
join ONLINE_SALE as sale on info.USER_ID = sale.USER_ID
where GENDER is not NULL
group by 1, 2, 3
order by 1, 2, 3

# select *
# from USER_INFO as info
# join ONLINE_SALE as sale on info.USER_ID = sale.USER_ID
# where GENDER is not NULL
