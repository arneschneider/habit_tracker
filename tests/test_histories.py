
from habit_tracker.data_access.model.histories import Histories
from tests.data_fixtures import histories_work, now


def test_transform_to_list(histories_work):
    """
    Asserts that a couple of histories can be transformed into a list of zeros and ones.
    """
    expected_history_list = [1, 1, 0, 1]
    actual_history_list = histories_work.transform_to_list()
    assert actual_history_list == expected_history_list, \
        "Transformed histories is not as expected."
