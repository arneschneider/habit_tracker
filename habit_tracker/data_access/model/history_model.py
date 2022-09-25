

class HistoryModel:
    """
    HistoryModel is a representation of all data of the history of a habit.

    The model of the history of a habit contains all data that is also stored in the database.
    """

    def __init__(self):
        """
        Sets all attributes of a history model representing its data.

        Constructor initializes all properties to be filled with actual data of the history of a habit.
        """
        self.__history_id = None
        self.__habit_id = None
        self.__checkoff_datetime = None
        self.__checked_off = None

    def __str__(self) -> str:
        """
        Outputs data structure as a string.

        Used to translate a history model into a string.

        Returns:
            str:
                String representation of a habit model.
        """
        output = f"History-ID: {self.__history_id}, " \
                 f"Habit-ID: {self.__habit_id}, " \
                 f"Checkoff-Datetime: {self.__checkoff_datetime}, " \
                 f"Checked-off: {self.__checked_off}"
        return output

    @property
    def history_id(self) -> int:
        """
        Gets the ID of the history of a habit.

        Returns:
            int:
                ID of the habit.
        """
        return self.__history_id

    @history_id.setter
    def history_id(self, history_id: int) -> None:
        """
        Sets the ID of the history.

        Args:
            history_id (int):
                ID of the history.
        """
        self.__history_id = history_id

    @property
    def habit_id(self) -> int:
        """
        Gets the ID of the habit.

        Returns:
            int:
                ID of the habit.
        """
        return self.__habit_id

    @habit_id.setter
    def habit_id(self, habit_id: int) -> None:
        """
        Sets the ID of the habit.

        Args:
            habit_id (int):
                ID of the habit.
        """
        self.__habit_id = habit_id

    @property
    def checkoff_datetime(self) -> str:
        """
        Gets the datetime of the history entry.

        Returns:
            str:
                Datetime of the history entry.
        """
        return self.__checkoff_datetime

    @checkoff_datetime.setter
    def checkoff_datetime(self, checkoff_datetime: str) -> None:
        """
        Sets the datetime of the history entry.

        Args:
            checkoff_datetime (str):
                Datetime of the history entry.
        """
        self.__checkoff_datetime = checkoff_datetime

    @property
    def checked_off(self) -> str:
        """
        Gets the checked-off value of the history entry.

        Returns:
            str:
                Checked-off value of the history entry.
        """
        return self.__checked_off

    @checked_off.setter
    def checked_off(self, checked_off: str) -> None:
        """
        Sets the checked-off value of the history entry.

        Args:
            checked_off (str):
                Checked-off value of the history entry.
        """
        self.__checked_off = checked_off
