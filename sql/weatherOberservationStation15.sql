
SELECT ROUND(nn.LONG_W, 4)
FROM(
SELECT id, lat_n , long_w  FROM station
WHERE LAT_N < 137.2345
order by lat_n desc
LIMIT 1
) nn
