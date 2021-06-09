from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor

from constants import DEFAULT_ARGS, START_DATE, RAW_DATA_DIR, DATA_VOLUME_DIR

with DAG(
        "02_train_pipeline",
        default_args=DEFAULT_ARGS,
        schedule_interval="@weekly",
        start_date=START_DATE
) as dag:
    start = DummyOperator(task_id="Begin")

    data_sensor = FileSensor(
        task_id="Wait_for_data",
        poke_interval=10,
        retries=100,
        filepath=f"{RAW_DATA_DIR}/data.csv",

    )

    target_sensor = FileSensor(
        task_id="Wait_for_target",
        poke_interval=10,
        retries=100,
        filepath=f"{RAW_DATA_DIR}/target.csv",
    )

    preprocess = DockerOperator(
        task_id="Data_preprocess",
        image="airflow-preprocess",
        command = "/data/raw/{{ ds }} /data/processed/{{ ds }} /data/model/{{ ds }}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
    )

    split = DockerOperator(
        task_id="Split_data",
        image="airflow-split",
        command="/data/processed/{{ ds }} /data/splitted/{{ ds }}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"]
    )

    train = DockerOperator(
        task_id="Train_model",
        image="airflow-train",
        command="/data/splitted/{{ ds }} /data/model/{{ ds }}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"]
    )

    validate = DockerOperator(
        task_id="Validate_model",
        image="airflow-validate",
        command="/data/splitted/{{ ds }} /data/model/{{ ds }}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"]
    )

    finish = DummyOperator(task_id="End")

    start >> [data_sensor, target_sensor] >> preprocess >> split >> train >> validate >> finish
