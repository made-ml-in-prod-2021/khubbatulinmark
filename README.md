Heart Disease UCI
==============================

Подготовка окружения: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~
Usage:
~~~
python heart_disease/train_pipeline.py -d data/raw/heart.csv -c configs/train_config.yaml
~~~
Test:
~~~
pytest tests/
~~~

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── ml_example                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- code to download or generate data
    │   │
    │   ├── features       <- code to turn raw data into features for modeling
    │   │
    │   ├── models         <- code to train models and then use trained models to make
    │   │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


Критерии оценивания
------------
Cостояние | Описание | Баллы |
--- | --- | ---
- [x] | Назовите ветку homework1 | 1
- [x] | положите код в папку src | 0
- [ ] В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, чтобы вашим ревьюерам было легче понять ваш код. (2 балла)
- [x] Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (2 баллов)
    - Вы так же можете построить в ноутбуке прототип(если это вписывается в ваш стиль работы)
    - Можете использовать не ноутбук, а скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (за это + 1 балл)
- [x]  Проект имеет модульную структуру(не все в одном файле =) ) (2 баллов)
- [x] Использованы логгеры (2 балла)
- [x] Написаны тесты на отдельные модули и на прогон всего пайплайна(3 баллов)
- [ ] Для тестов генерируются синтетические данные, приближенные к реальным (3 баллов)
    - Можно посмотреть на библиотеки https://faker.readthedocs.io/en/, https://feature-forge.readthedocs.io/en/latest/
    - Можно просто руками посоздавать данных, собственноручно написанными функциями
    - Как альтернатива, можно закоммитить файл с подмножеством трейна(это не оценивается) 
- [ ] Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3 балла)
- [x] Используются датаклассы для сущностей из конфига, а не голые dict (3 балла) 
- [ ] Используйте кастомный трансформер(написанный своими руками) и протестируйте его(3 балла)
- [ ] Обучите модель, запишите в readme как это предлагается (3 балла)
- [ ] Напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать (3 балла)  
- [ ] Используется hydra  (https://hydra.cc/docs/intro/) (3 балла - доп баллы)
- [ ] Настроен CI(прогон тестов, линтера) на основе github actions  (3 балла - доп баллы (будем проходить дальше в курсе, но если есть желание поразбираться - welcome)
- [ ] Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему (1 балл доп баллы)
------------
