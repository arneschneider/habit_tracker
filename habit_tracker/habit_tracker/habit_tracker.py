from datetime import datetime, timedelta

from habit_tracker.analytics.analytics import Analytics
from habit_tracker.data_access.data_access import DataAccess
from habit_tracker.data_access.model.habits import Habits
from habit_tracker.data_access.model.habit_model import HabitModel
from habit_tracker.data_access.model.histories import Histories
from habit_tracker.data_access.model.history_model import HistoryModel


class HabitTracker:
    """
    HabitTracker is the central entry-point containing all business logic.

    HabitTracker is the central class of the application and connects the storage and the presentation on the CLI.
    """

    def __init__(self):
        """
        Set the initial values needed.

        Constructor creates the property for the data access object.
        """
        self.__data_access = None

    @property
    def data_access(self) -> DataAccess:
        """
        Get the data access object for accessing the database.

        Returns the data access object that is the central object to interact with the database.

        Returns:
            DataAccess:
                Data access object assigned.
        """
        return self.__data_access

    @data_access.setter
    def data_access(self, data_access: DataAccess) -> None:
        """
        Set the data access object for storing habit data into a database.

        Assigns a given data access object to attribute.

        Args:
            data_access (DataAccess):
                Specific data access object to be assigned.
        """
        self.__data_access = data_access

    @classmethod
    def initial_data(cls, now) -> Habits:
        """
        Sets up initial data for predefined habits.

        A couple of habits with a couple of histories are set up and returned to be used as predefined habits.

        Args:
            now:
                The datetime as of now.

        Returns:
            Habits:
                A couple of initial habits as predefined habits.
        """
        habits = Habits()

        habit_model_work = HabitModel()
        habit_model_work.habit_id = 1
        habit_model_work.habit_name = "work"
        habit_model_work.habit_specification = "work each day"
        habit_model_work.habit_creation = now.strftime("%Y-%m-%d %H:%M:%S")
        habit_model_work.habit_periodicity_granularity = "daily"
        habit_model_work.habit_periodicity_from = now.strftime("%Y-%m-%d")
        habit_model_work.habit_periodicity_to = (now + timedelta(days=30)).strftime("%Y-%m-%d")

        histories_work = Histories()

        history_model_work_1 = HistoryModel()
        history_model_work_1.history_id = 1
        history_model_work_1.habit_id = 1
        history_model_work_1.checkoff_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        history_model_work_1.checked_off = 1

        histories_work.histories["1"] = history_model_work_1

        history_model_work_2 = HistoryModel()
        history_model_work_2.history_id = 2
        history_model_work_2.habit_id = 1
        history_model_work_2.checkoff_datetime = (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_work_2.checked_off = 1

        histories_work.histories["2"] = history_model_work_2

        history_model_work_3 = HistoryModel()
        history_model_work_3.history_id = 3
        history_model_work_3.habit_id = 1
        history_model_work_3.checkoff_datetime = (now + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_work_3.checked_off = 0

        histories_work.histories["3"] = history_model_work_3

        history_model_work_4 = HistoryModel()
        history_model_work_4.history_id = 4
        history_model_work_4.habit_id = 1
        history_model_work_4.checkoff_datetime = (now + timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_work_4.checked_off = 1

        histories_work.histories["4"] = history_model_work_4

        habit_model_work.habit_history = histories_work

        habits.habits["1"] = habit_model_work

        habit_model_walk = HabitModel()
        habit_model_walk.habit_id = 2
        habit_model_walk.habit_name = "walk"
        habit_model_walk.habit_specification = "walk each day"
        habit_model_walk.habit_creation = now.strftime("%Y-%m-%d %H:%M:%S")
        habit_model_walk.habit_periodicity_granularity = "daily"
        habit_model_walk.habit_periodicity_from = now.strftime("%Y-%m-%d")
        habit_model_walk.habit_periodicity_to = (now + timedelta(days=13)).strftime("%Y-%m-%d")

        histories_walk = Histories()

        history_model_walk_1 = HistoryModel()
        history_model_walk_1.history_id = 5
        history_model_walk_1.habit_id = 2
        history_model_walk_1.checkoff_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        history_model_walk_1.checked_off = 1

        histories_walk.histories["1"] = history_model_walk_1

        history_model_walk_2 = HistoryModel()
        history_model_walk_2.history_id = 6
        history_model_walk_2.habit_id = 2
        history_model_walk_2.checkoff_datetime = (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_walk_2.checked_off = 1

        histories_walk.histories["2"] = history_model_walk_2

        history_model_walk_3 = HistoryModel()
        history_model_walk_3.history_id = 7
        history_model_walk_3.habit_id = 2
        history_model_walk_3.checkoff_datetime = (now + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_walk_3.checked_off = 1

        histories_walk.histories["3"] = history_model_walk_3

        history_model_walk_4 = HistoryModel()
        history_model_walk_4.history_id = 8
        history_model_walk_4.habit_id = 2
        history_model_walk_4.checkoff_datetime = (now + timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_walk_4.checked_off = 1

        histories_walk.histories["4"] = history_model_walk_4

        habit_model_walk.habit_history = histories_walk

        habits.habits["2"] = habit_model_walk

        habit_model_book = HabitModel()
        habit_model_book.habit_id = 3
        habit_model_book.habit_name = "book"
        habit_model_book.habit_specification = "read a book each week"
        habit_model_book.habit_creation = now.strftime("%Y-%m-%d %H:%M:%S")
        habit_model_book.habit_periodicity_granularity = "weekly"
        habit_model_book.habit_periodicity_from = now.strftime("%Y-%m-%d")
        habit_model_book.habit_periodicity_to = (now + timedelta(weeks=13)).strftime("%Y-%m-%d")

        histories_book = Histories()

        history_model_book_1 = HistoryModel()
        history_model_book_1.history_id = 9
        history_model_book_1.habit_id = 3
        history_model_book_1.checkoff_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        history_model_book_1.checked_off = 0

        histories_book.histories["1"] = history_model_book_1

        history_model_book_2 = HistoryModel()
        history_model_book_2.history_id = 10
        history_model_book_2.habit_id = 3
        history_model_book_2.checkoff_datetime = (now + timedelta(weeks=1)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_book_2.checked_off = 1

        histories_book.histories["2"] = history_model_book_2

        history_model_book_3 = HistoryModel()
        history_model_book_3.history_id = 11
        history_model_book_3.habit_id = 3
        history_model_book_3.checkoff_datetime = (now + timedelta(weeks=2)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_book_3.checked_off = 0

        histories_book.histories["3"] = history_model_book_3

        history_model_book_4 = HistoryModel()
        history_model_book_4.history_id = 12
        history_model_book_4.habit_id = 3
        history_model_book_4.checkoff_datetime = (now + timedelta(weeks=3)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_book_4.checked_off = 1

        histories_book.histories["4"] = history_model_book_4

        habit_model_book.habit_history = histories_book

        habits.habits["3"] = habit_model_book

        habit_model_cycle = HabitModel()
        habit_model_cycle.habit_id = 4
        habit_model_cycle.habit_name = "cycle"
        habit_model_cycle.habit_specification = "cycle each week"
        habit_model_cycle.habit_creation = now.strftime("%Y-%m-%d %H:%M:%S")
        habit_model_cycle.habit_periodicity_granularity = "weekly"
        habit_model_cycle.habit_periodicity_from = now.strftime("%Y-%m-%d")
        habit_model_cycle.habit_periodicity_to = (now + timedelta(weeks=21)).strftime("%Y-%m-%d")

        histories_cycle = Histories()

        history_model_cycle_1 = HistoryModel()
        history_model_cycle_1.history_id = 13
        history_model_cycle_1.habit_id = 4
        history_model_cycle_1.checkoff_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        history_model_cycle_1.checked_off = 0

        histories_cycle.histories["1"] = history_model_cycle_1

        history_model_cycle_2 = HistoryModel()
        history_model_cycle_2.history_id = 14
        history_model_cycle_2.habit_id = 4
        history_model_cycle_2.checkoff_datetime = (now + timedelta(weeks=1)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_cycle_2.checked_off = 0

        histories_cycle.histories["2"] = history_model_cycle_2

        history_model_cycle_3 = HistoryModel()
        history_model_cycle_3.history_id = 15
        history_model_cycle_3.habit_id = 4
        history_model_cycle_3.checkoff_datetime = (now + timedelta(weeks=2)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_cycle_3.checked_off = 1

        histories_cycle.histories["3"] = history_model_cycle_3

        history_model_cycle_4 = HistoryModel()
        history_model_cycle_4.history_id = 16
        history_model_cycle_4.habit_id = 4
        history_model_cycle_4.checkoff_datetime = (now + timedelta(weeks=3)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_cycle_4.checked_off = 1

        histories_cycle.histories["4"] = history_model_cycle_4

        habit_model_cycle.habit_history = histories_cycle

        habits.habits["4"] = habit_model_cycle

        habit_model_swim = HabitModel()
        habit_model_swim.habit_id = 5
        habit_model_swim.habit_name = "swim"
        habit_model_swim.habit_specification = "swim each week"
        habit_model_swim.habit_creation = now.strftime("%Y-%m-%d %H:%M:%S")
        habit_model_swim.habit_periodicity_granularity = "weekly"
        habit_model_swim.habit_periodicity_from = now.strftime("%Y-%m-%d")
        habit_model_swim.habit_periodicity_to = (now + timedelta(weeks=4)).strftime("%Y-%m-%d")

        histories_swim = Histories()

        history_model_swim_1 = HistoryModel()
        history_model_swim_1.history_id = 17
        history_model_swim_1.habit_id = 5
        history_model_swim_1.checkoff_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        history_model_swim_1.checked_off = 1

        histories_swim.histories["1"] = history_model_swim_1

        history_model_swim_2 = HistoryModel()
        history_model_swim_2.history_id = 18
        history_model_swim_2.habit_id = 5
        history_model_swim_2.checkoff_datetime = (now + timedelta(weeks=1)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_swim_2.checked_off = 0

        histories_swim.histories["2"] = history_model_swim_2

        history_model_swim_3 = HistoryModel()
        history_model_swim_3.history_id = 19
        history_model_swim_3.habit_id = 5
        history_model_swim_3.checkoff_datetime = (now + timedelta(weeks=2)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_swim_3.checked_off = 1

        histories_swim.histories["3"] = history_model_swim_3

        history_model_swim_4 = HistoryModel()
        history_model_swim_4.history_id = 20
        history_model_swim_4.habit_id = 5
        history_model_swim_4.checkoff_datetime = (now + timedelta(weeks=3)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_swim_4.checked_off = 0

        histories_swim.histories["4"] = history_model_swim_4

        habit_model_swim.habit_history = histories_swim

        habits.habits["5"] = habit_model_swim

        habit_model_meditate = HabitModel()
        habit_model_meditate.habit_id = 6
        habit_model_meditate.habit_name = "meditate"
        habit_model_meditate.habit_specification = "meditate each day"
        habit_model_meditate.habit_creation = now.strftime("%Y-%m-%d %H:%M:%S")
        habit_model_meditate.habit_periodicity_granularity = "daily"
        habit_model_meditate.habit_periodicity_from = now.strftime("%Y-%m-%d")
        habit_model_meditate.habit_periodicity_to = (now + timedelta(days=13)).strftime("%Y-%m-%d")

        histories_meditate = Histories()

        history_model_meditate_1 = HistoryModel()
        history_model_meditate_1.history_id = 21
        history_model_meditate_1.habit_id = 6
        history_model_meditate_1.checkoff_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        history_model_meditate_1.checked_off = 1

        histories_meditate.histories["1"] = history_model_meditate_1

        history_model_meditate_2 = HistoryModel()
        history_model_meditate_2.history_id = 22
        history_model_meditate_2.habit_id = 6
        history_model_meditate_2.checkoff_datetime = (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_meditate_2.checked_off = 0

        histories_meditate.histories["2"] = history_model_meditate_2

        history_model_meditate_3 = HistoryModel()
        history_model_meditate_3.history_id = 23
        history_model_meditate_3.habit_id = 6
        history_model_meditate_3.checkoff_datetime = (now + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_meditate_3.checked_off = 0

        histories_meditate.histories["3"] = history_model_meditate_3

        history_model_meditate_4 = HistoryModel()
        history_model_meditate_4.history_id = 24
        history_model_meditate_4.habit_id = 6
        history_model_meditate_4.checkoff_datetime = (now + timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_meditate_4.checked_off = 0

        histories_meditate.histories["4"] = history_model_meditate_4

        habit_model_meditate.habit_history = histories_meditate

        habits.habits["6"] = habit_model_meditate

        habit_model_phone = HabitModel()
        habit_model_phone.habit_id = 7
        habit_model_phone.habit_name = "phone"
        habit_model_phone.habit_specification = "call friends each day"
        habit_model_phone.habit_creation = now.strftime("%Y-%m-%d %H:%M:%S")
        habit_model_phone.habit_periodicity_granularity = "daily"
        habit_model_phone.habit_periodicity_from = now.strftime("%Y-%m-%d")
        habit_model_phone.habit_periodicity_to = (now + timedelta(days=90)).strftime("%Y-%m-%d")

        histories_phone = Histories()

        history_model_phone_1 = HistoryModel()
        history_model_phone_1.history_id = 25
        history_model_phone_1.habit_id = 7
        history_model_phone_1.checkoff_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        history_model_phone_1.checked_off = 1

        histories_phone.histories["1"] = history_model_phone_1

        history_model_phone_2 = HistoryModel()
        history_model_phone_2.history_id = 26
        history_model_phone_2.habit_id = 7
        history_model_phone_2.checkoff_datetime = (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_phone_2.checked_off = 1

        histories_phone.histories["2"] = history_model_phone_2

        history_model_phone_3 = HistoryModel()
        history_model_phone_3.history_id = 27
        history_model_phone_3.habit_id = 7
        history_model_phone_3.checkoff_datetime = (now + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_phone_3.checked_off = 1

        histories_phone.histories["3"] = history_model_phone_3

        history_model_phone_4 = HistoryModel()
        history_model_phone_4.history_id = 28
        history_model_phone_4.habit_id = 7
        history_model_phone_4.checkoff_datetime = (now + timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
        history_model_phone_4.checked_off = 0

        histories_phone.histories["4"] = history_model_phone_4

        habit_model_phone.habit_history = histories_phone

        habits.habits["7"] = habit_model_phone

        return habits

    def initialize_db(self) -> None:
        """
        Execute the initialization of the database.

        Calls the database initialization of the data access object.
        """
        self.__data_access.initialize_db(HabitTracker.initial_data(datetime.now()))

    def create_new_habit(self, name: str, description: str, period: str, habit_from: str, habit_to: str) -> int:
        """
        Executes the creation of a new habit in the database.

        Calls the database method to create a new habit in the database.

        Args:
            name (str):
                Name of the new habit.
            description (str):
                Description of the new habit.
            period (str):
                Periodicity of the new habit.
            habit_from (str):
                Start date of the habit.
            habit_to (str):
                End date of the habit.

        Returns:
            int: ID of the newly created habit entry.
        """
        return self.__data_access.create_new_habit(name, description, period, habit_from, habit_to)

    def delete_habit(self, habit_id: int) -> None:
        """
        Executes the deletion of a habit in the database.

        Calls the database method to delete a habit from the database.

        Args:
            habit_id (int):
                ID of a habit to be deleted.
        """
        self.__data_access.delete_habit(habit_id)

    def modify_habit(self, habit_id: int, name, description, period, habit_from, habit_to) -> int:
        """
        Executes the modification of a habit in the database.

        Calls the database method to modify a habit from the database.

        Args:
            habit_id (int):
                ID of a habit to be modified.
            name (str):
                Name of the habit to be modified.
            description (str):
                Description of the habit to be modified.
            period (str):
                Periodicity of the habit to be modified.
            habit_from (str):
                Start date of the habit.
            habit_to (str):
                End date of the habit.

        Returns:
            int:
                ID of modified habit.
        """
        return self.__data_access.modify_habit(habit_id, name, description, period, habit_from, habit_to)

    def complete_habit(self, habit_id: int) -> int:
        """
        Set last habit to be completed or broken.

        Calls the database method to complete or break a habit in the database.

        Args:
            habit_id (int):
                ID of a habit to be modified.
        Returns:
            int:
                ID of the newly created histories entry.
        """
        return self.__data_access.complete_habit(habit_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def show_all_habits(self) -> Habits:
        """
        List all habits in the database.s

        Get all habits that are stored in the database at the moment.

        Returns:
            Habits:
                Dictionary containing all habits in the database.
        """
        return self.__data_access.get_all_habits()

    def show_all_habits_by_periodicity(self, periodicity: str) -> Habits:
        """
        Get a dictionary of habit models with habits that have a specific periodicity.

        Retrieves habits with a specific periodicity from the database and puts them into a Habits.

        Args:
            periodicity (str):
                Periodicity of the habits to be listed.

        Returns:
            Habits:
                A dictionary of habit models with a specific periodicity.
        """
        return self.__data_access.get_all_habits_by_periodicity(periodicity)

    def calc_longest_run_streak(self) -> int:
        """
        Determine the longest streak over all habits in the database.

        Retrieves habits from the database and puts them into a Habits.

        Returns:
            int:
                Longest run streak over all habits.
        """
        habits = self.__data_access.get_all_habits()
        longest_streak = Analytics.calc_longest_run_streak(habits)
        return longest_streak

    def calc_longest_run_streak_by_periodicity(self, periodicity: str) -> int:
        """
        Determine the longest streak over all habits with a specific periodicity in the database.

        Retrieves habits with a specific periodicity from the database and puts them into a Habits.

        Args:
            periodicity (str):
                Periodicity of the habits for which the longest streak is to be calculated.

        Returns:
            int:
                Longest run streak over all habits given the periodicity.
        """
        habits = self.__data_access.get_all_habits_by_periodicity(periodicity)
        longest_streak = Analytics.calc_longest_run_streak(habits)
        return longest_streak

    def calc_longest_run_streak_of_habit(self, habit_id: int) -> int:
        """
        Determine the longest streak over all habits in the database.

        Retrieves habits with a specific periodicity from the database and puts them into a Habits.

        Args:
            habit_id (int):
                ID of the habit for which the longest streak is to be calculated.

        Returns:
            int:
                Longest run streak over a habit given.
        """
        habit_model = self.__data_access.get_habit_by_id(habit_id)
        longest_streak = Analytics.calc_longest_run_streak_of_habit(habit_model)
        return longest_streak
