from PIL import Image

im = Image.open(r"pruebas/render_test.png")
w, h = im.size
# viewBox is -90 0 1853 1260 -> width 1853, height 1260
# scale factor:
sx = w / 1853
sy = h / 1260

def to_px(x, y):
    return int((x + 90) * sx), int(y * sy)

# Crop Adolfo Alsina & Viedma
# Layer1 transform: +112.9, +24.9
# In layer1, Alsina is ~1300-1650, y=700-950
# Root coords: ~1412-1762, y=725-975
x1, y1 = to_px(1350, 700)
x2, y2 = to_px(1780, 980)
crop1 = im.crop((x1, y1, x2, y2))
crop1.save(r"pruebas/crop_alsina_viedma.png")

# Crop 9 de Julio
# Root coords: ~700-1000, y=550-1120
x1, y1 = to_px(650, 550)
x2, y2 = to_px(1050, 1150)
crop2 = im.crop((x1, y1, x2, y2))
crop2.save(r"pruebas/crop_9dejulio.png")

print("Crops saved successfully!")
