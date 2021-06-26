from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor

from constants import (
    DEFAULT_ARGS, START_DATE, RAW_DATA_DIR, PROCESSED_DATA_DIR, SPLITTING_DATA_DIR,
    DATA_VOLUME_DIR, MODEL_DIR,
)

with DAG(
        "02_train_pipeline",
        default_args=DEFAULT_ARGS,
        schedule_interval="@weekly",
        start_date=START_DATE
) as dag:
    start = DummyOperator(task_id="Begin")

    data_sensor = FileSensor(
        task_id="Waiting_data",
        poke_interval=10,
        retries=100,
        filepath="data/raw/{{ ds }}/data.csv",

    )

    target_sensor = FileSensor(
        task_id="Waiting_target",
        poke_interval=10,
        retries=100,
        filepath="data/raw/{{ ds }}/target.csv",
    )

    preprocess = DockerOperator(
        task_id="Preprocess",
        image="airflow-preprocess",
        command=f"{RAW_DATA_DIR} {PROCESSED_DATA_DIR} {MODEL_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
    )

    split = DockerOperator(
        task_id="Split",
        image="airflow-split",
        command=f"{PROCESSED_DATA_DIR} {SPLITTING_DATA_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"]
    )

    train = DockerOperator(
        task_id="Train",
        image="airflow-train",
        command=F"{SPLITTING_DATA_DIR} {MODEL_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"]
    )

    validate = DockerOperator(
        task_id="Validate",
        image="airflow-validate",
        command=f"{SPLITTING_DATA_DIR} {MODEL_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"]
    )

    finish = DummyOperator(task_id="End")

    start >> [data_sensor, target_sensor] >> preprocess >> split >> train >> validate >> finish
