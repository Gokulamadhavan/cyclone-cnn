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
    format="%Y%m%d_%H%M%S",
    errors="coerce"
)

# remove failed timestamps
df_clean = df_clean.dropna(subset=["datetime"])

# Sort chronologically
df_clean = df_clean.sort_values("datetime").reset_index(drop=True)





# Round to nearest 15 min INSAT observation window
df_clean["datetime_15"] = df_clean["datetime"].dt.round("15min")

# Remove duplicates within same 15-min satellite pass
df_clean = df_clean.drop_duplicates(subset=["datetime_15"])

# Remove duplicates within same 15-min satellite pass
df_clean = df_clean.drop_duplicates(subset=["datetime_15"])

# Keep ORIGINAL true timestamps
df_clean = df_clean.sort_values("datetime").reset_index(drop=True)

# NOW compute real delay between observations
df_clean["delta_minutes"] = (
    df_clean["datetime"].diff().dt.total_seconds() / 60
)

df_clean["delta_minutes"] = df_clean["delta_minutes"].fillna(15)

# remove helper column only
df_clean = df_clean.drop(columns=["datetime_15"])
# Save cleaned CSV
os.makedirs("preprocessed_data", exist_ok=True)
clean_csv = "preprocessed_data/metadata_final.csv"
df_clean.to_csv(clean_csv, index=False)
print("Saved cleaned metadata at:", clean_csv)
print("Final usable triplets:", len(df_clean))