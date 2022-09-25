import sqlite3

import click

from habit_tracker.data_access.data_access import DataAccess
from habit_tracker.habit_tracker.habit_tracker import HabitTracker


@click.group()
def cli() -> None:
    """
    Habit Tracker is a CLI application to keep track of personal goals and how well they were achieved.
    """
    pass


@cli.command(help="Initializes the database for first usage with dummy dataa.")
def init_db() -> None:
    """
    Click command initializes database with dummy data.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to initialize the database with dummy
    data.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    habit_tracker.initialize_db()

    
@cli.command(help="Create a new habit.")
@click.option("--name", help="Name of the habit.")
@click.option("--description", help="Description of the habit.")
@click.option("--period", help="Periodicity of the habit, eg daily, weekly.")
@click.option("--habit-from", help="Start date of habit (YYYY-MM-DD), eg 2022-09-01.")
@click.option("--habit-to", help="End date of habit (YYYY-MM-DD), eg 2022-10-01.")
def create(name: str, description: str, period: str, habit_from: str, habit_to: str) -> None:
    """
    Click command creates a new habit in the database based on data given on the CLI.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to create a new habit.

    Args:
        name (str):
            Determines the name of the new habit.
        description (str):
            Determines the description of the new habit.
        period (str):
            Determines the periodicity of the new habit.
        habit_from (str):
            Determines the start date of a habit.
        habit_to (str):
            Determines the end date of a habit.
    """
    is_incomplete = False
    if name is None:
        click.echo("Habit name is not given.")
        is_incomplete = True
    if description is None:
        click.echo("Habit description is not given.")
        is_incomplete = True
    if period is None:
        click.echo("Habit period is not given.")
        is_incomplete = True
    if habit_from is None:
        click.echo("Habit start date habit-from is not given.")
        is_incomplete = True
    if habit_to is None:
        click.echo("Habit end date habit-to is not given.")
        is_incomplete = True
    if is_incomplete:
        return

    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    habit_id = habit_tracker.create_new_habit(name, description, period, habit_from, habit_to)
    if habit_id > 0:
        click.echo(f"Habit '{name}' created.")


@cli.command(help="Delete a habit.")
@click.option("--id", help="ID of the habit to delete.")
def delete(id: int) -> None:
    """
    Click command deletes a habit in the database based on habit id given on the CLI.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to delete a habit.

    Args:
        id (int):
            Determines the id of the habit to be deleted.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    habit_tracker.delete_habit(id)
    click.echo(f"Habit with ID '{id}' deleted.")


@cli.command(help="Modify a habit.")
@click.option("--id", help="ID of the habit to modify.")
@click.option("--name", default=None, help="Name of the habit.")
@click.option("--description", default=None, help="Description of the habit.")
@click.option("--period", default=None, help="Periodicity of the habit.")
@click.option("--habit-from", default=None, help="Start date of habit (YYYY-MM-DD), eg 2022-09-01.")
@click.option("--habit-to", default=None, help="End date of habit (YYYY-MM-DD), eg 2022-10-01.")
def modify(id: int, name: str, description: str, period: str, habit_from: str, habit_to: str) -> None:
    """
    Click command modifies a habit in the database based on data given on the CLI.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to modify a habit.

    Args:
        id (int):
            Determines the id of the habit to be modified.
        name (str):
            Determines the new name of the habit to be modified.
        description (str):
            Determines the new description of the habit to be modified.
        period (str):
            Determines the periodicity of the habit to be modified.
        habit_from (str):
            Determines the start date of the habit.
        habit_to (str):
            Determines the end date of the habit.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    habit_id = 0
    try:
        habit_id = habit_tracker.modify_habit(id, name, description, period, habit_from, habit_to)
    except NameError as name_error:
        click.echo(f"Habit with ID '{id}' does not exist.")
    if habit_id > 0:
        click.echo(f"Habit with ID '{habit_id}' modified.")


@cli.command(help="Complete, that means, check-off a habit.")
@click.option("--id", help="ID of the habit to complete / check-off.")
def complete(id: int) -> None:
    """
    Click command checks-off a habit in the database based on habit id given on the CLI.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to check-off a habit.

    Args:
        id (int):
            Determines the id of the habit to be checked-off.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    history_id = 0
    try:
        history_id = habit_tracker.complete_habit(id)
    except NameError as name_error:
        click.echo(f"Habit with ID '{id}' does not exist.")
    except ValueError as value_error:
        click.echo(f"Habit with ID '{id}' has already been checked-off in given period.")
    if history_id > 0:
        click.echo(f"Habit with ID '{id}' completed / checked-off.")


@cli.command(help="Show all habits.")
def show() -> None:
    """
    Click command shows all habits in the database.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to list all habits.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    habits = habit_tracker.show_all_habits()
    click.echo("Showing list of all defined habits:")
    if len(habits.habits) > 0:
        click.echo(str(habits))
    else:
        click.echo("No habits exist.")


@cli.command(help="Show all daily habits.")
def show_daily() -> None:
    """
    Click command shows all daily habits in the database.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to list all daily habits.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    habits = habit_tracker.show_all_habits_by_periodicity("daily")
    click.echo("Showing list of all defined daily habits:")
    if len(habits.habits) > 0:
        click.echo(str(habits))
    else:
        click.echo("No habits exist.")


@cli.command(help="Show all weekly habits.")
def show_weekly() -> None:
    """
    Click command shows all weekly habits in the database.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to list all weekly habits.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    habits = habit_tracker.show_all_habits_by_periodicity("weekly")
    click.echo("Showing list of all defined weekly habits:")
    if len(habits.habits) > 0:
        click.echo(str(habits))
    else:
        click.echo("No habits exist.")


@cli.command(help="Show longest run streak.")
def longest_run_streak() -> None:
    """
    Click command shows the longest streak of all habits in the database.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to list the longest streak of all habits.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    longest_streak = habit_tracker.calc_longest_run_streak()
    click.echo("Showing longest run streak with a length of: " + str(longest_streak))


@cli.command(help="Show all daily longest run streak.")
def longest_run_streak_daily() -> None:
    """
    Click command shows the longest streak of all daily habits in the database.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to list the longest streak of all daily
    habits.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    longest_streak = habit_tracker.calc_longest_run_streak_by_periodicity('daily')
    click.echo("Showing longest daily run streak with a length of: " + str(longest_streak))


@cli.command(help="Show all weekly longest run streak.")
def longest_run_streak_weekly():
    """
    Click command shows the longest streak of all weekly habits in the database.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to list the longest streak of all weekly
    habits.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    longest_streak = habit_tracker.calc_longest_run_streak_by_periodicity('weekly')
    click.echo("Showing longest weekly run streak with a length of: " + str(longest_streak))


@cli.command(help="Show  longest run streak for a given habit.")
@click.option("--id", help="ID of the habit to show it's longest run streak.")
def longest_run_streak_for_given_habit(id):
    """
    Click command shows the longest streak of a specific habit in the database.

    It sets the DataAccess attribute in HabitTracker and calls the HabitTrackr to list the longest streak of a specific
    habit.
    """
    habit_tracker = HabitTracker()
    habit_tracker.data_access = DataAccess()
    longest_streak = habit_tracker.calc_longest_run_streak_of_habit(id)
    click.echo(f"Showing longest run streak for given habit with ID {id} with length of: " + str(longest_streak))
