from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.decorators import task
import sys
import os
from pathlib import Path

project_root = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, project_root)

from scripts import ingest_openpwl

REPO_LOC = "data/opl-repo/"
OUT_LOC = "data/download-out/"

airflow_home = os.environ.get("AIRFLOW_HOME", "~/airflow")
airflow_home = Path(airflow_home).expanduser()

repo_path = airflow_home / REPO_LOC
out_path = airflow_home / OUT_LOC

with DAG(
    dag_id="ingest_openpowerlifting_data",
    start_date=datetime(2023, 4, 19),
    schedule="0 0 * * *"
    ) as dag:


    @task()
    def download_data():

        ingest_openpwl.download_openpwl_data(out_path, repo_path)

    download_data()

    