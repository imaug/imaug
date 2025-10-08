# Table of Contents

1. [Overview](#overview)
2. [Changed](#changed)
3. [Refactored](#refactored)
4. [Fixed](#fixed)
5. [Improved](#improved)

# Overview

# Changed

# Refactored

# Fixed

## Verified checks [?]
* Follow SciPy and scikit-image example by adding pooch caching for example data download from wikipedia for
    * `check_clouds.py`
    * `check_blendalphasomecolors.py`
    * `check_cartoon.py`
    * `check_fast_snowy_landscape.py`
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

# Improved
