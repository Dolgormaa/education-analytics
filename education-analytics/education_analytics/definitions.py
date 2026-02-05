from dagster import asset, AssetExecutionContext, define_asset_job, AssetSelection
import subprocess
import os

# Define the dbt project path
DBT_PROJECT_PATH = "/Users/user/dbt/dwh"

@asset(key=["taz", "dim_Date"])
def taz_dim_date(context: AssetExecutionContext):
    """
    dbt model: taz/dim_Date
    """
    original_dir = os.getcwd()
    os.chdir(DBT_PROJECT_PATH)

    try:
        result = subprocess.run(
            ["dbt", "run", "--select", "dim_Date"],
            capture_output=True,
            text=True,
            check=True
        )
        context.log.info(f"dbt run dim_Date completed: {result.stdout}")
        return {"status": "success", "model": "dim_Date"}
    except subprocess.CalledProcessError as e:
        context.log.error(f"dbt run dim_Date failed: {e.stderr}")
        raise e
    finally:
        os.chdir(original_dir)

@asset(key=["taz", "dim_Location"])
def taz_dim_location(context: AssetExecutionContext):
    """
    dbt model: taz/dim_Location
    """
    original_dir = os.getcwd()
    os.chdir(DBT_PROJECT_PATH)

    try:
        result = subprocess.run(
            ["dbt", "run", "--select", "dim_Location"],
            capture_output=True,
            text=True,
            check=True
        )
        context.log.info(f"dbt run dim_Location completed: {result.stdout}")
        return {"status": "success", "model": "dim_Location"}
    except subprocess.CalledProcessError as e:
        context.log.error(f"dbt run dim_Location failed: {e.stderr}")
        raise e
    finally:
        os.chdir(original_dir)

@asset
def dbt_education_models(context: AssetExecutionContext):
    """
    Execute all dbt models for education analytics
    """
    original_dir = os.getcwd()
    os.chdir(DBT_PROJECT_PATH)

    try:
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
        os.chdir(original_dir)

# Define the build assets for schedules
dbt_build_assets = define_asset_job(
    name="dbt_build_assets",
    selection=AssetSelection.all(),
)

# Define specific asset groups
taz_assets = [taz_dim_date, taz_dim_location]
education_assets = [dbt_education_models]