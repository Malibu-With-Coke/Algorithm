with cantRental as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where '2022-11-01' BETWEEN START_DATE AND END_DATE
    or '2022-11-31' BETWEEN START_DATE AND END_DATE
    or START_DATE BETWEEN '2022-11-01' AND '2022-11-31'
    or END_DATE BETWEEN '2022-11-01' AND '2022-11-31'
), sedanOrSUV as (
    select CAR_ID, info.CAR_TYPE, floor(30 * DAILY_FEE * (1-DISCOUNT_RATE/100)) as FEE
    from CAR_RENTAL_COMPANY_CAR as info
    join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as plan
    on info.CAR_TYPE = plan.CAR_TYPE
    where info.CAR_TYPE in ('세단', 'SUV') and DURATION_TYPE like '30%'
)

select a.*
from sedanOrSUV as a
where a.fee between 500000 and 2000000 
and a.CAR_ID not in (select CAR_ID
                    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                    where '2022-11-01' BETWEEN START_DATE AND END_DATE
                    or '2022-11-31' BETWEEN START_DATE AND END_DATE
                    or START_DATE BETWEEN '2022-11-01' AND '2022-11-31'
                    or END_DATE BETWEEN '2022-11-01' AND '2022-11-31')
order by 3 desc, 2 asc, 1 desc