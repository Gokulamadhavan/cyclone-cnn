import torch
import torch.nn as nn
import torch.nn.functional as F

class SatelliteCNN(nn.Module):
    def __init__(self, num_classes=2):
        super(SatelliteCNN, self).__init__()

        # CNN for IR
        self.ir_cnn = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        # CNN for VIS
        self.vis_cnn = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        # CNN for WV
        self.wv_cnn = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        # After conv layers, feature size is (32, 32, 32) for input 128x128
        self.fc = nn.Sequential(
            nn.Linear(32*32*32*3, 256),   # 3 branches concatenated
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes)
        )

    def forward(self, x_ir, x_vis, x_wv):
        ir_feat = self.ir_cnn(x_ir)
        vis_feat = self.vis_cnn(x_vis)
        wv_feat = self.wv_cnn(x_wv)

        # Flatten
        ir_feat = ir_feat.view(ir_feat.size(0), -1)
        vis_feat = vis_feat.view(vis_feat.size(0), -1)
        wv_feat = wv_feat.view(wv_feat.size(0), -1)

        # Concatenate
        combined = torch.cat((ir_feat, vis_feat, wv_feat), dim=1)

        # Fully connected
        out = self.fc(combined)
        return out
