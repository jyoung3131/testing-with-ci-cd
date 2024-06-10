import pytest

@pytest.fixture(scope="function")
def some_grades():
    return [90, 80, 70]

