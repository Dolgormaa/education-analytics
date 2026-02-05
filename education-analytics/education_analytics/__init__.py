from dagster import (
    Definitions,
    ScheduleDefinition,
    DefaultScheduleStatus,
    asset,
    AssetExecutionContext,
    define_asset_job,
    AssetSelection
)
import subprocess
import os

# Define the dbt project path
DBT_PROJECT_PATH = "/Users/user/dbt/dwh"

@asset
def dbt_education_models(context: AssetExecutionContext):
    """
    Execute all dbt models for education analytics
    """
    # Change to dbt project directory
    original_dir = os.getcwd()
    os.chdir(DBT_PROJECT_PATH)

    try:
        # Run dbt models
        result = subprocess.run(
            ["dbt", "run"],
            capture_output=True,
            text=True,
            check=True
        )
        context.log.info(f"dbt run completed successfully: {result.stdout}")
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        context.log.error(f"dbt run failed: {e.stderr}")
        raise e
    finally:
        # Return to original directory
        os.chdir(original_dir)

# Define a job that runs the dbt models
education_analytics_job = define_asset_job(
    name="education_analytics_job",
    selection=AssetSelection.all(),
)

# Create a schedule that runs daily at 9 AM
education_schedule = ScheduleDefinition(
    job=education_analytics_job,
    cron_schedule="0 9 * * *",  # Daily at 9 AM
    default_status=DefaultScheduleStatus.RUNNING,
)

# Define your Dagster definitions
defs = Definitions(
    assets=[dbt_education_models],
    jobs=[education_analytics_job],
    schedules=[education_schedule],
)