
SELECT  ROUND(SQRT(POW(ABS(MAX(LAT_N) - MIN(LAT_N)), 2) + POW(ABS(MAX(LONG_W) - MIN(LONG_W)),2)),4)  FROM STATION;
