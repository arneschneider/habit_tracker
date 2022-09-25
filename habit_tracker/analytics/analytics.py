
from itertools import groupby
from typing import List

from habit_tracker.data_access.model.habits import Habits
from habit_tracker.data_access.model.habit_model import HabitModel


class Analytics:
    """
    Analytics contains the logic to determine the longest streak given a list of zeros and ones.

    The longest streak given a list of zeros and ones is determined with the functional programming paradigm.
    """

    def __init__(self):
        """
        Empty constructor.
        """
        pass

    @classmethod
    def calc_longest_run_streak(cls, habits: Habits) -> int:
        """
        Determine the longest streak over all habits given.

        Calculate the longest run streak of all habits given.

        Args:
            habits (Habits):
                Dictionary of habit models to be analysed.

        Returns:
            int:
                Longest run streak over all given habits.
        """
        length_longest_run_streak = list()
        for habit_model in habits.habits.values():
            length_longest_run_streak.append(Analytics.calc_longest_run_streak_of_habit(habit_model))
        if len(length_longest_run_streak) > 0:
            return max(length_longest_run_streak)
        else:
            return 0

    @classmethod
    def calc_longest_run_streak_of_habit(cls, habit_model: HabitModel) -> int:
        """
        Determine the longest streak of a habit given.

        Calculate the longest run streak of a habit.

        Args:
            habit_model (HabitModel):
                Habit model to be analysed.

        Returns:
            int:
                Longest run streak of a habit.
        """
        return Analytics.length_longest_run_streak(habit_model.habit_history.transform_to_list())

    @classmethod
    def length_longest_run_streak(cls, history: List[int]) -> int:
        """
        Determine the longest streak of a list of zeros and ones.

        Calculate the longest run streak of a list of zeros and ones.

        Args:
            history (List[int]):
                History of a habit as a list of zeros and ones for which to determine the longest run streak.

        Returns:
            int:
                Longest run streak of a list of zeros and ones.
        """
        return max([len(list(group)) for value, group in groupby(history) if value == 1], default=0)
