from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import dwh_dbt_assets
from .project import dwh_project
from .schedules import schedules

defs = Definitions(
    assets=[dwh_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=dwh_project),
    },
)

