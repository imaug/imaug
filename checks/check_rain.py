from __future__ import print_function, division, absolute_import
import imageio

import imgaug as ia
from imgaug import augmenters as iaa

from _downloader import download


def main():
    augs = [
        iaa.Rain(speed=(0.1, 0.3)),
        iaa.Rain(),
        iaa.Rain(drop_size=(0.1, 0.2))
    ]

    image = imageio.imread(download('data/Kukle_Czech_Republic.jpg'))

    for aug, size in zip(augs, [0.1, 0.2, 1.0]):
        image_rs = ia.imresize_single_image(image, size, "cubic")
        print(image_rs.shape)

        images_aug = aug.augment_images([image_rs] * 64)
        ia.imshow(ia.draw_grid(images_aug))


if __name__ == "__main__":
    main()
