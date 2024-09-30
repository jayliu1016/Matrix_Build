import pytest
import pandas as pd
from main import print_head, describe_stat

# Load the player overview dataset
soccer_df = pd.read_csv("player_overview.csv")


def test_print_head():
    result = print_head()
    assert result.equals(soccer_df.head()), "The head of the dataset does not match."


def test_describe_stat():
    result = describe_stat()
    assert result.equals(soccer_df.describe(include=[float, int])), "The dataset description does not match."
