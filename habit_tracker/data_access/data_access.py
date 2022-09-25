import sqlite3
from datetime import datetime, timedelta

from habit_tracker.data_access.model.habits import Habits
from habit_tracker.data_access.model.habit_model import HabitModel
from habit_tracker.data_access.model.histories import Histories
from habit_tracker.data_access.model.history_model import HistoryModel


class DataAccess:
    """
    Manage all data in a SQlite database.

    All data is stored in a SQlite database and this class takes care about reading from, inserting into, modifying and
    deleting data in the database.
    """

    def __init__(self, db_name: str = "habit_tracker"):
        """
        Create SQlite database and get connection and cursor.

        Constructor creates a SQlite database, connects to it and gets cursor.
        """
        self.__connection = sqlite3.connect(f"db/{db_name}.db")
        self.__cursor = self.__connection.cursor()
        self.create_tables()

    def __del__(self):
        """
        Closes the database connection.

        Destructor closes the database connection when object is destroyed.
        """
        self.__connection.close()

    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.__cursor

    def drop_tables(self) -> None:
        """
        Deletes database tables.

        Both database tables habits and histories get deleted.
        """
        self.__cursor.execute("DROP TABLE histories;")
        self.__connection.commit()
        self.__cursor.execute("DROP TABLE habits;")
        self.__connection.commit()

    def create_tables(self) -> None:
        """
        Creates habits and histories tables in Database.

        If not already existing, the database tables habits and histories get deleted.
        """
        create_habit_table = """
            CREATE TABLE IF NOT EXISTS habits (
                [habit_id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                [habit_name] VARCHAR(255) NOT NULL,
                [habit_specification] VARCHAR(255),
                [habit_creation] DATETIME NOT NULL,
                [habit_periodicity_granularity] VARCHAR(255) NOT NULL,
                [habit_periodicity_from] DATE NOT NULL,
                [habit_periodicity_to] DATE NOT NULL
            );
        """
        self.__cursor.execute(create_habit_table)
        self.__connection.commit()
        create_history_table = """
            CREATE TABLE IF NOT EXISTS histories (
                [history_id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                [habit_id] INTEGER NOT NULL,
                [checkoff_datetime] DATETIME NOT NULL,
                [checked_off] INTEGER NOT NULL,
                FOREIGN KEY ([habit_id]) REFERENCES "habits" ([habit_id])
            );
        """
        self.__cursor.execute(create_history_table)
        self.__connection.commit()

    def insert_history_data_by_model(self, history_model: HistoryModel) -> None:
        """
        A history entry is created.

        Inserts a history entry in histories database table.

        Args:
            history_model (HistoryModel):
                History model with data to be inserted into database table histories.
        """
        insert_history_into_histories = f"""
            INSERT INTO histories (
                [habit_id],
                [checkoff_datetime],
                [checked_off]
            ) VALUES (
                {history_model.habit_id},
                '{history_model.checkoff_datetime}',
                {history_model.checked_off}
            );
        """
        self.__cursor.execute(insert_history_into_histories)
        self.__connection.commit()

    def insert_habit_data_by_model(self, habit_model: HabitModel) -> None:
        """
        A habit entry is created.

        Inserts a habit entry in habits database table.

        Args:
            habit_model (HabitModel):
                Habit model with data to be inserted into database table habits.
        """
        insert_habit_into_habits = f"""
            INSERT INTO habits (
                [habit_name],
                [habit_specification],
                [habit_creation],
                [habit_periodicity_granularity],
                [habit_periodicity_from],
                [habit_periodicity_to]
            ) VALUES (
                '{habit_model.habit_name}',
                '{habit_model.habit_specification}',
                '{habit_model.habit_creation}',
                '{habit_model.habit_periodicity_granularity}',
                '{habit_model.habit_periodicity_from}',
                '{habit_model.habit_periodicity_to}'
            );
        """
        self.__cursor.execute(insert_habit_into_habits)
        self.__connection.commit()
        for history_id in habit_model.habit_history.histories:
            self.insert_history_data_by_model(habit_model.habit_history.histories[history_id])

    def initialize_db(self, habits: Habits) -> None:
        """
        Initialize database by creating a database table and inserting dummy data into it.

        A database table is created and filled with dummy data for pre-defined habits on first usage of CLI application.
        """
        result_habits = self.__cursor.execute("SELECT * FROM habits;")
        result_histories = self.__cursor.execute("SELECT * FROM histories;")
        if len(result_habits.fetchall()) == 0 and len(result_histories.fetchall()) == 0:
            for habit_id in habits.habits:
                self.insert_habit_data_by_model(habits.habits[habit_id])

    def get_habit_by_id(self, habit_id: int) -> HabitModel:
        """
        Get a specific habit given its ID from the database and return a habit model.

        Fetches habit data of a habit with the given ID from database and create and fill a habit model with the data.

        Args:
            habit_id (int):
                ID of a habit that need to be fetched from database.

        Returns:
            HabitModel:
                A habit model containing the data of a habit fetched from the database.
        """
        self.__cursor.execute(f"SELECT * FROM habits WHERE [habit_id] = {habit_id};")
        row = self.__cursor.fetchone()
        habit_model = HabitModel()
        if row is not None:
            habit_model.habit_id = row[0]
            habit_model.habit_name = row[1]
            habit_model.habit_specification = row[2]
            habit_model.habit_creation = row[3]
            habit_model.habit_periodicity_granularity = row[4]
            habit_model.habit_periodicity_from = row[5]
            habit_model.habit_periodicity_to = row[6]
            habit_model.habit_history = self.get_histories_by_habit_id(habit_id)
        else:
            raise NameError("Habit ID does not exist.")
        return habit_model

    def get_history_by_id(self, history_id: int) -> HistoryModel:
        """
        Get a specific history given its ID from the database and return a history model.

        Fetches history data with the given ID from database and create and fill a history model with the data.

        Args:
            history_id (int):
                ID of a history entry that need to be fetched from database.

        Returns:
            HistoryModel:
                A history model containing the data of a history entry fetched from the database.
        """
        self.__cursor.execute(f"SELECT * FROM histories WHERE [history_id] = {history_id};")
        row = self.__cursor.fetchone()
        history_model = HistoryModel()
        if row is not None:
            history_model.history_id = row[0]
            history_model.habit_id = row[1]
            history_model.checkoff_datetime = row[2]
            history_model.checked_off = row[3]
        else:
            raise NameError("Habit ID does not exist.")
        return history_model

    def get_histories_by_habit_id(self, habit_id: int) -> Histories:
        """
        Get histories given the habit ID from the database and return a history model.

        Fetches histories given the habit ID from database and create and fill a history dictionary with the data.

        Args:
            habit_id (int):
                ID of a habit for which history entries need to be fetched from database.

        Returns:
            Histories:
                A history dictionary containing the data of history entries fetched from the database.
        """
        self.__cursor.execute(f"SELECT * FROM histories WHERE [habit_id] = {habit_id};")
        result_rows = self.__cursor.fetchall()
        histories = Histories()
        for row in result_rows:
            history_model = HistoryModel()
            history_model.history_id = row[0]
            history_model.habit_id = row[1]
            history_model.checkoff_datetime = row[2]
            history_model.checked_off = row[3]
            histories.histories[f"{history_model.history_id}"] = history_model
        return histories

    def get_all_habits(self) -> Habits:
        """
        Get a dictionary of habit models with all habits in the database.

        Retrieves all habits from the database and puts them into a Habits.

        Returns:
            Habits:
                A dictionary of habit models with data from the database.
        """
        self.__cursor.execute("SELECT * FROM habits;")
        result_rows = self.__cursor.fetchall()
        habits = Habits()
        for row in result_rows:
            habit_model = HabitModel()
            habit_model.habit_id = row[0]
            habit_model.habit_name = row[1]
            habit_model.habit_specification = row[2]
            habit_model.habit_creation = row[3]
            habit_model.habit_periodicity_granularity = row[4]
            habit_model.habit_periodicity_from = row[5]
            habit_model.habit_periodicity_to = row[6]
            habit_model.habit_history = self.get_histories_by_habit_id(habit_model.habit_id)
            habits.habits[f"{habit_model.habit_id}"] = habit_model
        return habits

    def get_all_habits_by_periodicity(self, periodicity: str) -> Habits:
        """
        Get a dictionary of habit models with all habits in the database that have a specific periodicity.

        Retrieves all habits with a specific periodicity from the database and puts them into a Habits.

        Args:
            periodicity (str):
                Periodicity of the habits to be retrieved.

        Returns:
            Habits:
                A dictionary of habit models with data from the database.
        """
        self.__cursor.execute(f"SELECT * FROM habits WHERE habit_periodicity_granularity = '{periodicity}';")
        result_rows = self.__cursor.fetchall()
        habits = Habits()
        for row in result_rows:
            habit_model = HabitModel()
            habit_model.habit_id = row[0]
            habit_model.habit_name = row[1]
            habit_model.habit_specification = row[2]
            habit_model.habit_creation = row[3]
            habit_model.habit_periodicity_granularity = row[4]
            habit_model.habit_periodicity_from = row[5]
            habit_model.habit_periodicity_to = row[6]
            habit_model.habit_history = self.get_histories_by_habit_id(habit_model.habit_id)
            habits.habits[f"{habit_model.habit_id}"] = habit_model
        return habits

    def create_new_habit(self, name: str, description: str, period: str, habit_from: str, habit_to: str) -> int:
        """
        Create a new habit given its data in the database.

        Add new habit data to database given the name, description, periodicity and start and end date of a new habit.

        Args:
            name (str):
                Name of the new habit to be stored in the database.
            description (str):
                Description of the new habit to be stored in the database.
            period (str):
                Periodicity of the new habit to be stored in the database.
            habit_from (str):
                Start date of the habit.
            habit_to (str):
                End date of the habit.

        Returns:
            int:
                ID of inserted habit.
        """
        insert_habit_into_habits = f"""
            INSERT INTO habits (
                [habit_name],
                [habit_specification],
                [habit_creation],
                [habit_periodicity_granularity],
                [habit_periodicity_from],
                [habit_periodicity_to]
            ) VALUES (
                '{name}',
                '{description}',
                '{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                '{period}',
                '{habit_from}',
                '{habit_to}'
            );
        """
        self.__cursor.execute(insert_habit_into_habits)
        last_id_inserted = self.__cursor.lastrowid
        self.__connection.commit()
        return last_id_inserted

    def delete_habit(self, habit_id: int) -> None:
        """
        Delete a habit from database given its ID.

        Habit with the given ID is removed from the database.

        Args:
            habit_id (int):
                ID of a habit to be deleted from the database.
        """
        delete_habit_from_habits = f"""
            DELETE FROM habits
            WHERE [habit_id] = {habit_id};
        """
        self.__cursor.execute(delete_habit_from_habits)
        self.__connection.commit()
        delete_history_from_histories = f"""
            DELETE FROM histories
            WHERE [habit_id] = {habit_id};
        """
        self.__cursor.execute(delete_history_from_histories)
        self.__connection.commit()

    def modify_habit(self, habit_id: int, name: str, description: str, period: str, habit_from: str, habit_to: str) \
            -> int:
        """
        Modify a habit given its new data in the database.

        Modify data of a habit in the database given its ID, name, description and periodicity.

        Args:
            habit_id (int):
                ID of a habit to be modified in the database.
            name (str):
                Name of the habit to be modified in the database.
            description (str):
                Description of the habit to be modified in the database.
            period (str):
                Periodicity of the habit to be modified in the database.
            habit_from (str):
                Start date of the habit.
            habit_to (str):
                End date of the habit.

        Returns:
            int:
                ID of modified habit.
        """

        if habit_id is None:
            raise NameError("Habit ID does not exist.")

        habit_model = self.get_habit_by_id(habit_id)

        if habit_model.habit_id is not None:
            if name is not None:
                habit_model.habit_name = name
            if description is not None:
                habit_model.habit_specification = description
            if period is not None:
                habit_model.habit_periodicity_granularity = period
            if habit_from is not None:
                habit_model.habit_periodicity_from
            if habit_to is not None:
                habit_model.habit_periodicity_to

            modify_habit_in_habits = f"""
                UPDATE habits 
                SET
                    [habit_name] = '{habit_model.habit_name}',
                    [habit_specification] = '{habit_model.habit_specification}',
                    [habit_periodicity_granularity] = '{habit_model.habit_periodicity_granularity}',
                    [habit_periodicity_from] = '{habit_model.habit_periodicity_from}',
                    [habit_periodicity_to] = '{habit_model.habit_periodicity_to}'
                WHERE [habit_id] = {habit_id};
            """
            self.__cursor.execute(modify_habit_in_habits)
            self.__connection.commit()
            return habit_model.habit_id
        else:
            raise NameError("Habit ID does not exist.")

    def complete_habit(self, habit_id: int, complete_datetime: str) -> int:
        """
        Set a habit with the ID given to be checked-off in the database.

        New data of a habit being checked-off is added to the habit history in the database.

        Args:
            habit_id (int):
                ID of a habit to add a marker in the habit history.
            complete_datetime (str):
                Datetime when the check-off took place.

        Returns:
            int:
                ID of histories entry inserted last.
        """
        select_habit_with_habit_id = f"""
            SELECT [habit_periodicity_granularity], [habit_periodicity_from] FROM habits WHERE [habit_id] = {habit_id};
        """
        self.__cursor.execute(select_habit_with_habit_id)
        habit = self.__cursor.fetchone()
        # Only complete habit if it exists given the habit ID.
        if habit is not None and len(habit) == 2:
            select_latest_history_of_habit = f"""
                SELECT [checkoff_datetime] from histories
                WHERE [habit_id] = {habit_id} and [checked_off] = 1
                ORDER BY [checkoff_datetime] DESC LIMIT 1;
            """
            self.__cursor.execute(select_latest_history_of_habit)
            latest_checkoff_datetime = self.__cursor.fetchone()

            checkoff_datetime = datetime.strptime(complete_datetime, "%Y-%m-%d %H:%M:%S")

            # Get last checked-off datetime of the given habit.
            last_checkoff_exists = False
            if latest_checkoff_datetime is None or len(latest_checkoff_datetime) == 0:
                last_checkoff = datetime.strptime(habit[1]+" 00:00:00", "%Y-%m-%d %H:%M:%S")
            elif latest_checkoff_datetime is not None and len(latest_checkoff_datetime) == 1:
                last_checkoff_exists = True
                last_checkoff = datetime.strptime(latest_checkoff_datetime[0], "%Y-%m-%d %H:%M:%S")

            diff_between_checkoffs = checkoff_datetime - last_checkoff

            if habit[0] == 'daily': # For daily habits calculate the numbers of days between check-offs.
                days_diff_since_last_checkoff = diff_between_checkoffs.days
                # Only complete if habit has not already be completed in this period.
                if last_checkoff_exists and days_diff_since_last_checkoff < 1:
                    raise ValueError(f"Habit with ID {habit_id} has already been checked-off in given period.")
                number_broken = days_diff_since_last_checkoff - 1
                # Start with today and hence add one period to broken habits if no completed period already exists.
                increment = 0
                loop_range = number_broken + 1
                # Start with next period for broken habits if a completed period already exists.
                if last_checkoff_exists:
                    increment = 1
                    loop_range = number_broken
                # Add broken habits for periods in-between two check-offs.
                for index in range(loop_range):
                    insert_history_into_histories = f"""
                        INSERT INTO histories (
                            [habit_id],
                            [checkoff_datetime],
                            [checked_off]
                        ) VALUES (
                            {habit_id},
                            '{(last_checkoff + timedelta(days=index+increment)).strftime("%Y-%m-%d %H:%M:%S")}',
                            0
                        );
                    """
                    self.__cursor.execute(insert_history_into_histories)
                    self.__connection.commit()
            elif habit[0] == 'weekly': # For weekly habits calculate the numbers of weeks between check-offs.
                weeks_diff_since_last_checkoff = int(diff_between_checkoffs.days / 7.0)
                # Only complete if habit has not already be completed in this period.
                if last_checkoff_exists and weeks_diff_since_last_checkoff < 1:
                    raise ValueError(f"Habit with ID {habit_id} has already been checked-off in given period.")
                number_broken = weeks_diff_since_last_checkoff - 1
                # Start with today and hence add one period to broken habits if no completed period already exists.
                increment = 0
                loop_range = number_broken + 1
                # Start with next period for broken habits if a completed period already exists.
                if last_checkoff_exists:
                    increment = 1
                    loop_range = number_broken
                # Add broken habits for periods in-between two check-offs.
                for index in range(loop_range):
                    insert_history_into_histories = f"""
                        INSERT INTO histories (
                            [habit_id],
                            [checkoff_datetime],
                            [checked_off]
                        ) VALUES (
                            {habit_id},
                            '{(last_checkoff + timedelta(weeks=index+increment)).strftime("%Y-%m-%d %H:%M:%S")}',
                            0
                        );
                    """
                    self.__cursor.execute(insert_history_into_histories)
                    self.__connection.commit()
            # Complete habit
            insert_history_into_histories = f"""
                INSERT INTO histories (
                    [habit_id],
                    [checkoff_datetime],
                    [checked_off]
                ) VALUES (
                    {habit_id},
                    '{checkoff_datetime.strftime("%Y-%m-%d %H:%M:%S")}',
                    1
                );
            """
            self.__cursor.execute(insert_history_into_histories)
            last_id_inserted = self.__cursor.lastrowid
            self.__connection.commit()
            return last_id_inserted
        else:
            raise NameError(f"Habit with ID {habit_id} does not exist.")

