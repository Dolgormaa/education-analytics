from dagster import Definitions

# Import assets and jobs from definitions
from .definitions import (
    taz_dim_date,
    taz_dim_location,
    dbt_education_models,
    dbt_build_assets,
    taz_assets,
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
    assets=[taz_dim_date, taz_dim_location, dbt_education_models],
    jobs=[dbt_build_assets, daily_dbt_job, hourly_dbt_job, weekly_dbt_job],
    schedules=[daily_dbt_schedule, hourly_dbt_schedule, weekly_dbt_schedule],
)