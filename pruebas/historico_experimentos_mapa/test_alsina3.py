import re
import pymupdf
from PIL import Image

with open(r"pruebas/test_fixed.svg", "r", encoding="utf-8") as f:
    svg_content = f.read()

# Position test 3:
old_alsina = re.search(r'<text id="text2211"[^>]*>.*?</text>', svg_content, re.DOTALL).group(0)
new_alsina = '''<text id="text2211" y="758" x="1350" style="font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;font-size:32px;font-weight:700;letter-spacing:1px;fill:#0f2d59;fill-opacity:0.95;stroke:none;" xml:space="preserve"><tspan y="758" x="1350" id="tspan2213" sodipodi:role="line">Adolfo</tspan><tspan id="tspan2215" y="796" x="1350" sodipodi:role="line">Alsina</tspan></text>'''

old_viedma = re.search(r'<text id="text2207"[^>]*>.*?</text>', svg_content, re.DOTALL).group(0)
new_viedma = '''<text id="text2207" y="832" x="1535" style="font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;letter-spacing:0.5px;fill:#0f2d59;stroke:none;" xml:space="preserve" text-anchor="end"><tspan x="1535" y="832" style="font-family:'Segoe UI',Arial,sans-serif;font-size:20px;font-weight:800;fill:#0f2d59;">★ Viedma</tspan><tspan x="1535" y="854" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;fill:#c89632;">(Sede CURZAS)</tspan></text>'''

test_svg = svg_content.replace(old_alsina, new_alsina).replace(old_viedma, new_viedma)

with open(r"pruebas/test_fixed.svg", "w", encoding="utf-8") as f:
    f.write(test_svg)

doc = pymupdf.open(r"pruebas/test_fixed.svg")
pix = doc[0].get_pixmap(dpi=150)
pix.save(r"pruebas/test_fixed.png")

im = Image.open(r"pruebas/test_fixed.png")
w, h = im.size
sx = w / 1853
sy = h / 1260
def to_px(x, y):
    return int((x + 90) * sx), int(y * sy)

crop1 = im.crop((to_px(1300, 680)[0], to_px(1300, 680)[1], to_px(1780, 980)[0], to_px(1780, 980)[1]))
crop1.save(r"pruebas/test_crop_alsina_viedma3.png")

print("Position 3 complete!")
