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
