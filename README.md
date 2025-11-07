# Page View Time Series Visualizer

This project visualizes freeCodeCamp forum page views data from May 2016 to December 2019 using Python, Pandas, Matplotlib, and Seaborn.

## Features

- **Data Cleaning**: Filters out outliers using a threshold to ensure data quality.
- **Line Plot**: Shows daily page views over time.
- **Bar Plot**: Displays average page views by year and month.
- **Box Plot**: Illustrates year-wise and month-wise distributions for trend and seasonality analysis.

## Files

- `time_series_visualizer.py`: Main module containing data import, cleaning, and plotting functions.
- `main.py`: Script to generate all plots.
- `test_module.py`: Unit tests for data cleaning and plot generation.
- `debug_df.py`: Utility script to inspect dataset statistics.
- `fcc-forum-pageviews.csv`: Dataset of daily page views.
- Generated plots: `line_plot.png`, `bar_plot.png`, `box_plot.png`.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/CodeWithStella/Page_View_Time_Series_Visualizer.git
   cd Page_View_Time_Series_Visualizer
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install pandas matplotlib seaborn
   ```

## Usage

Run the main script to generate plots:
```
python main.py
```

Run tests:
```
python test_module.py
```

## Data Source

The dataset is from freeCodeCamp's forum page views, available at [freeCodeCamp](https://www.freecodecamp.org/).

## License

This project is open-source and available under the MIT License.
