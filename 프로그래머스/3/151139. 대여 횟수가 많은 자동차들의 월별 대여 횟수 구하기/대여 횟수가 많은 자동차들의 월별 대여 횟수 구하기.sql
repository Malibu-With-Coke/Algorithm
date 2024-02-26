with get_car_id as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where month(START_DATE) >= 8 and month(START_DATE) <= 10 and year(START_DATE) = 2022
    group by CAR_ID
    having count(CAR_ID) >= 5
)

select month(START_DATE), a.CAR_ID, count(a.CAR_ID)
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as a
join get_car_id as b on a.CAR_ID = b.CAR_ID
where month(START_DATE) >= 8 and month(START_DATE) <= 10 and year(START_DATE) = 2022
group by 1, 2
order by 1, 2 desc

# select CAR_ID
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where month(START_DATE) = 8 and year(START_DATE) = 2022
# group by CAR_ID
# having count(CAR_ID) >= 5