
import pytest

from habit_tracker.habit_tracker.habit_tracker import HabitTracker
from tests.data_fixtures import all_data, now
from tests.db_fixtures import data_access_drop_init


def test_calc_longest_run_streak(data_access_drop_init):
    """
    Asserts that longest run streak of all habits is calculated correctly.
    """
    expected_longest_streak = 4
    habit_tracker = HabitTracker()
    habit_tracker.data_access = data_access_drop_init
    actual_longest_streak = habit_tracker.calc_longest_run_streak()
    assert actual_longest_streak == expected_longest_streak, \
        "Longest run streak is not calculated correctly."


def test_calc_longest_run_streak_by_periodicity_check_daily(data_access_drop_init):
    """
    Asserts that longest run streak of all daily habits is calculated correctly.
    """
    expected_longest_streak = 4
    habit_tracker = HabitTracker()
    habit_tracker.data_access = data_access_drop_init
    actual_longest_streak = habit_tracker.calc_longest_run_streak_by_periodicity("daily")
    assert actual_longest_streak == expected_longest_streak, \
        "Longest run streak is not calculated correctly."


def test_calc_longest_run_streak_by_periodicity_check_weekly(data_access_drop_init):
    """
    Asserts that longest run streak of all weekly habits is calculated correctly.
    """
    expected_longest_streak = 2
    habit_tracker = HabitTracker()
    habit_tracker.data_access = data_access_drop_init
    actual_longest_streak = habit_tracker.calc_longest_run_streak_by_periodicity("weekly")
    assert actual_longest_streak == expected_longest_streak, \
        "Longest run streak is not calculated correctly."


def test_calc_longest_run_streak_of_habit(data_access_drop_init):
    """
    Asserts that longest run streak of a specific habit is calculated correctly.
    """
    expected_longest_streak = 2
    habit_id = 1
    habit_tracker = HabitTracker()
    habit_tracker.data_access = data_access_drop_init
    actual_longest_streak = habit_tracker.calc_longest_run_streak_of_habit(habit_id)
    assert actual_longest_streak == expected_longest_streak, \
        "Longest run streak is not calculated correctly."
