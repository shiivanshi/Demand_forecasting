"""Time series analysis template using pandas, matplotlib, and seaborn.

How to use:
1. Load your dataset into `df` in the placeholder section below imports.
2. Set DATE_COLUMN and TARGET_COLUMN to match your dataset.
3. Run the script.
"""

import warnings

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# === DATASET PLACEHOLDER ===
# Upload/load your dataset into this `df` variable.
# Example:
# df = pd.read_csv("your_dataset.csv")
df = None

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid", context="talk")

# Update these to match your dataset
DATE_COLUMN = "date"
TARGET_COLUMN = "value"
FREQUENCY = "D"  # D=daily, W=weekly, M=monthly, etc.
ROLLING_WINDOW = 7


def validate_input(dataframe: pd.DataFrame) -> None:
    """Validate that required columns exist and data is usable."""
    if dataframe is None or dataframe.empty:
        raise ValueError("`df` is empty. Please load your dataset into the df variable.")

    missing = [col for col in [DATE_COLUMN, TARGET_COLUMN] if col not in dataframe.columns]
    if missing:
        raise ValueError(
            f"Missing required columns: {missing}. "
            "Update DATE_COLUMN/TARGET_COLUMN to match your dataset."
        )


def preprocess(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Convert date column, clean target, and create indexed time series."""
    ts = dataframe.copy()

    ts[DATE_COLUMN] = pd.to_datetime(ts[DATE_COLUMN], errors="coerce")
    ts[TARGET_COLUMN] = pd.to_numeric(ts[TARGET_COLUMN], errors="coerce")
    ts = ts.dropna(subset=[DATE_COLUMN, TARGET_COLUMN]).sort_values(DATE_COLUMN)

    ts = ts.set_index(DATE_COLUMN)
    ts = ts.resample(FREQUENCY).mean(numeric_only=True)
    ts["rolling_mean"] = ts[TARGET_COLUMN].rolling(ROLLING_WINDOW).mean()
    ts["rolling_std"] = ts[TARGET_COLUMN].rolling(ROLLING_WINDOW).std()
    return ts


def print_overview(raw_df: pd.DataFrame, ts_df: pd.DataFrame) -> None:
    """Print a concise statistical overview."""
    print("\n=== Basic Overview ===")
    print(f"Rows (raw): {len(raw_df)}")
    print(f"Rows (after preprocessing): {len(ts_df)}")
    print(f"Date range: {ts_df.index.min()} -> {ts_df.index.max()}")
    print("\n=== Summary statistics ===")
    print(ts_df[TARGET_COLUMN].describe())
    print("\nMissing values after preprocessing:")
    print(ts_df.isna().sum())


def plot_series(ts_df: pd.DataFrame) -> None:
    """Create a small set of standard time series plots."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    # 1) Main series + rolling stats
    sns.lineplot(x=ts_df.index, y=ts_df[TARGET_COLUMN], ax=axes[0, 0], label="Actual")
    sns.lineplot(x=ts_df.index, y=ts_df["rolling_mean"], ax=axes[0, 0], label=f"{ROLLING_WINDOW}-period Rolling Mean")
    axes[0, 0].set_title("Time Series with Rolling Mean")
    axes[0, 0].set_xlabel("Date")
    axes[0, 0].set_ylabel(TARGET_COLUMN)

    # 2) Distribution
    sns.histplot(ts_df[TARGET_COLUMN].dropna(), kde=True, ax=axes[0, 1], color="teal")
    axes[0, 1].set_title("Distribution of Target")
    axes[0, 1].set_xlabel(TARGET_COLUMN)

    # 3) Boxplot by month (seasonality glimpse)
    monthly = ts_df.copy()
    monthly["month"] = monthly.index.month
    sns.boxplot(data=monthly, x="month", y=TARGET_COLUMN, ax=axes[1, 0], color="lightblue")
    axes[1, 0].set_title("Monthly Distribution")
    axes[1, 0].set_xlabel("Month")

    # 4) Autocorrelation-like lag plot (simple)
    lagged = ts_df[[TARGET_COLUMN]].copy()
    lagged["lag_1"] = lagged[TARGET_COLUMN].shift(1)
    sns.scatterplot(data=lagged, x="lag_1", y=TARGET_COLUMN, ax=axes[1, 1], alpha=0.6)
    axes[1, 1].set_title("Lag Plot (t vs t-1)")
    axes[1, 1].set_xlabel("Lag 1")

    plt.tight_layout()
    plt.show()


def main() -> None:
    validate_input(df)
    ts_df = preprocess(df)
    print_overview(df, ts_df)
    plot_series(ts_df)


if __name__ == "__main__":
    main()
