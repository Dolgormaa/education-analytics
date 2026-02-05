# schedule.py

from dagster import (
    ScheduleDefinition,
    DefaultScheduleStatus,
    define_asset_job,
    AssetSelection
)

# Daily job → specific dbt models from /Users/user/dbt/dwh/models
daily_dbt_job = define_asset_job(
    name="daily_dbt_job",
    selection=AssetSelection.keys(
        "country_year_mapping",
        "population_of_primary_education"
    )
)

# Hourly job → run all education dbt models
hourly_dbt_job = define_asset_job(
    name="hourly_dbt_job",
    selection=AssetSelection.keys(
        "country_year_mapping",
        "population_of_primary_education",
        "restructure_table",
        "show_tables"
    )
)

# Weekly job → full refresh of all models
weekly_dbt_job = define_asset_job(
    name="weekly_dbt_job",
    selection=AssetSelection.all()
)

# --------------------------------------------------
# SCHEDULE DEFINITIONS
# --------------------------------------------------

# Daily at 02:00 UTC - Core models
daily_dbt_schedule = ScheduleDefinition(
    job=daily_dbt_job,
    cron_schedule="0 2 * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)

# Hourly schedule - All education models
hourly_dbt_schedule = ScheduleDefinition(
    job=hourly_dbt_job,
    cron_schedule="0 * * * *",
    default_status=DefaultScheduleStatus.STOPPED,
)

# Weekly schedule - Full refresh on Sundays at 1 AM
weekly_dbt_schedule = ScheduleDefinition(
    job=weekly_dbt_job,
    cron_schedule="0 1 * * 0",
    default_status=DefaultScheduleStatus.RUNNING,
)