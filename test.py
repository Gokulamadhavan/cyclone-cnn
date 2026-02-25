from dataset import SatelliteDataset
from torch.utils.data import DataLoader

# Path to your generated CSV
csv_path = "preprocessed_data/metadata.csv"

# Initialize dataset
dataset = SatelliteDataset(csv_path)

print(f"Total samples in dataset: {len(dataset)}")

# Create a DataLoader for batching
loader = DataLoader(dataset, batch_size=2, shuffle=True)

# Iterate over a few batches
for i, batch in enumerate(loader):
    ir = batch["IR"]
    vis = batch["VIS"]
    wv = batch["WV"]
    dt = batch["datetime"]

    print(f"Batch {i}:")
    print("  IR shape:", ir.shape)
    print("  VIS shape:", vis.shape)
    print("  WV shape:", wv.shape)
    print("  Datetime:", dt)

