from datetime import datetime, timedelta

import pytest

from habit_tracker.data_access.data_access import DataAccess
from tests.data_fixtures import all_data


@pytest.fixture(scope="function")
def data_access_drop_init(all_data):
    """
    Fixture creates a test database and initializes it, afterwards the database tables will be dropped.
    """
    data_access = DataAccess("habit_tracker_test")
    data_access.initialize_db(all_data)
    yield data_access
    data_access.drop_tables()
    del data_access
