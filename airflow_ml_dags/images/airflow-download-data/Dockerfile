FROM airflow-ml-base:latest
RUN pip install --no-cache-dir kaggle
COPY download.py /download.py
ENTRYPOINT ["python", "download.py"]