(
    select car_id, "대여 가능" as AVAILABILITY
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where car_id not in (
        select car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where '2022-10-16' between START_DATE and END_DATE
    )
    group by car_id
)
union
(
    select car_id, "대여중" as AVAILABILITY
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where car_id in (
        select car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where '2022-10-16' between START_DATE and END_DATE
    )
    group by car_id
)
order by car_id desc