#direct database query
import os
import pandas as pd


# ==================================================
# LOAD DATASET
# ==================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "data.csv"
)

df = pd.read_csv(DATA_PATH)


# ==================================================
# BASIC DATASET FUNCTIONS
# ==================================================

def count_condition(column, value="yes"):
    """
    Count records where a column has a specific value.
    """

    if column not in df.columns:
        return f"Column '{column}' does not exist."

    count = (df[column].astype(str).str.lower() == value.lower()).sum()

    return int(count)


def most_common(column):
    """
    Return the most common value in a column.
    """

    if column not in df.columns:
        return f"Column '{column}' does not exist."

    return df[column].value_counts().idxmax()


def value_counts(column):
    """
    Return frequency of every value in a column.
    """

    if column not in df.columns:
        return f"Column '{column}' does not exist."

    return df[column].value_counts()


def percentage_condition(column, value="yes"):
    """
    Calculate percentage of records matching a value.
    """

    if column not in df.columns:
        return f"Column '{column}' does not exist."

    count = (
        df[column]
        .astype(str)
        .str.lower()
        .eq(value.lower())
        .sum()
    )

    percentage = (count / len(df)) * 100

    return round(percentage, 2)


def total_records():
    """
    Return total number of records.
    """

    return len(df)


# ==================================================
# TEST FUNCTIONS
# ==================================================

if __name__ == "__main__":

    print("=" * 50)
    print("VERBAL AUTOPSY DATASET QUERY")
    print("=" * 50)

    print("\nTotal records:")
    print(total_records())

    print("\nPeople with fever:")
    print(count_condition("fever"))

    print("\nPeople with cough:")
    print(count_condition("cough"))

    print("\nMost common cause of death:")
    print(most_common("cause_of_death"))

    print("\nCause of death distribution:")
    print(value_counts("cause_of_death"))

    print("\nPercentage with fever:")
    print(f"{percentage_condition('fever')}%")

    print("=" * 50)

