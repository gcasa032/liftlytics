import pandas
from pandas import DataFrame
from datetime import datetime
import re

def inspect_range_constraint(df):
    """ Given the OpenPowerlifting dataset this function returns rows outside of range constraints
        including info regarding the specific validation check
        TODO add type check for input DF, validate the schema

    Args:
        df (_type_): A dataframe containing OpenPowerlifting data
    """

    # Go though various checks and append results to the DF which we will return

    age_constraint = df[df['Age'] > 120]
    bw_constraint = df[df['BodyweightKg'] > 230]

    # Check for date that is in the future
    print(age_constraint.head())

    return None


def date_oorc(df:DataFrame):
    """Find any rows in the DataFrame in which the Date is outside the Date OORC (Out Of Range Contraint)

    Args:
        df (_type_): Open Powerlifting data
    """

    tdy = datetime.strftime(datetime.today(), "%Y-%m-%d") # Todays date as a string
    df_date = df[df['Date'] > tdy]

    df_date["VAL_ERR_CODE"] = "DATE_OORC"
    df_date["ERR_COMMENT"] = f"Competition date cannot be in the future. Meet date = {df_date['Date']}, Todays date = {tdy}"

    return df_date

def date_regxc(df: DataFrame):
    """Find any rows in the DataFrame in which the Date column is not in the correct format

    Args:
        df (_type_): Open Powerlifting data

    Args:
        df (DataFrame): _description_
    """

    def is_date(string):
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        match = re.match(pattern, string)
        return bool(match)

    df_date_format = df[~df['Date'].apply(is_date)]

    df_date_format["VAL_ERR_CODE"] = "DATE_REGXC"
    df_date_format["ERR_COMMENT"] = f"Date must be in the YYYY-MM-DD format. Date = {df_date_format['Date']}"

    return df_date_format

def dupe_constraint(df: DataFrame):

    df2 = df.groupby(df.columns.tolist(), as_index=False).size()

    return df2[df2['size'] > 1]

def age_cfv(df: DataFrame):
    """ This cross field validation check looks for invalid age

    Args:
        df (DataFrame): Open Powerlifting data
    """

    # I am looking for a lifters who have 

    return None


def bw_range_constraint(df):
    """Helper function for `inspect_range_contraint(df)`. This function finds rows where the BW is outside of range

    Args:
        df (_type_): _description_
    """

    # TODO this should be a cross-field validation

    bw_constraint = df[df['BodyweightKg'] > 230]


def clean_openpl_data(df):

    return df[df.duplicated()].groupby(list(df.columns)).size().reset_index(name='dupe_count')

    # find duplicates
    # find lifters who are are listed as ambigious
    # TODO: List other wrong data