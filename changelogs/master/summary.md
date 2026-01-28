# Table of Contents

1. [Overview](#overview)
2. [Changed](#changed)
3. [Refactored](#refactored)
4. [Fixed](#fixed)
5. [Improved](#improved)

# Overview

# Changed
## `RandAugment` `random_state` handling [#19](https://github.com/imaug/imaug/pull/19)
The class `RandAugment` handled the parameter `random_state` inconsistently for
its parent class `meta.Sequential`. This resulted in assertion errors once it
was set. Instead of overwriting `seed` and keeping the provided `random_state`,
the new version resets `random_state` to `'depreciated'` once `seed` is
overwritten. Additionally, a new test case is added to check the new behavior.

## `_blend_alpha_uint8_single_alpha_` always returns copies [#23](https://github.com/imaug/imaug/pull/23)
The inplace modification of `image_fg` caused errors when applied on non-C-contiguous views.
Thus, the function was changed such that it always returns copies, even when called with `inplace=True`.
It was verfied that calling functions do not rely on inplace modifications for proper functionality.

## Moved image `_downloader.py` from `checks` to `imgaug` [#21](https://github.com/imaug/imaug/pull/21)
For creating the example images for the documentation it is necessary to download online sample images
similar to the workflow for the checks. Instead of copy the `download` function for the documentation, 
the function was moved to serve as a general utility function for the library.

## Add `beautifulsoup4` as explicit dependency for building the documentation [#21](https://github.com/imaug/imaug/pull/21)
The dependency `dashtable.html2rst` depends on `beautifulsoup4` as optional dependency.

# Refactored

## Add cached downloader to example image creation for documentation [#21](https://github.com/imaug/imaug/pull/21)
Added `pooch` caching for online data to the example creation scripts
* `generate_main_repo_readme_images.py`
* `gen_v040_changelog_images.py`
* `gen_overview_artistic.py`
* `gen_overview_blend.py`
* `gen_overview_color.py`
* `gen_overview_weather.py`

## Change `utils` import in all scripts for rtd example images [#21](https://github.com/imaug/imaug/pull/21)
Without a `imaug-docs` package there are no realtive imports allowed. Thus the utilities need to be imported
by a standard local import call.

# Fixed

## Verified checks [#19](https://github.com/imaug/imaug/pull/19)
* Follow SciPy and scikit-image example by adding pooch caching for example data download from wikipedia for
    * `check_clouds.py`
    * `check_blendalphasomecolors.py`
    * `check_cartoon.py`
    * `check_fast_snowy_landscape.py`
    * `check_fog.py`
    * `check_rain.py`
    * `check_remove_saturation.py`
    * `check_snowflakes.py`
    * `check_snowflakes_layer.py`
    * `check_voronoi.py`
    * `check_with_hue_and_saturation.py`
    
* Change depreciated `ia.quokka_square` to `ia.data.quokka_square` or similar for heatmaps and keypoints in 
    * `check_add_to_hue_and_saturation.py`
    * `check_brightness.py`
    * `check_canny.py`
    * `check_color_temperature.py`
    * `check_jigsaw.py`
    * `check_kmeans_color_quantization.py`
    * `check_mean_shift_blur.py`
    * `check_multiply_hue_and_saturation.py`
    * `check_noise.py`
    * `check_pooling.py`
    * `check_quantize_uniform_to_n_bits.py`
    * `check_rot90.py`
    * `check_solarize.py`
    * `check_uniform_color_quantization.py`

* In `check_cartoon.py` remove unnecessary imports and use all listed images.

* In `check_performance.py` replace non-working format string.
* In `check_polygons_stay_valid_during_augmentation.py` adapt to new min/max seed value locations.
* In `check_visually.py` keep image shape consistent for "Sequential" and "Sometimes" checks.
* Multiple fixes in `check_flip_performance.py`:
    * `cv2.flip` does not support `bool` and `uint32` data types anymore.
    * `cv2.flip` does not support `uint64` and `int64`, as well as Fortran-style output arrays.
    * `cv2.flip` returns NumPy arrays without a `get` attribute.
* In `check_multicore_pool.py` move local functions outside the main definition for multiprocessing.

## Correct the `__version__` string [#18](https://github.com/imaug/imaug/pull/18)

## Handling of non-c-contiguous views in `_blend_alpha_uint8_single_alpha_`[#23](https://github.com/imaug/imaug/pull/23)
The calling functions of `_blend_alpha_uint8_single_alpha_` do not always guarantee C-contiguous arrays base 
arrays (i.e. which own their data). This leads to problems when the function sets the `inplace`
parameter to `True`. In this case the `_normalize_cv2_input_arr_` makes sure that `image_fg` is a C-contiguous
base array when used as CV2 input, but does not change it when used as CV2 destination. This fix makes sure that
also the destination array matches the CV2 requirements, while sacrificing the (real) inplace modification of 
`image_fg`.

## Multiple fixes in `collect_dtype_support.py` [#21](https://github.com/imaug/imaug/pull/21)
Remove call for `matplotlib.Figure._cachedRenderer` and incorrectly masked regular expression
pattern.

## Fix incorrect dtype docstrings [#21](https://github.com/imaug/imaug/pull/21)
The script `collect_dtype_support.py` is very sensitive to incorrectly defined dtype docstrings.
Pull request [#640](https://github.com/aleju/imgaug/pull/640) introduced a circular look-up definition
in `imgaug.augmenters.segmentation`for the class `Voronoi`. Another problem was a misplacement of the
version added docstring in `imgaug.augmenters.arithmetrics` for the function `cutout` in
[#598](https://github.com/aleju/imgaug/pull/598).

# Improved

## Handling of views in `_multiply_elementwise_to_uint8_`[#19](https://github.com/imaug/imaug/pull/19)
The elementwise multiplication with `cv2.multiply` breaks if a
RGB image is sliced in the channel dimension and used as destination.
The error only seems to occur if the view's base shape has a singular first
dimension. Therefore a true copy of the image is used as destination instead.

## Enable dtype support matrix script on Windows [#21](https://github.com/imaug/imaug/pull/21)
The original `collect_dtype_support.py` script hard-coded the front-slash directory separator and
assumed a root suffix. Replaced it with the OS specific separator and make script more robust with respect
to relative directory definitions.

## Fix tempfile issue for readme image generation script[#21](https://github.com/imaug/imaug/pull/21)
According to https://stackoverflow.com/a/54768241 Windows struggles with `NamedTemporaryFile` without
the additional parameter `delete_on_close=False`.

## Store all generated documentation images in a single folder[#21](https://github.com/imaug/imaug/pull/21)
Moved and reorganized scripts for the example data generation and its outputs.
* `docs/scripts/images_documentation/collect_dtype_support.py` outputs to `docs/images/dtype_support/*.png`
* `docs/scripts/images_documentation/gen_*.py` outputs to `docs/images/**/*.jpg`
* `docs/scripts/tables_performance/*.py` outputs to `docs/measure_performance_results/results_*.pickle`
* `docs/scripts/images_changelogs/gen_v040_changelog_images.py` outputs to `docs/images/changelogs/0.4.0/*.jpg`
* `docs/scripts/images_readme/generate_main_repo_readme_images.py` outputs to `docs/images/readme_images/augmenter_videos/**/*.gif`
