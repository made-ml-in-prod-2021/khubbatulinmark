from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator

from constants import (
    DEFAULT_ARGS, RAW_DATA_DIR, DATA_VOLUME_DIR, START_DATE,
    KAGGLE_USERNAME, KAGGLE_KEY
)

with DAG(
        "01-download-data",
        default_args=DEFAULT_ARGS,
        schedule_interval="@daily",
        start_date=START_DATE,
) as dag:
    start = DummyOperator(task_id="Begin")

download = DockerOperator(
    task_id="Download-data",
    image="airflow-download-data",
    command=f"--output-dir {RAW_DATA_DIR}",
    network_mode="bridge",
    do_xcom_push=False,
    volumes=[f"{DATA_VOLUME_DIR}:/data"],
    environment={
        'KAGGLE_USERNAME': KAGGLE_USERNAME,
        'KAGGLE_KEY': KAGGLE_KEY
    },
)

finish = DummyOperator(task_id="End")

start >> download >> finish
