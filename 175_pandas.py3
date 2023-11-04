#175. Combine Two Tables

#problum:
    # Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

#Solution:

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(person, address, on='personId', how='left')
    data = data[['firstName', 'lastName', 'city', 'state']]
    return data
