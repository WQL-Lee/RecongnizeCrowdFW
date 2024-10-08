from torchvision import datasets, transforms

# import sys
# sys.path.append(".")

from base import BaseDataLoader
from .dataset import ShangHaiTechDataset


# class MnistDataLoader(BaseDataLoader):
#     """
#     MNIST data loading demo using BaseDataLoader
#     """
#     def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
#         trsfm = transforms.Compose([
#             transforms.ToTensor(),
#             transforms.Normalize((0.1307,), (0.3081,))
#         ])
#         self.data_dir = data_dir
#         self.dataset = datasets.MNIST(self.data_dir, train=training, download=True, transform=trsfm)
#         super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)

class ShanghaiTechDataLoader(BaseDataLoader):
    def __init__(self, data_dir, crop_size, downsample, method, is_gray, unit_size, pre_resize, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        self.data_dir = data_dir
        self.dataset = ShangHaiTechDataset(self.data_dir, crop_size, downsample, method, is_gray, unit_size, pre_resize)
        super(ShanghaiTechDataLoader, self).__init__(self.dataset, batch_size, shuffle, validation_split, num_workers, self.dataset.collate)

if __name__=="__main__":
    data_dir="data/processed/ShanghaiTechA"
    crop_size=320
    downsample=1
    method="train"
    is_gray=False
    unit_size=1
    pre_resize=1
    batch_size=16
    shuffle=True
    validation_split=0.0
    num_workers=1
    training=True
    sht = ShanghaiTechDataLoader(data_dir, crop_size, downsample, method, is_gray, unit_size, pre_resize, batch_size)
    print(len(sht.dataset))