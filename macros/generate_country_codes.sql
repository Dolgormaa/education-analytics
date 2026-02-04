{% macro generate_country_codes() %}
  WITH distinct_countries AS (
    SELECT DISTINCT Country_Name
    FROM {{ ref('restructure_table') }}
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
{% endmacro %}