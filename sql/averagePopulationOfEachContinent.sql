SELECT 
Country.Continent,
FLOOR(AVG(City.Population))
FROM City
JOIN Country
ON City.CountryCode=Country.Code
GROUP BY Country.Continent;
