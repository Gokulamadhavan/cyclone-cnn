# train.py
import torch
from torch.utils.data import DataLoader
from torchvision import transforms

from dataset import SatelliteDataset
from basic import CycloneCNN
from train_utils import train_step
from dataset import SatelliteDataset
from torch.utils.data import DataLoader

csv_path = "metadata.csv"  # change to your CSV path
dataset = SatelliteDataset(csv_path)

# Debug print
sample = dataset[0]
print("Dataset sample keys:", sample.keys())
print("IR shape:", sample["IR"].shape)
print("VIS shape:", sample["VIS"].shape)
print("WV shape:", sample["WV"].shape)
print("Datetime:", sample["datetime"])

# Wrap in DataLoader
loader = DataLoader(dataset, batch_size=2, shuffle=True)


# Settings
num_epochs = 3  # small number for testing
batch_size = 4
learning_rate = 1e-3
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Dataset + DataLoader
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])
dataset = SatelliteDataset("preprocessed_data/metadata.csv", transform=transform)
loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Model
model = CycloneCNN().to(device)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Training loop with debug prints
for epoch in range(num_epochs):
    print(f"\n=== Epoch {epoch+1}/{num_epochs} ===")
    running_loss = 0.0

    for batch_idx, (images, times) in enumerate(loader):
        # Move tensors to device
        images = images.to(device)
        times = times.to(device)

        # Forward + loss
        outputs = model(images)
        loss = criterion(outputs, times)

        # Backward + optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        # Debug prints
        print(f"Batch {batch_idx+1}:")
        print("  Images shape:", images.shape)
        print("  Times shape:", times.shape)
        print("  Outputs shape:", outputs.shape)
        print("  Batch loss:", loss.item())

    print(f"Epoch {epoch+1} average loss: {running_loss / len(loader):.4f}")
