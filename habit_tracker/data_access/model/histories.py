
from typing import Dict, List

from habit_tracker.data_access.model.history_model import HistoryModel


class Histories:
    """
    Data structure to store history models in a dictionary.

    Histories is a data structure made of a dictionary of habit models.
    """

    def __init__(self):
        """
        Initializes the dictionary of history models.

        Constructor sets the dictionary of history models to an empty dictionary.
        """
        self.__histories = dict()

    def __str__(self) -> str:
        """
        Outputs data structure as a string.

        Used to translate a dictionary of history models into a string.

        Returns:
            str:
                String representation of a dictionary of history models.
        """
        output = ""
        for history in self.__histories.values():
            output += str(history) + "\n"
        return output

    def transform_to_list(self) -> List[int]:
        """
        Transforms a dictionary of history models to a list of checked-off values.

        Each history model contains a checked-off value. All of them are collected in a list.

        Returns:
            List[int]:
                List of checked-off values taken from a dictionary of history models.
        """
        histories = list()
        for history in self.__histories.values():
            histories.append(history.checked_off)
        return histories

    @property
    def histories(self) -> Dict[str, HistoryModel]:
        """
        Get the dictionary of history models.

        Returns the data structure containing a dictionary of history models.

        Returns:
            Dict[str, HistoryModel]:
                Data structure as a dictionary of history models.
        """
        return self.__histories

    @histories.setter
    def histories(self, histories: Dict[str, HistoryModel]) -> None:
        """
        Set the dictionary of history models.

        Assigns the data structure containing a dictionary of history models.

        Args:
            histories (Dict[str, HabitModel]):
                Data structure as a dictionary of history models.
        """
        self.__histories = histories
