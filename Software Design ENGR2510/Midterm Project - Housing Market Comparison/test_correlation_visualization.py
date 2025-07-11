"""
module for testing correlation_visualization.py
"""

import pytest


from correlation_visualization import create_scatter_plot

# Mock data dictionary for testing
data_dictionary = {"metric1": [1, 2, 3, 4, 5], "metric2": [2, 3, 4, 5, 6]}


def test_create_scatter_plot_invalid_metric():
    """Test create_scatter_plot with invalid metric names."""
    with pytest.raises(KeyError):
        create_scatter_plot(
            "invalid_metric",
            "metric2",
            None,
            None,
            "X-axis",
            "Y-axis",
            "Test Scatter Plot",
        )
