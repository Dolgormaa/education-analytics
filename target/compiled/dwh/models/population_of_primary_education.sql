

WITH country_codes AS (
  
  WITH distinct_countries AS (
    SELECT DISTINCT Country_Name
    FROM `claude_db`.`primary_education`
    WHERE Country_Name IS NOT NULL
    ORDER BY Country_Name
  ),
  country_codes AS (
    SELECT
      Country_Name,
      ROW_NUMBER() OVER (ORDER BY Country_Name) as country_code
    FROM distinct_countries
  )
  SELECT * FROM country_codes

),
primary_education_data AS (
  SELECT
    Country_Name,
    year,
    value
  FROM `claude_db`.`primary_education`
  WHERE Country_Name IS NOT NULL
    AND year IS NOT NULL
    AND value IS NOT NULL
    AND value != ''
)

SELECT
  p.Country_Name as country_name,
  p.year,
  c.country_code,
  
  ROUND(CAST(p.value AS DECIMAL(15,4)), 2)
 as value
FROM primary_education_data p
LEFT JOIN country_codes c
  ON p.Country_Name = c.Country_Name
WHERE c.country_code IS NOT NULL
ORDER BY c.country_code, p.year