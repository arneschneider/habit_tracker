
from datetime import datetime, timedelta

import pytest

from habit_tracker.data_access.model.habit_model import HabitModel
from habit_tracker.data_access.model.history_model import HistoryModel
from tests.data_fixtures import all_data, now
from tests.db_fixtures import data_access_drop_init


@pytest.fixture(scope="function", params=[
    1,
    2,
    3
])
def habit_model(request, data_access_drop_init):
    """
    Fixture fetches habit models with specific IDs, while database tables are deleted and initialized again beforehand.
    """
    expected_habit_id = request.param
    habit_model = data_access_drop_init.get_habit_by_id(habit_id=expected_habit_id)
    yield habit_model, expected_habit_id
    del habit_model


@pytest.fixture(scope="function", params=[
    1,
    2,
    3
])
def history_model(request, data_access_drop_init):
    """
    Fixture fetches history models with specific IDs, while database tables are deleted and initialized beforehand.
    """
    expected_history_id = request.param
    history_model = data_access_drop_init.get_history_by_id(history_id=expected_history_id)
    yield history_model, expected_history_id
    del history_model


@pytest.fixture(scope="function", params=[
    1
])
def histories(request, data_access_drop_init):
    """
    Fixture fetches history models with specific IDs, while database tables are deleted and initialized beforehand.
    """
    expected_habit_id = request.param
    histories = data_access_drop_init.get_histories_by_habit_id(habit_id=expected_habit_id)
    yield histories
    del histories


@pytest.fixture(scope="function")
def habits_all(data_access_drop_init):
    """
    Fixture fetches all habit models, while database tables are deleted and initialized beforehand.
    """
    habits = data_access_drop_init.get_all_habits()
    yield habits
    del habits


@pytest.fixture(scope="function")
def habits_daily(data_access_drop_init):
    """
    Fixture fetches all daily habit models, while database tables are deleted and initialized beforehand.
    """
    habits = data_access_drop_init.get_all_habits_by_periodicity("daily")
    yield habits
    del habits


@pytest.fixture(scope="function")
def habits_weekly(data_access_drop_init):
    """
    Fixture fetches all weekly habit models, while database tables are deleted and initialized beforehand.
    """
    habits = data_access_drop_init.get_all_habits_by_periodicity("weekly")
    yield habits
    del habits


@pytest.mark.parametrize(
    'table_name, expected_number_entries', [
        ("habits", 7),
        ("histories", 28)
    ]
)
def test_init_db(data_access_drop_init, table_name, expected_number_entries) -> None:
    """
    Asserts that initializing the database works.
    """
    result = data_access_drop_init.cursor.execute(f"SELECT * FROM {table_name};")
    actual_number_entries = len(result.fetchall())
    assert actual_number_entries == expected_number_entries, \
        "Number of table entries is different to expected number of table entries."


def test_get_habit(habit_model):
    """
    Asserts that fetching a particular habit from database returns the correct habit with the correct habit ID.
    """
    model, expected_habit_id = habit_model
    actual_habit_id = model.habit_id
    assert actual_habit_id == expected_habit_id, \
        "Habit ID is different to expected ID."


def test_get_history_by_id(history_model):
    """
    Asserts that fetching a particular history from database returns the correct history with the correct history ID.
    """
    model, expected_history_id = history_model
    actual_history_id = model.history_id
    assert actual_history_id == expected_history_id, \
        "History ID is different to expected ID."


def test_get_histories_by_habit_id_check_size(histories):
    """
    Asserts that fetching a particular history dictionary from database returns the correct history dictionary.
    """
    expected_size_of_histories = 4
    actual_size_of_histories = len(histories.histories)
    assert actual_size_of_histories == expected_size_of_histories, \
        "Size of history dict is different to expected size of history dict."


def test_get_histories_by_habit_id_check_first_id(histories):
    """
    Asserts that fetching a particular history dictionary from database returns the correct history dictionary.
    """
    expected_history_id = 1
    habit_id = "1"
    actual_history_id = histories.histories[habit_id].history_id
    assert actual_history_id == expected_history_id, \
        "History ID is different to expected ID."


def test_get_all_habits_check_size(habits_all):
    """
    Asserts that fetching all habits from database returns the correct habit dictionary.
    """
    expected_size_of_habits = 7
    actual_size_of_habits = len(habits_all.habits)
    assert actual_size_of_habits == expected_size_of_habits, \
        "Size of habit dict is different to expected size of habit dict."


