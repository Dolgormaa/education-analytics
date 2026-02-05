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

# Import schedules
from .schedules import daily_dbt_schedule, hourly_dbt_schedule

# Define your Dagster definitions
defs = Definitions(
    assets=[taz_dim_date, taz_dim_location, dbt_education_models],
    jobs=[dbt_build_assets],
    schedules=[daily_dbt_schedule, hourly_dbt_schedule],
)