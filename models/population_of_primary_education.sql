{{
  config(
    alias='population_of_primary_education'
  )
}}

WITH country_codes AS (
  {{ generate_country_codes() }}
),
primary_education_data AS (
  SELECT
    Country_Name,
    year,
    value
  FROM {{ ref('restructure_table') }}
  WHERE Country_Name IS NOT NULL
    AND year IS NOT NULL
    AND value IS NOT NULL
    AND value != ''
)

SELECT
  p.Country_Name as country_name,
  p.year,
  c.country_code,
  {{ round_value('CAST(p.value AS DECIMAL(15,4))') }} as value
FROM primary_education_data p
LEFT JOIN country_codes c
  ON p.Country_Name = c.Country_Name
WHERE c.country_code IS NOT NULL
ORDER BY c.country_code, p.year