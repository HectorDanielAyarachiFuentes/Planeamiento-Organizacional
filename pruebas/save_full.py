from PIL import Image

im = Image.open(r"pruebas/test_fixed.png")
# Let's save a reasonably-sized version to inspect the entire map
im_small = im.resize((1200, 816), Image.Resampling.LANCZOS)
im_small.save(r"pruebas/full_map_test.png")
print("Full map saved to pruebas/full_map_test.png")
