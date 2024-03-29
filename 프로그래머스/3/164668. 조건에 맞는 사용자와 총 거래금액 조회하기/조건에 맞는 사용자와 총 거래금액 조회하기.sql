# -- 코드를 입력하세요
# SELECT *
# FROM (
#     SELECT WRITER_ID, SUM(PRICE)
#     FROM USED_GOODS_BOARD
#     WHERE USED_GOODS_BOARD.STATUS = "DONE"
#     GROUP BY PRICE
# )
# JOIN USED_GOODS_USER 
# ON USED_GOODS_USER.USER_ID = USED_GOODS_BOARD.WRITER_ID
SELECT WRITER_ID, (SELECT NICKNAME FROM USED_GOODS_USER WHERE USED_GOODS_USER.USER_ID = USED_GOODS_BOARD.WRITER_ID) as NICKNAME, SUM(PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD
WHERE USED_GOODS_BOARD.STATUS = "DONE"
GROUP BY WRITER_ID
HAVING SUM(PRICE)  >= 700000
ORDER BY TOTAL_SALES
