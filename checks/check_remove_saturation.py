import imageio

import imgaug as ia
import imgaug.augmenters as iaa
from imgaug._downloader import download

def main():
    files = [
        'data/320px-Sarcophilus_harrisii_taranna.jpg',
        'data/320px-Vincent_van_Gogh-Wheatfield.jpg',
        'data/207px-Galerella_sanguinea_Zoo_Praha_2011-2.jpg',
        'data/307px-Ambrosius_Bosschaert_the_Elder-Flower_Still_Life.jpg',
    ]

    for file in files:
        image = imageio.imread(download(file))

        aug = iaa.RemoveSaturation()
        images_aug = aug(images=[image] * (5*5))

        ia.imshow(ia.draw_grid(images_aug))


if __name__ == "__main__":
    main()
