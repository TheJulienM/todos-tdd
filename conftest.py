import pytest

from todos import TaskManager


@pytest.fixture
def task_manager(tmp_path):
    sqlite_path = tmp_path / "tests.db"
    return TaskManager(sqlite_path)
