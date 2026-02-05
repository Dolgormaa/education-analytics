from dagster import Definitions

# Import assets and jobs from definitions
from .definitions import (
    country_year_mapping,
    population_of_primary_education,
    restructure_table,
    show_tables,
    dbt_build_assets,
    education_assets
)

# Import schedules and jobs
from .schedules import (
    daily_dbt_schedule,
    hourly_dbt_schedule,
    weekly_dbt_schedule,
    daily_dbt_job,
    hourly_dbt_job,
    weekly_dbt_job
)

# Define your Dagster definitions
defs = Definitions(
    assets=[country_year_mapping, population_of_primary_education, restructure_table, show_tables],
    jobs=[dbt_build_assets, daily_dbt_job, hourly_dbt_job, weekly_dbt_job],
    schedules=[daily_dbt_schedule, hourly_dbt_schedule, weekly_dbt_schedule],
)