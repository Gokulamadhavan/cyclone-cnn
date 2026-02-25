import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset
import torchvision.transforms as T

class SatelliteDataset(Dataset):
    def __init__(self, csv_path, transform=None):
        self.data = pd.read_csv(csv_path)
        self.transform = transform

        # Default transforms if none provided
        if self.transform is None:
            self.transform = T.Compose([
                T.Resize((128, 128)),
                T.ToTensor()
            ])
        
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]

        ir_path = row["IR"]
        vis_path = row["VIS"]
        wv_path = row["WV"]

        # Open images
        ir_img = Image.open(ir_path).convert("RGB")
        vis_img = Image.open(vis_path).convert("RGB")
        wv_img = Image.open(wv_path).convert("RGB")

        # Apply transforms
        ir_tensor = self.transform(ir_img)
        vis_tensor = self.transform(vis_img)
        wv_tensor = self.transform(wv_img)

        # Return as dictionary (so model can handle multiple inputs)
        sample = {
            "IR": ir_tensor,
            "VIS": vis_tensor,
            "WV": wv_tensor,
            "datetime": row["datetime"]
        }

        return sample
