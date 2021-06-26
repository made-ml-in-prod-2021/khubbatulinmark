from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor

from constants import DEFAULT_ARGS, START_DATE, DATA_VOLUME_DIR, PRODICTION_MODEL, PREDICTIONS_DIR

with DAG(
        "03_predict_pipeline",
        default_args=DEFAULT_ARGS,
        schedule_interval="@daily",
        start_date=START_DATE,
) as dag:

    start = DummyOperator(task_id="Begin")

    data_sensor = FileSensor(
        task_id="Waiting_data",
        poke_interval=10,
        retries=100,
        filepath="data/raw/{{ ds }}/data.csv"
    )

    scaler_sensor = FileSensor(
        task_id="Waiting_scaler",
        poke_interval=10,
        retries=100,
        filepath=PRODICTION_MODEL + "/scaler.pkl"
    )

    model_sensor = FileSensor(
        task_id="Waiting_model",
        poke_interval=10,
        retries=100,
        filepath=PRODICTION_MODEL + "/model.pkl"
    )

    predict = DockerOperator(
        task_id="Predict",
        image="airflow-predict",
        command="data/raw/{{ ds }} " + PRODICTION_MODEL + ' ' + PREDICTIONS_DIR,
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
    )

    finish = DummyOperator(task_id="End")

    start >> [data_sensor, scaler_sensor, model_sensor] >> predict >> finish
