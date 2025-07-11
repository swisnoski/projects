"""
This module provides functions for visualizing geographical data
related to housing metrics across different states in the United
States.

Dependencies:
    - pandas
    - seaborn
    - geopandas
    - matplotlib
    - shapely.geometry
    - processing_data module (for processing housing data)

    Functions:
    - translate_geometries: Performs translation, scaling, and rotation
        operations on GeoDataFrame geometries.
    - adjust_maps: Adjusts the positions of maps for Alaska and Hawaii
        within a GeoDataFrame.
    - assign_color: Assigns colors to values based on specified data breaks.
    - create_map: Creates a choropleth map showing the distribution of a
        metric across states.
"""

# Import libraries
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from shapely.geometry import Point
from processing_data import average_price
from processing_data import average_sqft
from processing_data import average_age

EDGE_COLOR = "#30011E"
BACKGROUND_COLOR = "#ADD8E6"


def translate_geometries(df, x, y, scale, rotate):
    """
    Performs translation, scaling, and rotation operations on the geometries
    within a GeoDataFrame. The transformations are applied in the order:
    translation, scaling, and rotation.

    Args:
        df (GeoDataFrame): The GeoDataFrame containing geometries to be
        transformed.
        x (float): The distance to translate the geometries along the x-axis.
        y (float): The distance to translate the geometries along the y-axis.
        scale (float): The scaling factor to be applied to the geometries.
        rotate (float): The angle of rotation (in degrees) to be applied
        to the geometries.

    Returns:
        GeoDataFrame: The GeoDataFrame with transformed geometries.
    """
    df.loc[:, "geometry"] = df.geometry.translate(yoff=y, xoff=x)
    center = df.dissolve().centroid.iloc[0]
    df.loc[:, "geometry"] = df.geometry.scale(
        xfact=scale, yfact=scale, origin=center
    )
    df.loc[:, "geometry"] = df.geometry.rotate(rotate, origin=center)
    return df


def adjust_maps(df):
    """
    Adjusts the positions of maps for Alaska and Hawaii within a GeoDataFrame.
    Separates the maps for Alaska and Hawaii from the main land of the United
    States, translates them to their correct positions, and adjusts their
    scales.

    Args:
        df (GeoDataFrame): The GeoDataFrame containing maps for Alaska
        and Hawaii.

    Returns:
        GeoDataFrame: The GeoDataFrame with adjusted map positions.
    """
    df_main_land = df[~df.STATEFP.isin(["02", "15"])]
    df_alaska = df[df.STATEFP == "02"]
    df_hawaii = df[df.STATEFP == "15"]

    df_alaska = translate_geometries(df_alaska, 1470000, -4900000, 0.5, 0)
    df_hawaii = translate_geometries(df_hawaii, 5400000, -1500000, 1, 0)

    return pd.concat([df_main_land, df_alaska, df_hawaii])


def assign_color(value, data_breaks):
    """
    Assigns colors to values based on a list of specified data breaks.
    Values are compared against the data breaks, and colors are
    assigned accordingly.

    Args:
        value (float): The value to be assigned a color.
        data_breaks (list): A list of threshold values for color breaks.

    Returns:
        str: The color assigned to the value.
    """
    for color_index, threshold in enumerate(data_breaks):
        if value >= threshold:
            return colors[color_index]
    return SELECTED_COLOR


sns.set_style(
    {
        "font.family": "serif",
        "figure.facecolor": BACKGROUND_COLOR,
        "axes.facecolor": BACKGROUND_COLOR,
    }
)

# Load and prepare geo-data
states = gpd.read_file("map-data")
states = states[~states.STATEFP.isin(["72", "69", "60", "66", "78"])]
states = states.to_crs("ESRI:102003")
states = adjust_maps(states)


# Load and process data
largest_city_data = pd.read_csv("city-data/largest_cities.csv")

largest_city_coordinates = largest_city_data[
    ["Largest_City", "Latitude", "Longitude"]
]
largest_city_coordinates[["Latitude"]] = largest_city_coordinates[["Latitude"]]
largest_city_coordinates[["Longitude"]] = largest_city_coordinates[
    ["Longitude"]
]

