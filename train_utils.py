# train_utils.py
import torch

def train_step(model, data_loader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    for images, times in data_loader:
        images, times = images.to(device), times.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, times)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    return running_loss / len(data_loader)
