from PIL import Image

im = Image.open(r"pruebas/test_fixed.png")
w, h = im.size
sx = w / 1853
sy = h / 1260
def to_px(x, y):
    return int((x + 90) * sx), int(y * sy)

# Crop Valcheta
crop = im.crop((to_px(850, 550)[0], to_px(850, 550)[1], to_px(1150, 950)[0], to_px(1150, 950)[1]))
crop.save(r"pruebas/test_crop_valcheta.png")
print("Valcheta crop saved!")
