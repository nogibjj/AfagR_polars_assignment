import polars as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn.objects as so
import seaborn as sns
from matplotlib import style

sns.set_style("whitegrid")


def get_data(dataset):
    data = pd.read_csv(dataset)
    return data


def get_mean(df, col):
    return df[col].mean()


def get_median(df, col):
    return df[col].median()


def summary(df):
    return df.describe()


def vizualisation(data, first_column="EngineSize", second_column="Horsepower"):
    sns.set_style("whitegrid")
    my_chart = (
        so.Plot(data, first_column, second_column)
        .add(so.Line(color="r"), so.PolyFit(order=2))
        .add(so.Dot())
        .label(title=f"Visualization of {first_column} and {second_column}")
    )
    my_chart.save(f"Visualization_of_{first_column}_&_{second_column}.png")
    return my_chart


def create_histogram(df, column="Horsepower"):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=20, color="blue", edgecolor="black")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(f"{column}_histogram.png")
    plt.show()


def correlation_matrix(df):
    df = df.select_dtypes(float)
    plt.figure(figsize=(14, 10))
    plt.matshow(
        df.corr(),
        cmap="coolwarm",
    )
    plt.title("Correlation Matrix", pad=20)
    plt.colorbar()
    plt.savefig("correlation_matrix.png")
    plt.show()


def save_to_md(df):
    """save summary report to markdown"""
    describe_df = summary(df)
    markdown_table1 = describe_df.to_markdown()
    # Write the markdown table to a file
    with open("summary_statistics.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz](Horsepower_histogram.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz2](Visualization_of_EngineSize_&_MPG_Highway.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz3](correlation_matrix.png)\n")
