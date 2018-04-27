from __future__ import print_function, division, absolute_import

from .models import *


class SRLConvolutionalNetwork(BaseModelSRL):
    """
    Convolutional Neural Net for State Representation Learning (SRL)
    input shape : 3-channel RGB images of shape (3 x H x W), where H and W are expected to be at least 224
    :param state_dim: (int)
    :param cuda: (bool)
    :param noise_std: (float)  To avoid NaN (states must be different)
    """

    def __init__(self, state_dim=2, cuda=False, noise_std=1e-6):
        super(SRLConvolutionalNetwork, self).__init__()
        self.resnet = models.resnet18(pretrained=True)
        # TODO: add squeezeNet support
        # self.squeezeNet = models.squeezenet1_0(pretrained=True)
        # TODO: freeze less layers
        # Freeze params
        for param in self.resnet.parameters():
            param.set_grad_enabled(False)

        self.device = torch.device("cuda" if torch.cuda.is_available() and cuda else "cpu")
        # Replace the last fully-connected layer
        n_units = self.resnet.fc.in_features
        print("{} units in the last layer".format(n_units))
        self.resnet.fc = nn.Linear(n_units, state_dim)
        self.resnet.to(self.device)
        # This variant does not require the batch_size
        self.noise = GaussianNoiseVariant(self.device, noise_std)
        # self.noise = GaussianNoise(batch_size, state_dim, self.device, noise_std)

    def forward(self, x):
        x = self.resnet(x)
        if self.training:
            x = self.noise(x)
        return x


class SRLCustomCNN(BaseModelSRL):
    """
    Convolutional Neural Network for State Representation Learning
    input shape : 3-channel RGB images of shape (3 x H x W), where H and W are expected to be at least 224
    :param state_dim: (int)
    :param cuda: (bool)
    :param noise_std: (float)  To avoid NaN (states must be different)
    """

    def __init__(self, state_dim=2, cuda=False, noise_std=1e-6):
        super(SRLCustomCNN, self).__init__()
        self.cnn = CustomCNN(state_dim)
        self.device = torch.device("cuda" if torch.cuda.is_available() and cuda else "cpu")
        self.cnn.to(self.device)
        self.noise = GaussianNoiseVariant(self.device, noise_std)

    def forward(self, x):
        x = self.cnn(x)
        if self.training:
            x = self.noise(x)
        return x


class SRLDenseNetwork(BaseModelSRL):
    """
    Dense Neural Net for State Representation Learning (SRL)
    input shape : 3-channel RGB images of shape (3 x H x W) (to be consistent with CNN network)
    :param input_dim: (int) 3 x H x H
    :param state_dim: (int)
    :param noise_std: (float)  To avoid NaN (states must be different)
    :param batch_size: (int)
    :param cuda: (bool)
    :param n_hidden: (int)
    """

    def __init__(self, input_dim, state_dim=2, batch_size=256,
                 cuda=False, n_hidden=32, noise_std=1e-6):
        super(SRLDenseNetwork, self).__init__()

        self.device = torch.device("cuda" if torch.cuda.is_available() and cuda else "cpu")

        self.fc1 = nn.Linear(input_dim, n_hidden)
        self.fc2 = nn.Linear(n_hidden, state_dim)
        self.noise = GaussianNoiseVariant(self.device, noise_std)
        # self.noise = GaussianNoise(batch_size, state_dim, self.device, noise_std)

    def forward(self, x):
        # Flatten input
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        if self.training:
            x = self.noise(x)
        return x
