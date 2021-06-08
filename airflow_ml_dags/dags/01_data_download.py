from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

from constants import DEFAULT_ARGS, DATA_VOLUME_DIR

with DAG(
        "1-download-data",
        default_args=DEFAULT_ARGS,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    start = DummyOperator(task_id="Begin")

download = DockerOperator(
        task_id="Generate_data",
        image="airflow-download-data",
        command="--output-dir /data/raw/{{ ds }}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
        environment={
        'KAGGLE_USERNAME': "markhubbatulin",
        'KAGGLE_KEY': "644576713099ef9bf4910baf2c91856d"
        },
    )

finish = DummyOperator(task_id="End")

start >> download >> finish