def test_get_all_habits_check_first_id(habits_all):
    """
    Asserts that fetching a particular history dictionary from database returns the correct history dictionary.
    """
    expected_habit_id = 1
    habit_id = "1"
    actual_habit_id = habits_all.habits[habit_id].habit_id
    assert actual_habit_id == expected_habit_id, \
        "Habit ID is different to expected ID."


def test_get_all_habits_by_periodicity_check_daily(habits_daily):
    """

    """
    expected_habit_id = 1
    habit_id = "1"
    actual_habit_id = habits_daily.habits[habit_id].habit_id
    assert actual_habit_id == expected_habit_id, \
        "Habit ID is different to expected ID."


def test_get_all_habits_by_periodicity_check_weekly(habits_weekly):
    """

    """
    expected_habit_id = 3
    habit_id = "3"
    actual_habit_id = habits_weekly.habits[habit_id].habit_id
    assert actual_habit_id == expected_habit_id, \
        "Habit ID is different to expected ID."


def test_create_new_habit(data_access_drop_init):
    """
    Asserts that creating a new habit stores the habit correctly into the database.
    """
    expected_name = "test_name"
    expected_description = "test_description"
    expected_period = "daily"
    expected_habit_from = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_habit_to = (datetime.now() + timedelta(days=6)).strftime("%Y-%m-%d %H:%M:%S")
    expected_habit_id = data_access_drop_init.create_new_habit(expected_name,
                                                               expected_description,
                                                               expected_period,
                                                               expected_habit_from,
                                                               expected_habit_to)
    habit_model = data_access_drop_init.get_habit_by_id(habit_id=expected_habit_id)
    actual_habit_id = habit_model.habit_id
    data_access_drop_init.delete_habit(expected_habit_id)
    assert actual_habit_id == expected_habit_id, \
        "Habit ID is different to expected ID."


def test_delete_habit(data_access_drop_init):
    """
    Asserts that deleting a habit from the database works.
    """
    expected_name = "test_name"
    expected_description = "test_description"
    expected_period = "daily"
    expected_habit_from = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_habit_to = (datetime.now() + timedelta(days=6)).strftime("%Y-%m-%d %H:%M:%S")
    expected_habit_id = data_access_drop_init.create_new_habit(expected_name,
                                                               expected_description,
                                                               expected_period,
                                                               expected_habit_from,
                                                               expected_habit_to)
    data_access_drop_init.delete_habit(expected_habit_id)
    with pytest.raises(NameError) as error_info:
        data_access_drop_init.get_habit_by_id(habit_id=expected_habit_id)
    assert "Habit ID does not exist." in str(error_info.value), \
        "Habit is not properly deleted from database."


def test_modify_habit(data_access_drop_init):
    """
    Asserts that modifying a habit in the database works.
    """
    name = "test_name"
    description = "test_description"
    period = "daily"
    habit_from = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    habit_to = (datetime.now() + timedelta(days=6)).strftime("%Y-%m-%d %H:%M:%S")
    expected_habit_id = data_access_drop_init.create_new_habit(name,
                                                               description,
                                                               period,
                                                               habit_from,
                                                               habit_to)
    expected_name = "test_name_new"
    expected_description = "test_description_new"
    expected_period = "weekly"
    expected_habit_from = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    expected_habit_to = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    data_access_drop_init.modify_habit(expected_habit_id,
                                       expected_name,
                                       expected_description,
                                       expected_period,
                                       expected_habit_from,
                                       expected_habit_to)
    habit_model = data_access_drop_init.get_habit_by_id(habit_id=expected_habit_id)
    actual_habit_name = habit_model.habit_name
    data_access_drop_init.delete_habit(expected_habit_id)
    assert actual_habit_name == expected_name, \
        "Habit name is different to expected name."


