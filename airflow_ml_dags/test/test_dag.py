import sys
import pytest
from airflow.models import DagBag

sys.path.append("dags")


@pytest.fixture()
def dag_bag():
    return DagBag(dag_folder="dags/", include_examples=False)


def test_dag_bag_import(dag_bag):
    assert dag_bag.dags is not None
    assert dag_bag.import_errors == {}


def test_dag_generate_data_load(dag_bag):
    assert "1_generate_data" in dag_bag.dags
    assert len(dag_bag.dags["01_data_download"].tasks) == 3


def test_dag_train_pipeline_load(dag_bag):
    assert "2_train_pipeline" in dag_bag.dags
    assert len(dag_bag.dags["02_train_pipeline"].tasks) == 8


def test_dag_predict_pipeline_load(dag_bag):
    assert "3_predict_pipeline" in dag_bag.dags
    assert len(dag_bag.dags["03_predict_pipeline"].tasks) == 6


def test_dag_generate_data_structure(dag_bag):
    structure = {
        "Begin": ["Download-data"],
        "Download-data": ["End"],
        "End": [],
    }
    dag = dag_bag.dags["01_data_download"]
    for name, task in dag.task_dict.items():
        assert set(structure[name]) == task.downstream_task_ids


def test_dag_train_pipeline_structure(dag_bag):
    structure = {
        "Begin": ["Waiting_data", "Waiting_target"],
        "Waiting_data": ["Preprocess"],
        "Waiting_target": ["Preprocess"],
        "Preprocess": ["Split"],
        "Split": ["Train"],
        "Train": ["Validate"],
        "Validate": ["End"],
        "End": [],
    }
    dag = dag_bag.dags["02_train_pipeline"]
    for name, task in dag.task_dict.items():
        assert set(structure[name]) == task.downstream_task_ids


def test_dag_predict_pipeline_structure(dag_bag):
    structure = {
        "Begin": ["Waiting_data", "Waiting_scaler", "Waiting_model"],
        "Wait_for_data": ["Predict"],
        "Wait_for_scaler": ["Predict"],
        "Wait_for_model": ["Predict"],
        "Predict": ["End"],
        "End": [],
    }
    dag = dag_bag.dags["03_predict_pipeline"]
    for name, task in dag.task_dict.items():
        assert set(structure[name]) == task.downstream_task_ids
