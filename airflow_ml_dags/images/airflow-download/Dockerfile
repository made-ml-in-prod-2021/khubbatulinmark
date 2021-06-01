FROM python:3.7-slim-buster

RUN pip install --no-cache-dir scikit-learn pandas kaggle

COPY download.py /download.py

ENTRYPOINT ["python", "download.py"]