@pytest.mark.parametrize(
    'now_datetime, checkoff_datetime_delta, period, expected_number_broken', [
        (datetime.now(), timedelta(days=2), "daily", 1),
        (datetime.now(), timedelta(days=3), "daily", 2),
        (datetime.now(), timedelta(days=4), "daily", 3),
        (datetime.now(), timedelta(days=5), "daily", 4)
    ]
)
def test_complete_habit_check_daily_with_one_completed(
        data_access_drop_init, now_datetime, checkoff_datetime_delta, period, expected_number_broken
):
    """
    Asserts that checking off a daily habit in the database works.
    """
    expected_name = "test_name"
    expected_description = "test_description"
    expected_period = period
    habit_from = now_datetime + timedelta(days=1)
    expected_checked_off = now_datetime + checkoff_datetime_delta
    expected_habit_from = habit_from.strftime("%Y-%m-%d")
    diff = expected_checked_off - habit_from
    number_diff_days = diff.days
    expected_habit_to = (habit_from + timedelta(days=6)).strftime("%Y-%m-%d")
    expected_habit_id = data_access_drop_init.create_new_habit(expected_name,
                                                               expected_description,
                                                               expected_period,
                                                               expected_habit_from,
                                                               expected_habit_to)
    expected_last_history_id = data_access_drop_init.complete_habit(expected_habit_id,
                                                                    expected_checked_off.strftime("%Y-%m-%d %H:%M:%S"))
    assert expected_last_history_id > 0, \
        "Habit was not checked off."
    habit_model = data_access_drop_init.get_habit_by_id(habit_id=expected_habit_id)
    actual_last_history_id = list(habit_model.habit_history.histories.keys())[-1]
    data_access_drop_init.delete_habit(expected_habit_id)
    assert int(actual_last_history_id) == expected_last_history_id, \
        "History ID is different to expected ID."
    actual_number_broken = 0
    if number_diff_days > 0:
        actual_number_broken = number_diff_days
    assert actual_number_broken == expected_number_broken, \
        "Number of broken history entries is not correct."


@pytest.mark.parametrize(
    'now_datetime, checkoff_datetime_delta, period, expected_number_broken', [
        (datetime.now(), timedelta(days=2), "daily", 0),
        (datetime.now(), timedelta(days=3), "daily", 1),
        (datetime.now(), timedelta(days=4), "daily", 2),
        (datetime.now(), timedelta(days=5), "daily", 3)
    ]
)
def test_complete_habit_check_daily_with_two_completed(
        data_access_drop_init, now_datetime, checkoff_datetime_delta, period, expected_number_broken
):
    """
    Asserts that checking off a daily habit in the database works.
    """
    expected_name = "test_name"
    expected_description = "test_description"
    expected_period = period
    habit_from = now_datetime + timedelta(days=1)
    expected_checked_off = now_datetime + checkoff_datetime_delta
    first_checked_off = habit_from
    expected_habit_from = habit_from.strftime("%Y-%m-%d")
    expected_habit_to = (habit_from + timedelta(days=6)).strftime("%Y-%m-%d")
    expected_habit_id = data_access_drop_init.create_new_habit(expected_name,
                                                               expected_description,
                                                               expected_period,
                                                               expected_habit_from,
                                                               expected_habit_to)
    data_access_drop_init.complete_habit(expected_habit_id, first_checked_off.strftime("%Y-%m-%d %H:%M:%S"))
    expected_last_history_id = data_access_drop_init.complete_habit(expected_habit_id,
                                                                    expected_checked_off.strftime("%Y-%m-%d %H:%M:%S"))
    assert expected_last_history_id > 0, \
        "Habit was not checked off."
    habit_model = data_access_drop_init.get_habit_by_id(habit_id=expected_habit_id)
    actual_last_history_id = list(habit_model.habit_history.histories.keys())[-1]
    data_access_drop_init.delete_habit(expected_habit_id)
    assert int(actual_last_history_id) == expected_last_history_id, \
        "History ID is different to expected ID."
    actual_number_broken = 0
    histories = habit_model.habit_history.histories
    if len(histories) > 1:
        histories_keys_reversed = reversed(histories)
        first_skipped = False
        for history_id in histories_keys_reversed:
            if not first_skipped:
                first_skipped = True
                continue
            if histories[history_id].checked_off == 0:
                actual_number_broken += 1
            else:
                break
    assert actual_number_broken == expected_number_broken, \
        "Number of broken history entries is not correct."


