import pytest

from todos import TaskManager


@pytest.fixture
def task_manager(tmp_path):
    res = TaskManager(repository_path=tmp_path / "tasks.pickle")
    yield res
