"""
module for pytest, testing the file processing_data.py
"""

import json
import pytest
from processing_data import average_price
from processing_data import average_sqft
from processing_data import average_age
from processing_data import all_age
from processing_data import all_sqft
from processing_data import all_price


@pytest.fixture
def sample_data(tmp_path):
    """makes sample data"""
    data = [
        {"yearBuilt": 1990, "squareFootage": 2000, "price": 300000},
        {"yearBuilt": 2005, "squareFootage": 1800},  # missing price
        {"yearBuilt": 2010, "squareFootage": 2200, "price": 350000},
    ]
    file_path = tmp_path / "sample.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return str(file_path)


def test_all_price_returns_list(sample_data):
    """Checks if the all_price function returns a list."""
    assert isinstance(all_price(sample_data), list)


def test_all_price_contains_prices(sample_data):
    """Checks if all prices returned by the all_price function are integers."""
    prices = all_price(sample_data)
    assert all(isinstance(price, int) for price in prices)


def test_all_price_correct_prices(sample_data):
    """Checks if the all_price function returns the correct prices."""
    prices = all_price(sample_data)
    assert prices == [300000, 350000]


def test_all_age_returns_list(sample_data):
    """Checks if the all_age function returns a list."""
    assert isinstance(all_age(sample_data), list)


def test_all_age_contains_ages(sample_data):
    """Checks if all ages returned by the all_age function are integers."""
    ages = all_age(sample_data)
    assert all(isinstance(age, int) for age in ages)


def test_all_age_correct_ages(sample_data):
    """Checks if the all_age function returns the correct ages."""
    ages = all_age(sample_data)
    assert ages == [1990, 2010]


def test_all_sqft_returns_list(sample_data):
    """Checks if the all_sqft function returns a list."""
    assert isinstance(all_sqft(sample_data), list)


def test_all_sqft_contains_sqft(sample_data):
    """Checks if all sqft returned by the all_sqft function are integers."""
    sqfts = all_sqft(sample_data)
    assert all(isinstance(sqft, int) for sqft in sqfts)


def test_all_sqft_correct_sqft(sample_data):
    """Checks if the all_sqft function returns the correct sqfts."""
    sqfts = all_sqft(sample_data)
    assert sqfts == [2000, 2200]


def test_ave_price_returns_float(sample_data):
    """Checks if the average_price function returns an float."""
    assert isinstance(average_price(sample_data), float)


def test_ave_price_correct_price(sample_data):
    """Checks if the aveerage_price function returns the correct price."""
    price = average_price(sample_data)
    assert price == 325000


def test_ave_age_returns_float(sample_data):
    """Checks if the average_age function returns an float."""
    assert isinstance(average_age(sample_data), float)


def test_ave_age_correct_age(sample_data):
    """Checks if the all_age function returns the correct age."""
    age = average_age(sample_data)
    assert age == 2003.3333333333335


def test_ave_sqft_returns_float(sample_data):
    """Checks if the average_sqft function returns an float."""
    assert isinstance(average_sqft(sample_data), float)


def test_ave_sqft_correct_sqft(sample_data):
    """Checks if the all_sqft function returns the correct sqft."""
    sqft = average_sqft(sample_data)
    assert sqft == 2000