@pytest.mark.parametrize(
    'now_datetime, checkoff_datetime_delta, period, expected_number_broken', [
        (datetime.now(), timedelta(weeks=0, days=1), "weekly", 0),
        (datetime.now(), timedelta(weeks=1, days=1), "weekly", 1),
        (datetime.now(), timedelta(weeks=2, days=1), "weekly", 2),
        (datetime.now(), timedelta(weeks=3, days=1), "weekly", 3),
        (datetime.now(), timedelta(weeks=4, days=1), "weekly", 4)
    ]
)
def test_complete_habit_check_weekly_with_one_completed(
        data_access_drop_init, now_datetime, checkoff_datetime_delta, period, expected_number_broken
):
    """
    Asserts that checking off a weekly habit in the database works.
    """
    expected_name = "test_name"
    expected_description = "test_description"
    expected_period = period
    habit_from = now_datetime + timedelta(days=1)
    expected_checked_off = now_datetime + checkoff_datetime_delta
    expected_habit_from = habit_from.strftime("%Y-%m-%d")
    diff = expected_checked_off - habit_from
    number_weeks = int(diff.days / 7.0)
    expected_habit_to = (habit_from + timedelta(weeks=6)).strftime("%Y-%m-%d")
    expected_habit_id = data_access_drop_init.create_new_habit(expected_name,
                                                               expected_description,
                                                               expected_period,
                                                               expected_habit_from,
                                                               expected_habit_to)
    expected_last_history_id = data_access_drop_init.complete_habit(expected_habit_id,
                                                                    expected_checked_off.strftime("%Y-%m-%d %H:%M:%S"))
    assert expected_last_history_id > 0, \
        "Habit was not checked off."
    habit_model = data_access_drop_init.get_habit_by_id(habit_id=expected_habit_id)
    actual_last_history_id = list(habit_model.habit_history.histories.keys())[-1]
    data_access_drop_init.delete_habit(expected_habit_id)
    assert int(actual_last_history_id) == expected_last_history_id, \
        "History ID is different to expected ID."
    actual_number_broken = 0
    if number_weeks > 0:
        actual_number_broken = number_weeks
    assert actual_number_broken == expected_number_broken, \
        "Number of broken history entries is not correct."


@pytest.mark.parametrize(
    'now_datetime, checkoff_datetime_delta, period, expected_number_broken', [
        (datetime.now(), timedelta(weeks=1, days=1), "weekly", 0),
        (datetime.now(), timedelta(weeks=2, days=1), "weekly", 1),
        (datetime.now(), timedelta(weeks=3, days=1), "weekly", 2),
        (datetime.now(), timedelta(weeks=4, days=1), "weekly", 3)
    ]
)
def test_complete_habit_check_weekly_with_two_completed(
        data_access_drop_init, now_datetime, checkoff_datetime_delta, period, expected_number_broken
):
    """
    Asserts that checking off a weekly habit in the database works.
    """
    expected_name = "test_name"
    expected_description = "test_description"
    expected_period = period
    habit_from = now_datetime + timedelta(days=1)
    first_checked_off = habit_from
    expected_checked_off = now_datetime + checkoff_datetime_delta
    expected_habit_from = habit_from.strftime("%Y-%m-%d")
    expected_habit_to = (habit_from + timedelta(weeks=6)).strftime("%Y-%m-%d")
    expected_habit_id = data_access_drop_init.create_new_habit(expected_name,
                                                               expected_description,
                                                               expected_period,
                                                               expected_habit_from,
                                                               expected_habit_to)
    data_access_drop_init.complete_habit(expected_habit_id, first_checked_off.strftime("%Y-%m-%d %H:%M:%S"))
    expected_last_history_id = data_access_drop_init.complete_habit(expected_habit_id,
                                                                    expected_checked_off.strftime("%Y-%m-%d %H:%M:%S"))
    assert expected_last_history_id > 0, \
        "Habit was not checked off."
    habit_model = data_access_drop_init.get_habit_by_id(habit_id=expected_habit_id)
    actual_last_history_id = list(habit_model.habit_history.histories.keys())[-1]
    data_access_drop_init.delete_habit(expected_habit_id)
    assert int(actual_last_history_id) == expected_last_history_id, \
        "History ID is different to expected ID."
    actual_number_broken = 0
    histories = habit_model.habit_history.histories
    if len(histories) > 1:
        histories_keys_reversed = reversed(histories)
        first_skipped = False
        for history_id in histories_keys_reversed:
            if not first_skipped:
                first_skipped = True
                continue
            if histories[history_id].checked_off == 0:
                actual_number_broken += 1
            else:
                break
    assert actual_number_broken == expected_number_broken, \
        "Number of broken history entries is not correct."
