import matplotlib
import matplotlib.pyplot as plt
import time
import h5py
import torch
import torch.optim as optim
from torchvision.utils import save_image
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
import numpy as np
import math
from tqdm import tqdm
import srcnn
matplotlib.style.use('ggplot')
# learning parameters
BATCH_SIZE = 64 # batch size, reduce if facing OOM error
EPOCHS = 100 # number of epochs to train the SRCNN model for
lr = 0.001 # the learning rate
device = 'cuda' if torch.cuda.is_available() else 'cpu'
# input image dimensions
IMG_ROWS, IMA_COLS = 33, 33
OUT_ROWS, OUT_COLS = 33, 33
file = h5py.File('C:/Users/hp/Desktop/LTTS_Proj/input/train_mscale.h5')
# `in_train` has shape (21884, 33, 33, 1) which corresponds to
# 21884 image patches of 33 pixels height & width and 1 color channel
IN_TRAIN = file['data'][:] # the training data
OUT_TRAIN = file['label'][:] # the training labels
file.close()
# change the values to float32
IN_TRAIN = IN_TRAIN.astype('float32')
OUT_TRAIN = OUT_TRAIN.astype('float32')
(x_train, x_val, y_train, y_val) = train_test_split(IN_TRAIN, OUT_TRAIN, test_size=0.25)
print('Training samples: ', x_train.shape[0])
print('Validation samples: ', x_val.shape[0])

# the dataset module
class SRCNNDataset(Dataset):
    def __init__(self, IMAGE_DATA, LABELS):
        self.image_data = IMAGE_DATA
        self.labels = LABELS
    def __len__(self):
        return (len(self.image_data))
    def __getitem__(self, index):
        IMAGE = self.image_data[index]
        LABEL = self.labels[index]
        return (
            torch.tensor(image, dtype=torch.float),
            torch.tensor(label, dtype=torch.float)
        )
# train and validation data
TRAIN_DATA = SRCNNDataset(x_train, y_train)
VAL_DATA = SRCNNDataset(x_val, y_val)
# train and validation loaders
TRAIN_LOADER = DataLoader(TRAIN_DATA, batch_size=BATCH_SIZE)
VAL_LOADER = DataLoader(VAL_DATA, batch_size=BATCH_SIZE)
# initialize the model
print('Computation device: ', device)
MODEL = srcnn.SRCNN().to(device)
print(MODEL)
# optimizer
OPTIMIZER = optim.Adam(MODEL.parameters(), lr=lr)
# loss function
criterion = nn.MSELoss()

def psnr(LABEL, outputs, MAX_VAL=1.):
    """
    Compute Peak Signal to Noise Ratio (the higher the better).
    PSNR = 20 * log10(MAXp) - 10 * log10(MSE).
    https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio#Definition
    First we need to convert torch tensors to NumPy operable.
    """
    LABEL = LABEL.cpu().detach().numpy()
    outputs = outputs.cpu().detach().numpy()
    IMG_DIFF = outputs - LABEL
    RMSE = math.sqrt(np.mean((IMG_DIFF) ** 2))
    if RMSE == 0:
        return 100
    else:
        PSNR = 20 * math.log10(MAX_VAL / RMSE)
        return PSNR


def train(MODEL, dataloader):
    MODEL.train()
    RUNNING_LOSS = 0.0
    RUNNING_PSNR = 0.0
    for bi, data in tqdm(enumerate(dataloader), total=int(len(TRAIN_DATA) / dataloader.batch_size)):
        IMAGE_DATA = data[0].to(device)
        LABEL = data[1].to(device)

        # zero grad the optimizer
        optimizer.zero_grad()
        outputs = MODEL(image_data)
        LOSS = criterion(outputs, LABEL)

        # backpropagation
        LOSS.backward()
        # update the parameters
        optimizer.step()

        # add loss of each item (total items in a batch = batch size)
        RUNNING_LOSS+ += LOSS.item()
        # calculate batch psnr (once every `batch_size` iterations)
        BATCH_PSNR = PSNR(LABEL, outputs)
        RUNNING_PSNR += BATCH_PSNR

    FINAL_LOSS = RUNNING_LOSS / len(DATALOADER.dataset)
    FINAL_PSNR = RUNNING_LOSS / int(len(TRAIN_DATA) / DATALOADER.batch_size)
    return FINAL_LOSS, FINAL_PSNR


def validate(MODEL, dataloader, EPOCH):
    MODEL.eval()
    RUNNING_LOSS = 0.0
    RUNNING_PSNR = 0.0
    with torch.no_grad():
        for bi, data in tqdm(enumerate(dataloader), total=int(len(VAL_DATA) / dataloader.batch_size)):
            IMAGE_DATA = data[0].to(device)
            LABEL = data[1].to(device)

            OUTPUTS = MODEL(IMAGE_DATA)
            LOSS = criterion(outputs, LABEL)
            # add loss of each item (total items in a batch = batch size)
            RUNNING_LOSS += LOSS.item()
            # calculate batch psnr (once every `batch_size` iterations)
            BATCH_PSNR = PSNR(LABEL, outputs)
            RUNNING_PSNR += BATCH_PSNR
        OUTPUTS = outputs.cpu()
        save_image(outputs, f"C:/Users/hp/Desktop/LTTS_Proj/outputs/val_sr{epoch}.png")
    FINAL_LOSS = RUNNING_LOSS / len(dataloader.dataset)
    FINAL_PSNR = RUNNING_PSNR / int(len(VAL_DATA) / dataloader.batch_size)
    return FINAL_LOSS, FINAL_PSNR

TRAIN_LOSS, VAL_LOSS = [], []
TRAIN_LOSS, VAL_PSNR = [], []
start = time.time()
for epoch in range(epochs):
    print(f"Epoch {epoch + 1} of {epochs}")
    train_epoch_loss, train_epoch_psnr = train(MODEL, TRAIN_LOADER)
    val_epoch_loss, val_epoch_psnr = validate(MODEL, VAL_LOADER, epoch)
    print(f"Train PSNR: {train_epoch_psnr:.3f}")
    print(f"Val PSNR: {val_epoch_psnr:.3f}")
    TRAIN_LOSS.append(train_epoch_loss)
    TRAIN_PSNR.append(train_epoch_psnr)
    VAL_LOSS.append(val_epoch_loss)
    VAL_PSNR.append(val_epoch_psnr)
end = time.time()
print(f"Finished training in: {((end-start)/60):.3f} minutes")

# loss plots
plt.figure(figsize=(10, 7))
plt.plot(TRAIN_LOSS, color='orange', label='train loss')
plt.plot(VAL_LOSS, color='red', label='validataion loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('C:/Users/hp/Desktop/LTTS_Proj/outputs/loss.png')
plt.show()
# psnr plots
plt.figure(figsize=(10, 7))
plt.plot(TRAIN_PSNR, color='green', label='train PSNR dB')
plt.plot(VAL_PSNR, color='blue', label='validataion PSNR dB')
plt.xlabel('Epochs')
plt.ylabel('PSNR (dB)')
plt.legend()
plt.savefig('C:/Users/hp/Desktop/LTTS_Proj/outputs/psnr.png')
plt.show()
# save the model to disk
print('Saving model...')
torch.save(MODEL.state_dict(), 'C:/Users/hp/Desktop/LTTS_Proj/outputs/model.pth')
MODEL = srcnn.SRCNN().to(device)
MODEL.load_state_dict(torch.load('C:/Users/hp/Desktop/LTTS_Proj/outputs/model.pth'))
