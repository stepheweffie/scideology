import pandas as pd
import d6tflow
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import json
import torchaudio
import torch
from torchaudio.transforms import MFCC


def preprocess_audio(audio_path, transcription, sample_rate=16000):

    # Load audio waveform
    waveform, _ = torchaudio.load(audio_path, normalize=True, num_frames=16000)

    # Resample to the desired sample rate
    waveform = torchaudio.transforms.Resample(orig_freq=waveform.size(1), new_freq=sample_rate)(waveform)

    # Extract MFCC features
    mfcc_transform = MFCC(
        sample_rate=sample_rate,
        n_mfcc=13,  # Number of MFCC coefficients
        melkwargs={'n_fft': 400, 'hop_length': 160, 'n_mels': 23, 'center': False}
    )
    mfcc_features = mfcc_transform(waveform)

    # Normalize MFCC features
    mfcc_features = (mfcc_features - mfcc_features.mean(dim=-1, keepdim=True)) / mfcc_features.std(dim=-1, keepdim=True)

    # Tokenize the transcription (replace this with your actual tokenization method)
    # For simplicity, we'll just convert the transcription to lowercase and split by spaces
    tokens = transcription.lower().split()

    return {'audio': mfcc_features, 'transcription': tokens}


class LoadJson(d6tflow.tasks.TaskCache):
    filename = d6tflow.Parameter()

    def run(self):
        # Load the JSON file
        data = pd.read_json(self.filename)

        # Save the loaded data
        self.save(data)


class GetData(d6tflow.tasks.TaskCache):
    version = 0

    def requires(self):
        # Load the JSON file
        return LoadJson(filename="data.json")

    def run(self):
        # Access the output of the LoadJson task
        loaded_data = self.input().load()

        # Perform any further processing if needed
        # For example, you can apply transformations to the loaded data

        # Save the processed data
        self.save(loaded_data)


# Define your PyTorch model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)


# Define a PyTorch task for loading data
class LoadDataTask(d6tflow.tasks.TaskCache):
    def run(self):
        # Load data from the JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)

        # Extract audio paths and transcriptions
        audio_paths = [item['audio'] for item in data]
        transcriptions = [item['transcription'] for item in data]

        # Split the data into training and test sets
        train_size = int(0.8 * len(audio_paths))
        train_paths, test_paths = audio_paths[:train_size], audio_paths[train_size:]
        train_transcriptions, test_transcriptions = transcriptions[:train_size], transcriptions[train_size:]

        # For simplicity, create random tensors as placeholders
        X_train = torch.randn((len(train_paths), 10))
        y_train = torch.randn((len(train_transcriptions), 1))
        X_test = torch.randn((len(test_paths), 10))
        y_test = torch.randn((len(test_transcriptions), 1))

        self.save({'X_train': X_train, 'y_train': y_train, 'X_test': X_test, 'y_test': y_test})


# Define a PyTorch task for model training
class TrainModelTask(d6tflow.tasks.PyTorchTask):

    def requires(self):
        return LoadDataTask()

    def model(self):
        return SimpleModel()

    def criterion(self):
        return nn.MSELoss()

    def optimizer(self):
        return optim.SGD(self.model().parameters(), lr=0.01)

    def batch_size(self):
        return 32

    def epochs(self):
        return 10

    def train_loader(self):
        data = self.input()
        return DataLoader(TensorDataset(data['X_train'], data['y_train']), batch_size=self.batch_size(), shuffle=True)

    def test_loader(self):
        data = self.input()
        return DataLoader(TensorDataset(data['X_test'], data['y_test']), batch_size=self.batch_size(), shuffle=False)


# Run the workflow
if __name__ == "__main__":
    # Example usage
    audio_path = 'path/to/audio.wav'
    transcription = "Hello, how are you?"
    preprocessed_data = preprocess_audio(audio_path, transcription)
    d6tflow.run(TrainModelTask())

