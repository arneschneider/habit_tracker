
import pytest

from habit_tracker.analytics.analytics import Analytics
from habit_tracker.data_access.data_access import DataAccess
from habit_tracker.data_access.model.habit_model import HabitModel
from tests.data_fixtures import all_data, habit_model_work, now


@pytest.mark.parametrize(
    'run_streak, expected_longest_streak', [
        ([], 0),
        ([0], 0),
        ([1], 1),
        ([1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 4)
    ]
)
def test_length_longest_run_streak(run_streak, expected_longest_streak):
    """
    Asserts that determining the longest run streak given a list of zeros and ones works.
    """
    actual_longest_streak = Analytics.length_longest_run_streak(run_streak)
    assert actual_longest_streak == expected_longest_streak, \
        "Calculated longest run streak is not as expected."


def test_calc_longest_run_streak_of_habit(habit_model_work):
    """
    Asserts that determining the longest run streak given a specific habit model works.
    """
    expected_longest_streak = 2
    actual_longest_streak = Analytics.calc_longest_run_streak_of_habit(habit_model_work)
    assert actual_longest_streak == expected_longest_streak, \
        "Calculated longest run streak is not as expected."


def test_calc_longest_run_streak(all_data):
    """
    Asserts that determining the longest run streak given a habit dictionary works.
    """
    expected_longest_streak = 4
    actual_longest_streak = Analytics.calc_longest_run_streak(all_data)
    assert actual_longest_streak == expected_longest_streak, \
        "Calculated longest run streak is not as expected."
