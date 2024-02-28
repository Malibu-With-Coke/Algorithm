with temp as (
    SELECT ain.ANIMAL_ID, ain.NAME, ain.DATETIME
    from ANIMAL_INS as ain
    join ANIMAL_OUTS as aout on ain.ANIMAL_ID = aout.ANIMAL_ID
    where ain.DATETIME > aout.DATETIME
    order by 3
)
SELECT ANIMAL_ID,NAME
from temp