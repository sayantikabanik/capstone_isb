from analysis_framework.pipeline import process
from dagster import execute_pipeline


def test_process():
    """
    test to check if pipeline runs successfully
    """
    result = execute_pipeline(process)
    assert result.success
