"""
Module for calculating various statistics from real estate data.

This module provides functions for calculating average price,
average square footage, average age, and extracting lists of
all ages, square footages, and prices from a given dataset.

Dependencies:
    - json
    - statistics

Functions:
    - average_price(path): Calculates the average price of
        single-family properties.
    - average_sqft(path): Calculates the average square footage of
        single-family properties.
    - average_age(path): Calculates the average age of single-family properties.
    - all_age(path): Extracts the year built of all single-family properties.
    - all_sqft(path): Extracts the square footage of all
        single-family properties.
    - all_price(path): Extracts the price of all single-family properties.
"""

import json
import statistics


# Define Functions
def average_price(path):
    """
    Calculates the average price of single-family properties in the
    given dataset.

    Reads a txt file containing real estate data for single-family
    properties. Extracts the price of each property from the dataset
    and calculates the median and mean price. Returns the average of
    the median and mean prices.

    Args:
        path (str): The path to the txt file containing the dataset.

    Returns:
        float: The average price of single-family properties.
    """

    string_data = ""
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as pfd:
        for line in pfd:
            string_data = string_data + str(line)

    processed_data = json.loads(string_data)

    price_list = []
    for listing_dict in processed_data:
        try:
            price_list.append(listing_dict["price"])
        except KeyError:
            continue

    median_price = statistics.median(price_list)
    mean_price = statistics.mean(price_list)
    averages_price = (median_price + mean_price) / 2
    return averages_price


def average_sqft(path):
    """
    Calculates the average square footage of single-family properties in the
    given dataset.

    Reads a txt file containing real estate data for single-family properties.
    Extracts the square footage of each property from the dataset and calculates
    the median and mean square footage. Returns the average of the median
    and mean square footages.

    Args:
        path (str): The path to the txt file containing the dataset.

    Returns:
        float: The average square footage of single-family properties.
    """

    string_data = ""
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as pfd:
        for line in pfd:
            string_data = string_data + str(line)

    processed_data = json.loads(string_data)

    square_footage_list = []
    for listing_dict in processed_data:
        try:
            square_footage_list.append(listing_dict["squareFootage"])
        except KeyError:
            continue

    median_sqft = statistics.median(square_footage_list)
    mean_sqft = statistics.mean(square_footage_list)
    averages_sqft = (median_sqft + mean_sqft) / 2
    return averages_sqft


def average_age(path):
    """
    Calculates the average age of single-family properties in the
    given dataset.

    Reads a txt file containing real estate data for single-family properties.
    Extracts the year built of each property from the dataset and calculates
    the median and mean age. Returns the average of the median and mean ages.

    Args:
        path (str): The path to the txt file containing the dataset.

    Returns:
        float: The average age of single-family properties.
    """

    string_data = ""
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as pfd:
        for line in pfd:
            string_data = string_data + str(line)

    processed_data = json.loads(string_data)

    year_list = []
    for listing_dict in processed_data:
        try:
            year_list.append(listing_dict["yearBuilt"])
        except KeyError:
            continue

    median_year = statistics.median(year_list)
    mean_year = statistics.mean(year_list)
    averaged_age = (median_year + mean_year) / 2

    return averaged_age


def all_age(path):
    """
    Extracts the year built of all single-family properties in the
    given dataset.

    Reads a txt file containing real estate data for single-family properties.
    Extracts the year built of each property from the dataset and returns a list
    of all year built values.

    Args:
        path (str): The path to the txt file containing the dataset.

    Returns:
        list: A list of year built values for all single-family properties.
    """

    string_data = ""
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as pfd:
        for line in pfd:
            string_data = string_data + str(line)

    processed_data = json.loads(string_data)

    price_list1 = []
    year_list1 = []
    square_footage_list1 = []
    price_list = []
    year_list = []
    square_footage_list = []
    for listing_dict in processed_data:
        try:
            price_list1.append(listing_dict["price"])
            year_list1.append(listing_dict["yearBuilt"])
            square_footage_list1.append(listing_dict["squareFootage"])
            year_list.append(listing_dict["yearBuilt"])
            square_footage_list.append(listing_dict["squareFootage"])
            price_list.append(listing_dict["price"])
        except KeyError:
            continue

    return year_list


def all_sqft(path):
    """
    Extracts the square footage of all single-family properties in the
    given dataset.

    Reads a txt file containing real estate data for single-family properties.
    Extracts the square footage of each property from the dataset and returns
    a list of all square footage values.

    Args:
        path (str): The path to the txt file containing the dataset.

    Returns:
        list: A list of square footage values for all single-family properties.
    """

    string_data = ""
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as pfd:
        for line in pfd:
            string_data = string_data + str(line)

    processed_data = json.loads(string_data)

    price_list1 = []
    year_list1 = []
    square_footage_list1 = []
    price_list = []
    year_list = []
    square_footage_list = []
    for listing_dict in processed_data:
        try:
            price_list1.append(listing_dict["price"])
            year_list1.append(listing_dict["yearBuilt"])
            square_footage_list1.append(listing_dict["squareFootage"])
            year_list.append(listing_dict["yearBuilt"])
            square_footage_list.append(listing_dict["squareFootage"])
            price_list.append(listing_dict["price"])
        except KeyError:
            continue

    return square_footage_list


def all_price(path):
    """
    Extracts the price of all single-family properties in the given dataset.

    Reads a txt file containing real estate data for single-family properties.
    Extracts the price of each property from the dataset and returns a list
    of all price values.

    Args:
        path (str): The path to the txt file containing the dataset.

    Returns:
        list: A list of price values for all single-family properties.
    """

    string_data = ""
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as pfd:
        for line in pfd:
            string_data = string_data + str(line)

    processed_data = json.loads(string_data)

    price_list1 = []
    year_list1 = []
    square_footage_list1 = []
    price_list = []
    year_list = []
    square_footage_list = []
    for listing_dict in processed_data:
        try:
            year_list1.append(listing_dict["yearBuilt"])
            square_footage_list1.append(listing_dict["squareFootage"])
            price_list1.append(listing_dict["price"])
            year_list.append(listing_dict["yearBuilt"])
            square_footage_list.append(listing_dict["squareFootage"])
            price_list.append(listing_dict["price"])
        except KeyError:
            continue

    return price_list
