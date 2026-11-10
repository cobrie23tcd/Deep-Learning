import torch                                      # The main PyTorch library
import torch.nn as nn                             # Contains pytorch network building blocks (e.g., layers)
import torch.nn.functional as F                   # Contains functions for neural network operations (e.g., activation functions)

class SimpleNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()

        # here we define all the layers/transformations being used.
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(3*32*32, 1024)
        self.bn1 = nn.BatchNorm1d(1024)
        self.fc2 = nn.Linear(1024, 512)
        self.bn2 = nn.BatchNorm1d(512)
        self.fc3 = nn.Linear(512, 256)
        self.bn3 = nn.BatchNorm1d(256)
        self.fc4 = nn.Linear(256, num_classes)
        self.dropout = nn.Dropout(0.5)


    def forward(self, x):
        # here define the forward transformation, using builtin pytorch calls
        # and also the layers defined in __init__

        x = self.flatten(x)
        x = self.dropout(F.relu(self.bn1(self.fc1(x))))
        x = self.dropout(F.relu(self.bn2(self.fc2(x))))
        x = self.dropout(F.relu(self.bn3(self.fc3(x))))
        x = self.fc4(x)

        # Note that we are missing here the last Softmax layer.
        # In PyTorch, the last softmax layer is automatically included
        # in the nn.CrossEntropyLoss(). So do not define it here.
        # Your output tensor is simply expected to contain the logits for each
        # class.

        return x
