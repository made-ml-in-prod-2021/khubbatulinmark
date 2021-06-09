Airflow
==============================
[![python-package](https://github.com/made-ml-in-prod-2021/khubbatulinmark/actions/workflows/python-package.yml/badge.svg)](https://github.com/made-ml-in-prod-2021/khubbatulinmark/actions/workflows/python-package.yml)

## 1. Build base image
```bash
docker build airflow_ml_dags/images/airflow-ml-base/ -t airflow-ml-base:latest
```

## 2. Airflow
### Run Airflow:
```bash
docker-compose up --build
```  
Airflow address: ```http://localhost:8080/```
### Down Airflow: 
```bash
docker-compose down
```  

## 3. Testing
### Testing airflow module:
```bash
pytest -v
```  

## Evaluation criteria

| # |  | Description | Score |
| --- | --- | --- | --- |
| 0 | :ballot_box_with_check: | Поднимите airflow локально, используя docker compose (можно использовать из примера https://github.com/made-ml-in-prod-2021/airflow-examples/)  | - |
| 1 | :ballot_box_with_check: | Реализуйте dag, который генерирует данные для обучения модели (генерируйте данные, можете использовать как генератор синтетики из первой дз, так и что-то из датасетов sklearn), вам важно проэмулировать ситуации постоянно поступающих данных - записывайте данные в /data/raw/{{ ds }}/data.csv, /data/raw/{{ ds }}/target.csv | 5 |
| 2 | :ballot_box_with_check: | Реализуйте dag, который обучает модель еженедельно, используя данные за текущий день. В вашем пайплайне должно быть как минимум 4 стадии, но дайте волю своей фантазии=) | 10 |
| 3 | :ballot_box_with_check:| Реализуйте dag, который использует модель ежедневно | 5 |
| 3.1 | :ballot_box_with_check: | Реализуйте сенсоры на то, что данные готовы для дагов тренировки и обучения  | 3 |
| 4 | :ballot_box_with_check: | все даги реализованы только с помощью DockerOperator | 10 |
| 5 | :ballot_box_with_check: | Протестируйте ваши даги  | 5 |
| 6 | :black_square_button: | В docker compose так же настройте поднятие mlflow и запишите туда параметры обучения, метрики и артефакт(модель) | 5 |
| 7 | :black_square_button: | Вместо пути в airflow variables  используйте апи Mlflow Model Registry  | 5 |
| 8 | :black_square_button: | Настройте alert в случае падения дага | 3 |
| 9 | :ballot_box_with_check: | Традиционно, самооценка | 3 |
------------
