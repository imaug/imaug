import imgaug

try:
    import pooch
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "This check downloads online files. In order to keep the load on "
        "the external servers minimal, the installation of an optional "
        "dependency, pooch, is required."
    )

registry = {
    'data/Kukle_Czech_Republic.jpg': "261d05b7479abff17af7762777aee1ccfa72959038a11af3457decb6ef443852",
    'data/320px-Sarcophilus_harrisii_taranna.jpg': "6d15eea0afe42ccd7a74b64545f1cbb32ea21f4b715ec1a3eb89420bd6deeec4",
    'data/320px-Vincent_van_Gogh-Wheatfield.jpg': "aa3ad2e2d21b624c8439d267e9bb49db65f9bb4d73e20977dae0ed2adfd56fed",
    'data/207px-Galerella_sanguinea_Zoo_Praha_2011-2.jpg': "81c05232db8738659c4b342051cb441880dbf2bf36d3927903a94bf4de5a20a6",
    'data/307px-Ambrosius_Bosschaert_the_Elder-Flower_Still_Life.jpg': "f09220ca1a44155a08ffd94441a69e617f2b27bd3719d66c395a6cdd108926bc",
}
urls = {
    'data/Kukle_Czech_Republic.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/8/89/Kukle%2CCzech_Republic..jpg",
    'data/320px-Vincent_van_Gogh-Wheatfield.jpg': 
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Vincent_van_Gogh_-_Wheatfield_with_crows_-_Google_Art_Project.jpg/320px-Vincent_van_Gogh_-_Wheatfield_with_crows_-_Google_Art_Project.jpg",
    'data/320px-Sarcophilus_harrisii_taranna.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Sarcophilus_harrisii_taranna.jpg/320px-Sarcophilus_harrisii_taranna.jpg",
    'data/207px-Galerella_sanguinea_Zoo_Praha_2011-2.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Galerella_sanguinea_Zoo_Praha_2011-2.jpg/207px-Galerella_sanguinea_Zoo_Praha_2011-2.jpg",
    'data/307px-Ambrosius_Bosschaert_the_Elder-Flower_Still_Life.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Ambrosius_Bosschaert_the_Elder_%28Dutch_-_Flower_Still_Life_-_Google_Art_Project.jpg/307px-Ambrosius_Bosschaert_the_Elder_%28Dutch_-_Flower_Still_Life_-_Google_Art_Project.jpg",
}


downloader = pooch.HTTPDownloader(headers={"User-Agent": 'imaug (https://github.com/imaug/imaug)'})
image_fetcher = pooch.create(
    base_url = "",
    path=pooch.os_cache("imaug"),
    version = imgaug.__version__,
    version_dev="main",
    registry = registry,
    urls = urls,
    env="IMAUG_DATADIR",
)

def download(filename):
    return image_fetcher.fetch(filename, downloader=downloader)
