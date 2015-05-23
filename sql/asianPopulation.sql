SELECT SUM(City.Population) 
FROM City JOIN Country 
ON  City.CountryCode=Country.Code 
where Continent='Asia';
