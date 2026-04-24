# Demand Forecasting Time Series Analysis Project

## Overview
This project involves exploratory data analysis (EDA) for a demand forecasting dataset using time series techniques. The dataset contains historical sales data with features such as date, product ID, category ID, store ID, historical sales, price, promotion flag, holiday flag, economic index, and the target variable `target_demand`. The analysis focuses on understanding patterns, trends, and relationships in the data to inform demand forecasting. Note that this project primarily performs EDA and visualization; no predictive models or forecasting algorithms are implemented in the provided code.

## Dataset Description
- **Source**: CSV file (`demand_forecasting_dataset (1).csv`).
- **Key Columns**:
    - `date`: Date of the observation (converted to datetime).
    - `target_demand`: The target variable representing demand (numeric).
    - `price`: Product price (numeric).
    - `promotion_flag`: Binary indicator for promotions (0 or 1).
    - `holiday_flag`: Binary indicator for holidays (0 or 1).
    - `economic_index`: Economic indicator (numeric).
    - Other columns: `product_id`, `category_id`, `store_id`, `historical_sales` (used for context but not directly in analysis).
- **Data Characteristics**: The dataset has multiple entries per date (due to different products/stores), so aggregation to daily means is performed for time series analysis.

## Analysis Steps
The analysis is structured into several functions for modularity:

1. **Data Loading and Preparation**:
     - The dataset is loaded into a Pandas DataFrame (`df`) using `pd.read_csv()`.
     - No additional data cleaning beyond preprocessing is done here.

2. **Validation**:
     - `validate_input()`: Checks if the DataFrame is not empty and contains required columns (`date`, `target_demand`, `price`, `promotion_flag`, `holiday_flag`, `economic_index`). Raises errors if missing.

3. **Preprocessing**:
     - `preprocess()`: 
         - Converts `date` to datetime and numeric columns to numeric types, dropping invalid rows.
         - Aggregates data to daily means using `groupby()` on `date` to handle multiple entries per day.
         - Sets `date` as the index and resamples to daily frequency (though redundant after aggregation).
         - Computes rolling statistics: 7-day rolling mean and standard deviation for `target_demand`.
     - Output: A time series DataFrame (`ts_df`) with daily aggregated data.

4. **Overview and Statistics**:
     - `print_overview()`: Prints basic info (row counts, date range), summary statistics for `target_demand` (using `describe()`), and missing value counts.

5. **Visualization**:
     - `plot_series()`: Generates a 3x2 grid of plots using Matplotlib and Seaborn for EDA.
         - Time series plot with actual demand and 7-day rolling mean.
         - Histogram of demand distribution with KDE.
         - Scatter plot of price vs. demand.
         - Boxplot of demand by promotion status.
         - Scatter plot of economic index vs. demand.
         - Boxplot of demand by holiday status.

6. **Execution**:
     - `main()`: Orchestrates the pipeline by calling validation, preprocessing, overview printing, and plotting.

## Plotting Details
All plots use Seaborn for styling and Matplotlib for figure management. Key plots include:
- **Time Series with Rolling Mean**: Line plots showing demand over time with a smoothed rolling average to highlight trends.
- **Distribution Histogram**: KDE-enhanced histogram to assess normality and spread of demand.
- **Price vs. Demand Scatter**: Examines potential negative correlation between price and demand.
- **Promotion Effect Boxplot**: Compares demand distributions during promotions vs. non-promotions.
- **Economic Index vs. Demand Scatter**: Investigates relationship with economic factors.
- **Holiday Effect Boxplot**: Analyzes demand variations on holidays vs. non-holidays.

## Models and Algorithms Used
This project does not include any machine learning models or forecasting algorithms. It is limited to exploratory data analysis (EDA) techniques:
- **Statistical Summaries**: Basic descriptive statistics (mean, std, min, max, quartiles) via Pandas.
- **Rolling Statistics**: Simple moving averages and standard deviations for trend smoothing.
- **Visualization**: Seaborn/Matplotlib for plots; no predictive modeling (e.g., no ARIMA, Prophet, or regression models).
- **Aggregation**: Groupby operations for daily averaging.

For actual forecasting, extensions could include algorithms like:
- ARIMA/SARIMA for univariate time series forecasting.
- Prophet (Facebook) for handling seasonality and holidays.
- Machine learning models (e.g., Random Forest, XGBoost) using features like price, promotions, and economic index.
- Deep learning (e.g., LSTM networks) for sequence prediction.

## Dependencies
- `pandas`: Data manipulation and time series handling.
- `matplotlib.pyplot`: Plotting backend.
- `seaborn`: Statistical visualizations.
- `warnings`: Suppressing warnings for cleaner output.

## Limitations and Recommendations
- **Limitations**: No forecasting models; analysis is descriptive only. Aggregation to daily means may lose granularity from product/store-specific data.
- **Recommendations**: 
    - Implement forecasting models (e.g., using `statsmodels` for ARIMA or `prophet` library).
    - Explore correlations further with heatmaps or feature engineering.
    - Handle seasonality explicitly (e.g., decompose time series).
    - Validate on train/test splits for any future modeling.

This analysis provides a foundation for understanding demand patterns but requires predictive modeling for actionable forecasts.
