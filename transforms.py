from PIL import Image
from torchvision import transforms
from torchvision.transforms import functional as TF
import torch
import matplotlib.pyplot as plt

path = "/Users/wguo/GitRepo/dl-image-classification/train_full/9inches_dirty/9inches_dirty_1.bmp"
img = Image.open(path)
img

transforms = transforms.Compose([
    transforms.Resize(255),
    transforms.ColorJitter(),
    transforms.CenterCrop(200),
    #transforms.RandomCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.Resize(200),
    transforms.ToTensor(),
    transforms.ToPILImage()
])

img = transforms(img)
plt.imshow(img)
plt.show()
