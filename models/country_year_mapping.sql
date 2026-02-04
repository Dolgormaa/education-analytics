{{
  config(
    alias='country_year_mapping'
  )
}}

WITH country_codes AS (
  {{ generate_country_codes() }}
),
primary_education_data AS (
  SELECT DISTINCT
    Country_Name,
    year,
    value
  FROM {{ ref('restructure_table') }}
  WHERE Country_Name IS NOT NULL
    AND year IS NOT NULL
)

SELECT
  p.Country_Name as country_name,
  p.year,
  c.country_code,
  value
FROM primary_education_data p
LEFT JOIN country_codes c
  ON p.Country_Name = c.Country_Name
ORDER BY c.country_code, p.year