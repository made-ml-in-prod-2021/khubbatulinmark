Heart Disease UCI
==============================

## Data

Download [data](https://www.kaggle.com/ronitf/heart-disease-uci) and extract into folder `data/raw`

```bash
mkdir -p data/raw && unzip archive.zip -d data/raw
```

## Installation 
~~~
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~

## Make Report 
~~~
python heart_disease/make_report.py -d data/raw/heart.csv -o reports/data_report.html
~~~

## Train
#### Logistic Regression
~~~
python src/train_pipeline.py -c configs/train_config_log_reg.yaml
~~~
#### Random forest
~~~
python src/train_pipeline.py -c configs/train_config_rf.yaml
~~~
## Test:
~~~
pytest tests/
~~~

## Project Organization


    ├── configs            <- Configuration files
    ├── data               <- All datasets and data for project
    │   └── raw                 <- The original, immutable data dump.
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py         <- Makes src a Python module
    │   ├── data                <- Code to download or generate data
    │   ├── entities            <- Configuration ORM entities
    │   ├── features            <- Code to turn raw data into features for modeling
    │   ├── models              <- Code to train models and then use trained models to make
    │   ├── make_report.py      <- Script for report generation
    │   └── train_pipeline.py   <- Script for training model
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks.
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    ├── tests              <- unit & intagration tests
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.│
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


## Evaluation criteria

| # |  | Description | Score |
| --- | --- | --- | --- |
| -2 | :ballot_box_with_check: | Назовите ветку homework1 | 1 |
| -1 | :ballot_box_with_check: | Положите код в папку heart_disease | - |
| 0 | :ballot_box_with_check: | В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, чтобы вашим ревьюерам было легче понять ваш код | 2 |
| 1 | :ballot_box_with_check:| Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (2 баллов) Вы так же можете построить в ноутбуке прототип(если это вписывается в ваш стиль работы) Можете использовать не ноутбук, а скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (за это + 1 балл) | 3 |
| 2 | :ballot_box_with_check: | Проект имеет модульную структуру(не все в одном файле =) ) (2 баллов) | 2 |
| 3 | :ballot_box_with_check: | Использованы логгеры (2 балла) | 3 |
| 4 | :black_square_button: | Написаны тесты на отдельные модули и на прогон всего пайплайна(3 баллов) | 3 |
| 5 | :black_square_button: | Для тестов генерируются синтетические данные, приближенные к реальным (3 баллов) | 3 |
| 6 | :black_square_button: | Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3 балла) | 3 | 
| 7 | :ballot_box_with_check: | Используются датаклассы для сущностей из конфига, а не голые dict (3 балла) | 3 |
| 8 | :black_square_button: | Используйте кастомный трансформер(написанный своими руками) и протестируйте его(3 балла) | 3 |
| 9 | :black_square_button: | Обучите модель, запишите в readme как это предлагается (3 балла) | 3 |
| 10 | :black_square_button: |Напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать (3 балла) | 3 |
| 11 | :black_square_button: | Используется hydra  (https://hydra.cc/docs/intro/) (3 балла - доп баллы) | 3 |
| 12 | :black_square_button: | Настроен CI(прогон тестов, линтера) на основе github actions  (3 балла - доп баллы (будем проходить дальше в курсе, но если есть желание поразбираться - welcome) | 3 | 
| 13 | :ballot_box_with_check: | Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему (1 балл доп баллы) | 1 |
------------

