from __future__ import print_function, division

import imageio

import imgaug as ia
from imgaug import augmenters as iaa
from imgaug._downloader import download

def main():
    image = imageio.imread(download('data/Kukle_Czech_Republic.jpg'))
    augs = [
        ("iaa.FastSnowyLandscape(64, 1.5)", iaa.FastSnowyLandscape(64, 1.5)),
        ("iaa.FastSnowyLandscape(128, 1.5)", iaa.FastSnowyLandscape(128, 1.5)),
        ("iaa.FastSnowyLandscape(200, 1.5)", iaa.FastSnowyLandscape(200, 1.5)),
        ("iaa.FastSnowyLandscape(64, 2.5)", iaa.FastSnowyLandscape(64, 2.5)),
        ("iaa.FastSnowyLandscape(128, 2.5)", iaa.FastSnowyLandscape(128, 2.5)),
        ("iaa.FastSnowyLandscape(200, 2.5)", iaa.FastSnowyLandscape(200, 2.5)),
        ("iaa.FastSnowyLandscape(64, 3.5)", iaa.FastSnowyLandscape(64, 3.5)),
        ("iaa.FastSnowyLandscape(128, 3.5)", iaa.FastSnowyLandscape(128, 3.5)),
        ("iaa.FastSnowyLandscape(200, 3.5)", iaa.FastSnowyLandscape(200, 3.5)),
        ("iaa.FastSnowyLandscape()", iaa.FastSnowyLandscape())
    ]

    for descr, aug in augs:
        print(descr)
        images_aug = aug.augment_images([image] * 64)
        ia.imshow(ia.draw_grid(images_aug))


if __name__ == "__main__":
    main()
