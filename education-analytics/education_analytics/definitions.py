from dagster import asset, AssetExecutionContext, define_asset_job, AssetSelection
import subprocess
import os

# Define the dbt project path
DBT_PROJECT_PATH = "/Users/user/dbt/dwh"

@asset
def country_year_mapping(context: AssetExecutionContext):
    """
    dbt model: country_year_mapping
    """
    original_dir = os.getcwd()
    os.chdir(DBT_PROJECT_PATH)

    try:
        result = subprocess.run(
            ["dbt", "run", "--select", "country_year_mapping"],
            capture_output=True,
            text=True,
            check=True
        )
        context.log.info(f"dbt run country_year_mapping completed: {result.stdout}")
        return {"status": "success", "model": "country_year_mapping"}
    except subprocess.CalledProcessError as e:
        context.log.error(f"dbt run country_year_mapping failed: {e.stderr}")
        raise e
    finally:
        os.chdir(original_dir)

@asset
def population_of_primary_education(context: AssetExecutionContext):
    """
    dbt model: population_of_primary_education
    """
    original_dir = os.getcwd()
    os.chdir(DBT_PROJECT_PATH)

    try:
        result = subprocess.run(
            ["dbt", "run", "--select", "population_of_primary_education"],
            capture_output=True,
            text=True,
            check=True
        )
        context.log.info(f"dbt run population_of_primary_education completed: {result.stdout}")
        return {"status": "success", "model": "population_of_primary_education"}
    except subprocess.CalledProcessError as e:
        context.log.error(f"dbt run population_of_primary_education failed: {e.stderr}")
        raise e
    finally:
        os.chdir(original_dir)

@asset
def restructure_table(context: AssetExecutionContext):
    """
    dbt model: restructure_table
    """
    original_dir = os.getcwd()
    os.chdir(DBT_PROJECT_PATH)

    try:
        result = subprocess.run(
            ["dbt", "run", "--select", "restructure_table"],
            capture_output=True,
            text=True,
            check=True
        )
        context.log.info(f"dbt run restructure_table completed: {result.stdout}")
        return {"status": "success", "model": "restructure_table"}
    except subprocess.CalledProcessError as e:
        context.log.error(f"dbt run restructure_table failed: {e.stderr}")
        raise e
    finally:
        os.chdir(original_dir)

@asset
def show_tables(context: AssetExecutionContext):
    """
    dbt model: show_tables
    """
    original_dir = os.getcwd()
    os.chdir(DBT_PROJECT_PATH)

    try:
        result = subprocess.run(
            ["dbt", "run", "--select", "show_tables"],
            capture_output=True,
            text=True,
            check=True
        )
        context.log.info(f"dbt run show_tables completed: {result.stdout}")
        return {"status": "success", "model": "show_tables"}
    except subprocess.CalledProcessError as e:
        context.log.error(f"dbt run show_tables failed: {e.stderr}")
        raise e
    finally:
        os.chdir(original_dir)

# Define the build assets for schedules
dbt_build_assets = define_asset_job(
    name="dbt_build_assets",
    selection=AssetSelection.all(),
)

# Define asset groups
education_assets = [
    country_year_mapping,
    population_of_primary_education,
    restructure_table,
    show_tables
]