data_dictionary = {
    "State": [],
    "Price": [],
    "Sqft": [],
    "ppsf": [],
    "YearBuilt": [],
}
for i in range(len(largest_city_data)):
    state_index = largest_city_data.iloc[i]["State"]
    city_index = largest_city_data.iloc[i]["Largest_City"]
    dir_path = f"city-data/{state_index.lower()}_{city_index.lower()}.txt"

    age = average_age(dir_path)
    price = average_price(dir_path)
    sqft = average_sqft(dir_path)
    ppsf = price / sqft

    data_dictionary["State"].append(state_index)
    data_dictionary["Price"].append(price)
    data_dictionary["Sqft"].append(sqft)
    data_dictionary["ppsf"].append(ppsf)
    data_dictionary["YearBuilt"].append(age)

housing_dataframe = pd.DataFrame(data_dictionary)

# Create Data Map

# Step 1: Merge housing_dataframe with states
merged_states = states.merge(
    housing_dataframe, how="left", left_on="STUSPS", right_on="State"
)

# Step 2: Define color breaks and corresponding colors based on housing prices
colors = [
    "#070a02",
    "#161d07",
    "#25310c",
    "#344510",
    "#435815",
    "#526c1a",
    "#617f1f",
    "#709323",
    "#7fa628",
    "#8eba2d",
    "#9dce31",
    "#a7d245",
    "#b0d759",
    "#b9dc6c",
    "#c3e080",
    "#cce593",
    "#d5eaa7",
    "#deefba",
    "#e8f3ce",
    "#f1f8e2",
    "#fafafa",
]
SELECTED_COLOR = "#fafafa"


def create_map(
    threshold_list, metric, title, legend_title, unit, threshold_high
):
    """
    Creates a choropleth map showing the distribution of a metric across states.
    The choropleth map illustrates the distribution of a given metric
    across different states. The map is colored based on the values
    of the metric.

    Args:
        threshold_list (list): A list of threshold values for color breaks.
        metric (str): The name of the metric to be displayed on the map.
        title (str): The title of the map.
        legend_title (str): The title of the legend.
        unit (str): The unit of measurement for the metric.
        threshold_high (str): The label for the threshold
            higher than the highest value.

    Returns:
        None
    """
    data_breaks = threshold_list

    # Step 3: Assign colors to the states based on their housing prices
    merged_states["color"] = merged_states[metric].apply(
        lambda x: assign_color(x, data_breaks)
    )

    # Step 4: Plot the map with housing price data
    _, ax = plt.subplots(figsize=(18, 14))
    merged_states.plot(
        column="color",
        ax=ax,
        edgecolor=EDGE_COLOR + "55",
        linewidth=0.8,
        legend=True,
        cmap=ListedColormap(colors),
    )
    states.plot(ax=ax, edgecolor=EDGE_COLOR, color="None", linewidth=1)

    for _, row in largest_city_coordinates.iterrows():
        # Transform latitude and longitude to match map projection
        point = gpd.GeoSeries(
            [Point(row["Longitude"], row["Latitude"])], crs="EPSG:4326"
        )
        point = point.to_crs("ESRI:102003")

        if row["Largest_City"] == "Honolulu":
            new_x = point.geometry.x.iloc[0] + 5400000
            new_y = point.geometry.y.iloc[0] - 1500000
            point = gpd.GeoSeries([Point(new_x, new_y)], crs="ESRI:102003")
        if row["Largest_City"] == "Anchorage":
            new_x = point.geometry.x.iloc[0] + 1450000
            new_y = point.geometry.y.iloc[0] - 4770000
            point = gpd.GeoSeries([Point(new_x, new_y)], crs="ESRI:102003")

        # Plot the transformed point
        ax.plot(
            point.geometry.x,
            point.geometry.y,
            marker="o",
            color="red",
            markersize=5,
        )

        ax.annotate(
            row["Largest_City"],
            xy=(
                point.geometry.x.iloc[0],
                point.geometry.y.iloc[0],
            ),  # Position of the point
            xytext=(5, -5),  # Offset the text by a small amount
            textcoords="offset points",
            fontsize=10,
            color="red",
        )

    # Additional plot settings
    ax.set(xlim=(-3000000, None))  # Removing some of the padding to the left
    ax.set(ylim=(-2000000, 1550000))  # Removing some of the padding to the left
    plt.axis("off")
    plt.title(title)

    legend_labels = [f"More than {threshold_high}{unit}"] + [
        f"{threshold}{unit}" for threshold in data_breaks
    ]
    legend_patches = [
        Patch(color=color, label=label)
        for color, label in zip(colors, legend_labels)
    ]
    plt.legend(
        handles=legend_patches,
        title=legend_title,
        loc="lower left",
        bbox_to_anchor=(-0.17, 0.25),
    )

    plt.show()
