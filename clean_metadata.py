import pandas as pd
import os

raw_csv = "preprocessed_data/metadata_raw.csv"

df = pd.read_csv(raw_csv)

print("Original rows:", len(df))

# Remove incomplete IR-VIS-WV triplets
df_clean = df.dropna(subset=["IR", "VIS", "WV"])

print("After removing incomplete sets:", len(df_clean))

# Convert datetime to actual datetime object
df_clean["datetime"] = pd.to_datetime(
    df_clean["datetime"],
    format="%Y%m%d_%H%M%S"
)

# Sort chronologically
df_clean = df_clean.sort_values("datetime").reset_index(drop=True)

# Compute time difference in minutes
df_clean["delta_minutes"] = (
    df_clean["datetime"].diff().dt.total_seconds() / 60
)

# First row default = 15 mins
df_clean["delta_minutes"] = df_clean["delta_minutes"].fillna(15)

# Save cleaned CSV
os.makedirs("preprocessed_data", exist_ok=True)
clean_csv = "preprocessed_data/metadata_cleaned.csv"
df_clean.to_csv(clean_csv, index=False)

print("Saved cleaned metadata at:", clean_csv)
print("Final usable triplets:", len(df_clean))
