import os
import pandas as pd

# Path to your folder with images
folder = r"C:/Users/HP/cnn/satellite_Images"

records = []

for f in os.listdir(folder):
    if f.endswith(".jpg"):
        try:
            parts = f.split("_")
            img_type = parts[0]              # IR / VIS / WV
            date = parts[1]                  # e.g. 20250829
            time = parts[2].split(".")[0]    # e.g. 124641 (remove .jpg)

            records.append({
                "type": img_type,
                "date": date,
                "time": time,
                "filepath": os.path.join(folder, f).replace("\\", "/")
            })
        except Exception as e:
            print("Skipping file:", f, "Error:", e)

df = pd.DataFrame(records)

# Pivot on both date+time, so each row is one triplet IR+VIS+WV
df["datetime"] = df["date"] + "_" + df["time"]
df_pivot = df.pivot_table(index="datetime", columns="type", values="filepath",aggfunc=lambda x: x.iloc[0]).reset_index()

# Save metadata
os.makedirs("preprocessed_data", exist_ok=True)
csv_path = "preprocessed_data/metadata_raw.csv"
df_pivot.to_csv(csv_path, index=False)

print(f"✅ CSV generated at: {csv_path}")
print(df_pivot.head())
print("Total rows (triplets):", len(df_pivot))
