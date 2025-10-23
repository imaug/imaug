from __future__ import print_function, division

import imageio

import imgaug as ia
from imgaug import augmenters as iaa
from _downloader import download


def main():
    image = imageio.imread(download('data/Kukle_Czech_Republic.jpg'))
    augs = [
        ("iaa.SnowflakesLayer()", iaa.SnowflakesLayer(
            density=0.05, density_uniformity=0.5, flake_size=0.9, flake_size_uniformity=0.5,
            angle=(-45, 45), speed=(0.001, 0.04), blur_sigma_fraction=(0.75*0.0001, 0.75*0.001))
         )
    ]

    for descr, aug in augs:
        print(descr)
        images_aug = aug.augment_images([image] * 64)
        ia.imshow(ia.draw_grid(images_aug))


if __name__ == "__main__":
    main()
