"""
Module for processing real estate data and creating scatter plots.

This module provides functions for processing real estate data and
creating scatter plots to visualize relationships between different
metrics.

Dependencies:
    - pandas
    - matplotlib.pyplot
    - processing_data module

Functions:
    - create_scatter_plot(metric1, metric2, xaxis, yaxis):
        Creates a scatter plot of two metrics from a data dictionary.

"""

import pandas as pd
import matplotlib.pyplot as plt
from processing_data import all_price
from processing_data import all_sqft
from processing_data import all_age

largest_city_data = pd.read_csv("city-data/largest_cities.csv")

data_dictionary = {
    "State": [],
    "Price": [],
    "Sqft": [],
    "YearBuilt": [],
}

for i in range(len(largest_city_data)):
    state_index = largest_city_data.iloc[i]["State"]
    city_index = largest_city_data.iloc[i]["Largest_City"]
    dir_path = f"city-data/{state_index.lower()}_{city_index.lower()}.txt"

    age = all_age(dir_path)
    price = all_price(dir_path)
    sqft = all_sqft(dir_path)
    data_dictionary["Price"].extend(price)
    data_dictionary["Sqft"].extend(sqft)
    data_dictionary["YearBuilt"].extend(age)


def create_scatter_plot(metric1, metric2, xaxis, yaxis, xlabel, ylabel, title):
    """
    Creates a scatter plot of two metrics from a data dictionary.

    Generates a scatter plot using the values of two metrics from
    a data dictionary.
    The x-axis represents the values of the first metric, and the
    y-axis represents the values of the second metric.

    Args:
        metric1 (str): The name of the first metric.
        metric2 (str): The name of the second metric.
        xaxis (tuple, optional): Tuple specifying the limits of the x-axis.
        yaxis (tuple, optional): Tuple specifying the limits of the y-axis.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(
        data_dictionary[metric1], data_dictionary[metric2], alpha=0.5, s=5
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(xaxis)
    plt.ylim(yaxis)
    plt.grid(True)
    plt.show()
