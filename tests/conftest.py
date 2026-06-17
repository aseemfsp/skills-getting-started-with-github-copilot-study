from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


BASELINE_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange test isolation by restoring the in-memory store before each test.
    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app_module.app)
