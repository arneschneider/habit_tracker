
from habit_tracker.data_access.model.histories import Histories


class HabitModel:
    """
    HabitModel is a representation of all data of a habit.

    The model of a habit contains all data that is also stored in the database.
    """

    def __init__(self):
        """
        Sets all attributes of a habit model representing its data.

        Constructor initializes all properties to be filled with actual data of a habit.
        """
        self.__habit_id = None
        self.__habit_name = None
        self.__habit_specification = None
        self.__habit_creation = None
        self.__habit_periodicity_granularity = None
        self.__habit_periodicity_from = None
        self.__habit_periodicity_to = None
        self.__habit_history = Histories()

    def __str__(self) -> str:
        """
        Outputs data structure as a string.

        Used to translate a habit model into a string.

        Returns:
            str:
                String representation of a habit model.
        """
        output = f"Habit-ID: {self.__habit_id}, " \
                 f"Habit-Name: {self.__habit_name}, " \
                 f"Habit-Specification: {self.__habit_specification}, " \
                 f"Habit-Creation: {self.__habit_creation}, " \
                 f"Habit-Periodicity: {self.__habit_periodicity_granularity}, " \
                 f"Habit-From: {self.__habit_periodicity_from}, " \
                 f"Habit-To: {self.__habit_periodicity_to}, " \
                 f"Habit-History:\n{str(self.__habit_history)}"
        return output

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
    def habit_name(self) -> str:
        """
        Gets the name of the habit.

        Returns:
            str:
                Name of the habit.
        """
        return self.__habit_name

    @habit_name.setter
    def habit_name(self, habit_name: str) -> None:
        """
        Sets the name of the habit.

        Args:
            habit_name (str):
                Name of the habit.
        """
        self.__habit_name = habit_name

    @property
    def habit_specification(self) -> str:
        """
        Gets the specification of the habit.

        Returns:
            str:
                Specification of the habit.
        """
        return self.__habit_specification

    @habit_specification.setter
    def habit_specification(self, habit_specification: str) -> None:
        """
        Sets the specification of the habit.

        Args:
            habit_specification (str):
                Specification of the habit.
        """
        self.__habit_specification = habit_specification

    @property
    def habit_creation(self) -> str:
        """
        Gets the creation date and time of the habit.

        Returns:
            str:
                Creation date and time of the habit.
        """
        return self.__habit_creation

    @habit_creation.setter
    def habit_creation(self, habit_creation: str) -> None:
        """
        Sets the creation date and time of the habit.

        Args:
            habit_creation (str):
                Creation date and time of the habit.
        """
        self.__habit_creation = habit_creation

    @property
    def habit_periodicity_granularity(self) -> str:
        """
        Gets the periodicity of the habit.

        Returns:
            str:
                Periodicity of the habit.
        """
        return self.__habit_periodicity_granularity

    @habit_periodicity_granularity.setter
    def habit_periodicity_granularity(self, habit_periodicity_granularity: str) -> None:
        """
        Sets the periodicity of the habit.

        Args:
            habit_periodicity_granularity (str):
                Periodicity of the habit.
        """
        self.__habit_periodicity_granularity = habit_periodicity_granularity

    @property
    def habit_periodicity_from(self) -> str:
        """
        Gets the start date of the habit.

        Returns:
            str:
                Start date of the habit.
        """
        return self.__habit_periodicity_from

    @habit_periodicity_from.setter
    def habit_periodicity_from(self, habit_periodicity_from: str) -> None:
        """
        Sets the start date of the habit.

        Args:
            habit_periodicity_from (str):
                Start date of the habit.
        """
        self.__habit_periodicity_from = habit_periodicity_from

    @property
    def habit_periodicity_to(self) -> str:
        """
        Gets the end date of the habit.

        Returns:
            str:
                End date of the habit.
        """
        return self.__habit_periodicity_to

    @habit_periodicity_to.setter
    def habit_periodicity_to(self, habit_periodicity_to: str) -> None:
        """
        Sets the end date of the habit.

        Args:
            habit_periodicity_to (str):
                End date of the habit.
        """
        self.__habit_periodicity_to = habit_periodicity_to

    @property
    def habit_history(self) -> Histories:
        """
        Gets the habit history of the habit.

        Returns:
            Histories:
                History of the habit.
        """
        return self.__habit_history

    @habit_history.setter
    def habit_history(self, habit_history: Histories) -> None:
        """
        Sets the habit history of the habit.

        Args:
            habit_history (Histories):
                History of the habit.
        """
        self.__habit_history = habit_history
