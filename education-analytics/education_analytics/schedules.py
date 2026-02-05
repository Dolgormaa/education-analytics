# schedule.py

from dagster import (
    ScheduleDefinition,
    DefaultScheduleStatus,
    define_asset_job,
    AssetSelection
)

# Import local assets from definitions
from .definitions import (
    taz_dim_date,
    taz_dim_location,
    dbt_education_models
)

# Daily job → specific dbt model
daily_dbt_job = define_asset_job(
    name="daily_dbt_job",
    selection=AssetSelection.keys("dbt_education_models")
)

# Hourly job → run all dbt models
hourly_dbt_job = define_asset_job(
    name="hourly_dbt_job",
    selection=AssetSelection.all()
)

# --------------------------------------------------
# SCHEDULE DEFINITIONS
# --------------------------------------------------

# Daily at 02:00 UTC
daily_dbt_schedule = ScheduleDefinition(
    job=daily_dbt_job,
    cron_schedule="0 2 * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)

# Hourly schedule
hourly_dbt_schedule = ScheduleDefinition(
    job=hourly_dbt_job,
    cron_schedule="0 * * * *",
    default_status=DefaultScheduleStatus.STOPPED,
)