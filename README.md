# Habit Tracker

Habit Tracker is a CLI application to keep track of personal goals and how well they were achieved.

## Setup

### Install SQLite on Linux

```shell
sudo apt-get install sqlite3
```

### Install SQLite on Windows

Download precompiled binaries for Windows and extract the ZIP archive to a location of your choice.

### Virtual Environment and Dependencies on Linux

```shell
python3 -m venv .venv/
source .venv/bin/activate
pip install poetry
poetry install
```

### Virtual Environment and Dependencies on Windows

```shell
python3 -m venv .venv\
.venv\Scripts\activate
pip install poetry
poetry install
```

### Run application

#### Display Usage Message 

```shell
peotry run habit-tracker
```

```
Usage: habit-tracker [OPTIONS] COMMAND [ARGS]...

  Habit Tracker is a CLI application to keep track of personal goals and how
  well they were achieved.

Options:
  --help  Show this message and exit.

Commands:
  complete                        Complete, that means, check-off a...
  create                          Create a new habit.
  delete                          Delete a habit.
  init-db                         Initializes the database for first...
  longest-run-streak              Show longest run streak.
  longest-run-streak-daily        Show all daily longest run streak.
  longest-run-streak-for-given-habit
                                  Show longest run streak for a given...
  longest-run-streak-weekly       Show all weekly longest run streak.
  modify                          Modify a habit.
  show                            Show all habits.
  show-daily                      Show all daily habits.
  show-weekly                     Show all weekly habits.
```


#### Initialize Habits with Predefined Habits

A couple of predefined habits can be created by executing the following command:

```shell
poetry run habit-tracker init-db
```

#### Show All Habits

An overview of all habits can be given with the following command:

```shell
poetry run habit-tracker show
```

##### Show All Weekly Habits

To get an overview about all weekly habits you can execute the following command:

```shell
poetry run habit-tracker show-weekly
```

##### Show All Daily Habits

All daily habits can be listed in an overview with the following command:

```shell
poetry run habit-tracker show-daily
```

#### Creating New Habits

In order to add new habits one can use the `create`-command like this:

```shell
poetry run habit-tracker create --name "practice painting" --description "Practice painting each day" --period "daily" --habit-from "2022-10-01" --habit-to "2022-12-31"
```

#### Modify Existing Habit

After having created a habit you can alter the attributes of a habit later on like so:

```shell
poetry run habit-tracker modify --id 42 --name "practice drawing" --description "Practice drawing each day to become a master" --period "daily" --habit-from "2022-10-01" --habit-to "2022-12-31"
```

#### Delete Existing Habit

Habits can be deleted given the habit ID like this:

```shell
poetry run habit-tracker delete --id 42
```

#### Longest Run Streak of All Habits

Habits can be analysed by determining the longest run streak of all habits:

```shell
poetry run habit-tracker longest-run-streak
```

#### Longest Run Streak of All Weekly Habits

Only for weekly habits the longest run streak can be determined:

```shell
poetry run habit-tracker longest-run-streak-weekly
```

#### Longest Run Streak of All Daily Habits

Only for daily habits you can determine the longest run streak:

```shell
poetry run habit-tracker longest-run-streak-daily
```

#### Longest Run Streak of a Given Habit

The longest run streak of a habit given its habit ID can be determined:

```shell
poetry run habit-tracker longest-run-streak-for-given-habit --id 42
```
