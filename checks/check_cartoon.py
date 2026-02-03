import imageio

import imgaug as ia
import imgaug.augmenters as iaa
from imgaug._downloader import download

def main():
    data_small = [
        "data/330px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
        "data/330px-Barack_Obama_family_portrait_2011.jpg",
        "data/330px-Pahalgam_Valley.jpg",
        "data/330px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg",
        "data/330px-Salad_platter.jpg",
        "data/250px-Squirrel_posing.jpg",
    ]
    data_medium = [
        "data/500px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
        "data/500px-Barack_Obama_family_portrait_2011.jpg",
        "data/500px-Pahalgam_Valley.jpg",
        "data/500px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg",
        "data/500px-Salad_platter.jpg",
        "data/500px-Squirrel_posing.jpg",
    ]
    data_large = [
        "data/960px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
        "data/960px-Barack_Obama_family_portrait_2011.jpg",
        "data/960px-Pahalgam_Valley.jpg",
        "data/960px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg",
        "data/960px-Salad_platter.jpg",
    ]

    for dataset in [data_small, data_medium, data_large]:
        for d in dataset:
            image = imageio.imread(download(d))

            augs = [image] + iaa.Cartoon()(images=[image] * 15)
            ia.imshow(ia.draw_grid(augs, 4, 4))


if __name__ == "__main__":
    main()
