# Fix error in `arithmetic._add_scalar_to_uint8_` on Windows

On Python 3.8 tests for `_add_scalar_to_uint8_` fail for
windows due to dimension and dtype-specific behavior
in `cv2.add`.

The fix the errors by directly adding scalar values
if the input image is 2D or 3D with a singular channel
dimension.

If channel-dependent is required, broadcast the values
to full image shape and add it via `cv2.add`.