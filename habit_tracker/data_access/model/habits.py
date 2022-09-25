
from typing import Dict

from habit_tracker.data_access.model.habit_model import HabitModel


class Habits:
    """
    Data structure to store habit models in a dictionary.

    Habits is a data structure made of a dictionary of habit models.
    """

    def __init__(self):
        """
        Initializes the dictionary of habit models.

        Constructor sets the dictionary of habit models to an empty dictionary.
        """
        self.__habits = dict()

    def __str__(self) -> str:
        """
        Outputs data structure as a string.

        Used to translate a dictionary of habit models into a string.

        Returns:
            str:
                String representation of a dictionary of habit models.
        """
        output = ""
        for habit in self.__habits.values():
            output += str(habit) + "\n"
        return output

    @property
    def habits(self) -> Dict[str, HabitModel]:
        """
        Get the dictionary of habit models.

        Returns the data structure containing a dictionary of habit models.

        Returns:
            Dict[str, HabitModel]:
                Data structure as a dictionary of habit models.
        """
        return self.__habits

    @habits.setter
    def habits(self, habits: Dict[str, HabitModel]) -> None:
        """
        Set the dictionary of habit models.

        Assigns the data structure containing a dictionary of habit models.

        Args:
            habits (Dict[str, HabitModel]):
                Data structure as a dictionary of habit models.
        """
        self.__habits = habits
