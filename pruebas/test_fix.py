import re
import pymupdf
from PIL import Image

with open(r"tareas/actividad_01/entregables/avance 2/img/RioNegro.svg", "r", encoding="utf-8") as f:
    svg_content = f.read()

# 1. Fix Adolfo Alsina (text2211) and Viedma (text2207)
# Adolfo Alsina:
old_alsina = re.search(r'<text id="text2211"[^>]*>.*?</text>', svg_content, re.DOTALL).group(0)
new_alsina = '''<text id="text2211" y="745" x="1310" style="font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;font-size:32px;font-weight:700;letter-spacing:1px;fill:#0f2d59;fill-opacity:0.95;stroke:none;" xml:space="preserve"><tspan y="745" x="1310" id="tspan2213" sodipodi:role="line">Adolfo</tspan><tspan id="tspan2215" y="782" x="1310" sodipodi:role="line">Alsina</tspan></text>'''

# Viedma:
old_viedma = re.search(r'<text id="text2207"[^>]*>.*?</text>', svg_content, re.DOTALL).group(0)
new_viedma = '''<text id="text2207" y="865" x="1570" style="font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;letter-spacing:0.5px;fill:#0f2d59;stroke:none;" xml:space="preserve" text-anchor="middle"><tspan x="1570" y="865" style="font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:800;fill:#0f2d59;">★ Viedma</tspan><tspan x="1570" y="888" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:700;fill:#c89632;">(Sede CURZAS)</tspan></text>'''

# 2. Fix 9 de Julio (text2229)
old_9julio = re.search(r'<text id="text2229"[^>]*>.*?</text>', svg_content, re.DOTALL).group(0)
new_9julio = '''<text id="text2229" y="650" x="765" style="font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;font-size:32px;font-weight:700;letter-spacing:1px;fill:#0f2d59;fill-opacity:0.95;stroke:none;" xml:space="preserve" text-anchor="middle"><tspan y="650" x="765" id="tspan2231" sodipodi:role="line">9 de</tspan><tspan id="tspan2233" y="688" x="765" sodipodi:role="line">Julio</tspan></text>'''

# 3. Fix Valcheta (text2218)
old_valcheta = re.search(r'<text id="text2218"[^>]*>.*?</text>', svg_content, re.DOTALL).group(0)
new_valcheta = '''<text id="text2218" y="665" x="970" style="font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;font-size:32px;font-weight:700;letter-spacing:1px;fill:#0f2d59;fill-opacity:0.95;stroke:none;" xml:space="preserve" text-anchor="middle"><tspan y="665" x="970" id="tspan2220" sodipodi:role="line">Valcheta</tspan></text>'''

test_svg = svg_content.replace(old_alsina, new_alsina).replace(old_viedma, new_viedma).replace(old_9julio, new_9julio).replace(old_valcheta, new_valcheta)

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

crop1 = im.crop((to_px(1330, 680)[0], to_px(1330, 680)[1], to_px(1780, 980)[0], to_px(1780, 980)[1]))
crop1.save(r"pruebas/test_crop_alsina_viedma.png")

crop2 = im.crop((to_px(650, 550)[0], to_px(650, 550)[1], to_px(1050, 950)[0], to_px(1050, 950)[1]))
crop2.save(r"pruebas/test_crop_9dejulio.png")

print("Fixed test render complete!")
