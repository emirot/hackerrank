SELECT City.Name 
From City
JOIN Country
ON City.CountryCode=Country.Code
WHERE Country.Continent='Africa';
