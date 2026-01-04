from __future__ import print_function, division, absolute_import

import imageio

import imgaug as ia
import imgaug.augmenters as iaa
from imgaug._downloader import download

def main():
    aug = iaa.BlendAlphaMask(
        iaa.SomeColorsMaskGen(),
        iaa.OneOf([
            iaa.TotalDropout(1.0),
            iaa.AveragePooling(8)
        ])
    )

    aug2 = iaa.BlendAlphaSomeColors(iaa.OneOf([
            iaa.TotalDropout(1.0),
            iaa.AveragePooling(8)
    ]))

    files = [
        'data/320px-Vincent_van_Gogh-Wheatfield.jpg',
        'data/320px-Sarcophilus_harrisii_taranna.jpg',
        'data/207px-Galerella_sanguinea_Zoo_Praha_2011-2.jpg',
        'data/307px-Ambrosius_Bosschaert_the_Elder-Flower_Still_Life.jpg',
    ]

    for file in files:
        img = imageio.imread(download(file))
        ia.imshow(ia.draw_grid(aug(images=[img]*25), cols=5, rows=5))
        ia.imshow(ia.draw_grid(aug2(images=[img]*25), cols=5, rows=5))


if __name__ == "__main__":
    main()
