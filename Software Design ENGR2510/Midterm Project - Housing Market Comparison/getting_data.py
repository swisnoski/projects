"""
Module to fetch real estate data for cities using RentCast API.

This module provides functions to fetch real estate data for cities using the
RentCast API. It includes functions to fetch data for a single city or for the
largest cities in each state.

Dependencies:
    - time
    - requests
    - pandas

Functions:
    - get_single_city_data(state, city, longitude, latitude, api_key):
        Fetches real estate data for a single city.
    - get_fifty_states_data(api_key):
        Fetches real estate data for the largest cities in each state.
"""

import time
import requests
import pandas as pd


# Define functions
def get_single_city_data(state, city, longitude, lattitude, api_key):
    """
    his function fetches real estate data for a single-family property
    in a specific city using the RentCast API. The fetched data is saved
    to a text file in the 'city-data' directory with the format
    '{state}_{city}.txt'.

    Args:
        state (str): The state where the city is located.
        city (str): The name of the city.
        longitude (float): The longitude coordinate of the city.
        latitude (float): The latitude coordinate of the city.
        api_key (str): the api key needed to file a request

    Returns:
        None
    """
    property_type = "Single Family"
    bedrooms = "2"
    radius = "4"
    url = f"https://api.rentcast.io/v1/listings/sale?bedrooms={bedrooms}&propertyType={property_type}&latitude={lattitude}&longitude={longitude}&radius={radius}&limit=500"
    headers = {
        "Accept": "application/json",
        "X-Api-Key": api_key,
    }
    response = requests.get(url, headers=headers, timeout=50)

    if response.status_code == 200:
        # Do something with the response data
        # print(data)
        # data = response.json()
        print(response.status_code)
    else:
        print("Error:", response.status_code)

    with open(
        f"city-data/{state.lower()}_{city.lower()}.txt", "w", encoding="utf-8"
    ) as pfd:
        print(response.text, file=pfd)


def get_fifty_states_data(api_key):
    """
    Fetches real estate data for the largest cities in each state.
    Reads a CSV file containing data about the largest cities in each state
    and their corresponding coordinates. For each city, fetches real estate
    data for a single-family property using the 'get_single_city_data' function
    and saves it to a text file.

    Args:
        api_key (str): the api key needed to file a request

    Returns:
        None
    """
    largest_city_data = pd.read_csv("city-data/largest_cities.csv")
    for i in range(len(largest_city_data)):
        state_index = largest_city_data.iloc[i]["State"]
        city_index = largest_city_data.iloc[i]["Largest_City"]
        longitude_index = largest_city_data.iloc[i]["Longitude"]
        latitude_index = largest_city_data.iloc[i]["Latitude"]

        print(f"{state_index}")

        get_single_city_data(
            state_index, city_index, longitude_index, latitude_index, api_key
        )
        time.sleep(1)
