import pandas as pd
from datetime import datetime


def load_and_filter(xlsx_path):
    """
    Load XLSX file, merge in google sheet issue text, filter to autoparsed
    rows, fill missing values, and strip whitespace.
    """
    df = pd.read_excel(xlsx_path, dtype=str)

    # Filter - only include items marked for autoparsing
    df = df[df['Autoparsed?'].str.contains('Yes')]

    # Fill missing values and strip whitespace
    df = df.fillna('')
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # Generate merge.csv for local record
    # current_datetime = datetime.now().strftime("%Y-%m-%d")
    # df.to_csv(f"data/merge_{current_datetime}.csv", index=False)

    return df

