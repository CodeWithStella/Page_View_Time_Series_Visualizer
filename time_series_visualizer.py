import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)

# Force correct column name
df.columns = ["value"]

# Clean data
df = df[df['value'] <= 18243]




def draw_line_plot():
    # Copy data
    df_line = df.copy()

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_line.index, df_line['value'])

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save & return
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy data
    df_bar = df.copy()

    # Prepare data
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()

    # Group and pivot
    df_bar = df_bar.groupby(["Year", "Month"])['value'].mean().unstack()

    # Plot
    fig = df_bar.plot(kind="bar", figsize=(12, 6)).get_figure()

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    # Save & return
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data
    df_box = df.copy()
    df_box['Year'] = df_box.index.year
    df_box['Month'] = df_box.index.strftime('%b')
    df_box['MonthNum'] = df_box.index.month

    # Sort by month properly
    df_box = df_box.sort_values("MonthNum")

    # Draw figure
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x="Year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="Month", y="value", data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
