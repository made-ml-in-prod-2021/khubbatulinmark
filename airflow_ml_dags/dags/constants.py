import datetime

from airflow.models import Variable
from airflow.utils.dates import days_ago


DEFAULT_ARGS = {
    "owner": "KhubbatulinM",
    "email": ["khubbatulin@gmail.com"],
    "email_on_failure": True,
    'email_on_retry': False,
    "retries": 3,
    "retry_delay": datetime.timedelta(minutes=1),
}
START_DATE = days_ago(5)
DATA_VOLUME_DIR = Variable.get("data_path")


KAGGLE_USERNAME = Variable.get("kaggle_username")
KAGGLE_KEY = Variable.get("kaggle_key")


MODEL_PATH = Variable.get("model_path")
PRODICTION_MODEL = Variable.get('prod_dir')

RAW_DATA_DIR = "/data/raw/{{ ds }}"
PROCESSED_DATA_DIR = "/data/processed/{{ ds }}"
SPLITTING_DATA_DIR = "/data/processed/{{ ds }}"
MODEL_DIR = "/data/models/{{ ds }}"

PREDICTIONS_DIR = "/data/predictions/{{ ds }}"
