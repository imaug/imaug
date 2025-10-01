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
    'data/320px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg': "d908fc66615471e69b1c7bf4827edb207c26cb7ad538faa7c39775848475622a",
    'data/320px-Barack_Obama_family_portrait_2011.jpg': "894dab97ed3797b4e1e80a279091ef10edffc344595618d58ff9cbb2650211c7",
    'data/320px-Pahalgam_Valley.jpg': "ec1b98555fd4f2feca5aa7244406346c574c6f7a6bb14ec2f823360c72258793",
    'data/320px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg': "baa22a9e6f6e0310b45ee616117b8b8b669a0143a495ee2ef8acd897b1e6c6db",
    'data/320px-Salad_platter.jpg': "de7cd9c4a241a3a3c67c66e1c6f824ad5fdc45bbbea791dbfe1e3024f190f810",
    'data/287px-Squirrel_posing.jpg': "98a8e70d5295c355f2f51c54dfed901c94de122476cc566b9ae3bd792587897b",
    'data/640px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg': "e2b752a9f9297c4bd85e0eff822adecf8969a2d8a5d80800b512c59956a2dc59",
    'data/640px-Barack_Obama_family_portrait_2011.jpg': "694bdfa419e3f23cc5bbb64b9ee9e356f303227b28d852c1767b9f91370a49ff",
    'data/640px-Pahalgam_Valley.jpg': "023df6e7c7aca74ac653f5a1bfad11dbbb00f077bf752bd042bc393b02ccb73a",
    'data/640px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg': "a6a8d2e18df32ec2bca8336440c6f91da2e3ccc95781e65f20595c975783739b",
    'data/640px-Salad_platter.jpg': "19629c6cca80fa02b34a9d2eac9ae70ecddd4735247540acfdcf442c6d344268",
    'data/574px-Squirrel_posing.jpg': "986e04d38ff5c840d47068749e295e922dc165391a3101c5ae15bec7d3a0b24c",
    'data/1024px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg': "4654327c4c1dae72e8afb79daec326c0d5be4a91041b432cb3a46da317991097",
    'data/1024px-Barack_Obama_family_portrait_2011.jpg': "e522de65af56227747afae2cad43d3cef441269333576bdc4833c68b65a2fef3",
    'data/1024px-Pahalgam_Valley.jpg': "154ffbb23c53431ceb6567681986c8ab76f37b71f0fcdb4af24330639b4d50d4",
    'data/1024px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg': "37682593507d49140e6cf52fa04f2b3d38f2d2ca46a0de4e3d3dffb0a601e69f",
    'data/1024px-Salad_platter.jpg': "e3bd71241fabe6e35fb19864fb808e662301c5adbf1bee5084aacf8ac1889242",




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
    'data/320px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg/320px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
    'data/320px-Barack_Obama_family_portrait_2011.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Barack_Obama_family_portrait_2011.jpg/320px-Barack_Obama_family_portrait_2011.jpg",
    'data/320px-Pahalgam_Valley.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Pahalgam_Valley.jpg/320px-Pahalgam_Valley.jpg",
    'data/320px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Iglesia_de_Nuestra_Se%C3%B1ora_de_La_Blanca%2C_Cardej%C3%B3n%2C_Espa%C3%B1a%2C_2012-09-01%2C_DD_02.JPG/320px-Iglesia_de_Nuestra_Se%C3%B1ora_de_La_Blanca%2C_Cardej%C3%B3n%2C_Espa%C3%B1a%2C_2012-09-01%2C_DD_02.JPG",
    'data/320px-Salad_platter.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Salad_platter.jpg/320px-Salad_platter.jpg",
    'data/287px-Squirrel_posing.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Squirrel_posing.jpg/287px-Squirrel_posing.jpg",
    'data/640px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg/640px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
    'data/640px-Barack_Obama_family_portrait_2011.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Barack_Obama_family_portrait_2011.jpg/640px-Barack_Obama_family_portrait_2011.jpg",
    'data/640px-Pahalgam_Valley.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Pahalgam_Valley.jpg/640px-Pahalgam_Valley.jpg",
    'data/640px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Iglesia_de_Nuestra_Se%C3%B1ora_de_La_Blanca%2C_Cardej%C3%B3n%2C_Espa%C3%B1a%2C_2012-09-01%2C_DD_02.JPG/640px-Iglesia_de_Nuestra_Se%C3%B1ora_de_La_Blanca%2C_Cardej%C3%B3n%2C_Espa%C3%B1a%2C_2012-09-01%2C_DD_02.JPG",
    'data/640px-Salad_platter.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Salad_platter.jpg/640px-Salad_platter.jpg",
    'data/574px-Squirrel_posing.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Squirrel_posing.jpg/574px-Squirrel_posing.jpg",
    'data/1024px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg/1024px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg",
    'data/1024px-Barack_Obama_family_portrait_2011.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Barack_Obama_family_portrait_2011.jpg/1024px-Barack_Obama_family_portrait_2011.jpg",
    'data/1024px-Pahalgam_Valley.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Pahalgam_Valley.jpg/1024px-Pahalgam_Valley.jpg",
    'data/1024px-Iglesia_de_Nuestra_Señora_de_La_Blanca.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Iglesia_de_Nuestra_Se%C3%B1ora_de_La_Blanca%2C_Cardej%C3%B3n%2C_Espa%C3%B1a%2C_2012-09-01%2C_DD_02.JPG/1024px-Iglesia_de_Nuestra_Se%C3%B1ora_de_La_Blanca%2C_Cardej%C3%B3n%2C_Espa%C3%B1a%2C_2012-09-01%2C_DD_02.JPG",
    'data/1024px-Salad_platter.jpg':
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Salad_platter.jpg/1024px-Salad_platter.jpg",
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
