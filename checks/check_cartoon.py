import sys
from pathlib import Path

import imgaug as ia
import imgaug.augmenters as iaa
import imageio

sys.path.append(str(Path(__file__).parent))
from _downloader import download


def main():
    data_small = [
        "data/320px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
        "data/320px-Barack_Obama_family_portrait_2011.jpg",
        "data/320px-Pahalgam_Valley.jpg",
        "data/320px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg",
        "data/320px-Salad_platter.jpg",
        "data/287px-Squirrel_posing.jpg",
    ]
    data_medium = [
        "data/640px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
        "data/640px-Barack_Obama_family_portrait_2011.jpg",
        "data/640px-Pahalgam_Valley.jpg",
        "data/640px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg",
        "data/640px-Salad_platter.jpg",
        "data/574px-Squirrel_posing.jpg",
    ]
    data_large = [
        "data/1024px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
        "data/1024px-Barack_Obama_family_portrait_2011.jpg",
        "data/1024px-Pahalgam_Valley.jpg",
        "data/1024px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg",
        "data/1024px-Salad_platter.jpg",
    ]

    for dataset in [data_small, data_medium, data_large]:
        for d in dataset:
            image = imageio.imread(download(d))

            augs = [image] + iaa.Cartoon()(images=[image] * 15)
            ia.imshow(ia.draw_grid(augs, 4, 4))


if __name__ == "__main__":
    main()
