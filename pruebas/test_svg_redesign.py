import xml.etree.ElementTree as ET
import re
import copy
import pymupdf

# Load original SVG
svg_path = 'tareas/actividad_01/entregables/avance 2/img/RioNegro.svg'
tree = ET.parse(svg_path)
root = tree.getroot()

# SVG namespace
ns = {'svg': 'http://www.w3.org/2000/svg'}
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')

# Harmonious, modern academic palette for departments
# Muted, elegant pastel tones with excellent neighboring contrast
dept_colors = {
    'path2278': '#F3C5BA',  # Gral Roca (Alto Valle) - Soft terracotta blush
    'path2290': '#F9E2AF',  # Avellaneda (Valle Medio) - Soft warm honey/sun
    'path2300': '#E8D5C4',  # Pichi Mahuida - Soft warm sand/parchment
    'path2191': '#CDE5CE',  # Conesa - Soft sage/celadon
    'path2205': '#BBD6E8',  # Adolfo Alsina (Costa / Viedma) - Soft maritime powder blue
    'path2204': '#B1DDD6',  # San Antonio (Golfo) - Soft seafoam / coastal teal
    'path2216': '#E2CDE6',  # Valcheta - Soft muted lilac / lavender
    'path2220': '#EAD7BD',  # 9 de Julio - Warm clay / soft almond
    'path2249': '#CCE2C5',  # 25 de Mayo - Soft pistachio / herbal
    'path2256': '#E6D7CC',  # El Cuy - Soft neutral sandstone
    'path2289': '#D5D0E8',  # Pilcaniyeu - Soft thistle / lavender mist
    'path2263': '#F5DEB3',  # Ñorquinco - Soft wheat / warm peach
    'path2275': '#B5CCE2',  # Bariloche (Andes) - Glacial alpine blue
}

# Typography styling
# Departments: Deep Navy #0f2d59, bold, white halo for maximum readability
dept_text_style = (
    "font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;"
    "font-size:44px;font-weight:800;letter-spacing:1px;"
    "fill:#0f2d59;fill-opacity:1;"
    "stroke:#ffffff;stroke-width:5px;stroke-linejoin:round;stroke-linecap:round;"
    "paint-order:stroke fill;"
)

# Cabeceras / Capitals: Deep Burgundy Crimson #991b1b, semibold, white halo
cap_text_style = (
    "font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;"
    "font-size:28px;font-weight:700;"
    "fill:#991b1b;fill-opacity:1;"
    "stroke:#ffffff;stroke-width:4px;stroke-linejoin:round;stroke-linecap:round;"
    "paint-order:stroke fill;"
)

# Viedma Special style (Capital Provincial & Sede CURZAS)
viedma_text_style = (
    "font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;"
    "font-size:32px;font-weight:800;"
    "fill:#0f2d59;fill-opacity:1;"
    "stroke:#ffffff;stroke-width:4px;stroke-linejoin:round;stroke-linecap:round;"
    "paint-order:stroke fill;"
)

# Apply department fills
for el in root.iter():
    if el.tag.endswith('path'):
        pid = el.attrib.get('id')
        if pid in dept_colors:
            # Elegant boundary stroke
            new_fill = dept_colors[pid]
            el.attrib['style'] = f"fill:{new_fill};fill-rule:evenodd;stroke:#475569;stroke-width:1.8px;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1;"
        elif pid and pid.startswith('path22') and len(el.attrib.get('d', '')) < 100:
            # These are the city dots
            if pid == 'path2230':
                # Viedma dot! Make it distinctive (Gold center with Navy border)
                el.attrib['style'] = "fill:#c89632;fill-rule:evenodd;stroke:#0f2d59;stroke-width:2.5px;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1;"
            else:
                # Other cabeceras: Crimson dot with crisp border
                el.attrib['style'] = "fill:#dc2626;fill-rule:evenodd;stroke:#7f1d1d;stroke-width:1.5px;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1;"

# Department text IDs vs Capital text IDs
dept_text_ids = {
    'text2280', 'text2296', 'text2306', 'text2201', 'text2211',
    'text2212', 'text2218', 'text2229', 'text2251', 'text2262',
    'text2285', 'text2291', 'text2269'
}

cap_text_ids = {
    'text2286', 'text2292', 'text2302', 'text2197', 'text2207',
    'text2206', 'text2236', 'text2222', 'text2259', 'text2265',
    'text2277', 'text2295', 'text2258'
}

for el in root.iter():
    if el.tag.endswith('text'):
        tid = el.attrib.get('id')
        if tid == 'text2207':  # Viedma
            el.attrib['style'] = viedma_text_style
            for ts in el.iter():
                if ts.tag.endswith('tspan'):
                    ts.attrib['style'] = viedma_text_style
        elif tid in dept_text_ids:
            el.attrib['style'] = dept_text_style
            for ts in el.iter():
                if ts.tag.endswith('tspan'):
                    ts.attrib['style'] = dept_text_style
        elif tid in cap_text_ids:
            el.attrib['style'] = cap_text_style
            for ts in el.iter():
                if ts.tag.endswith('tspan'):
                    ts.attrib['style'] = cap_text_style

# Fix specific text alignments:
# 1. Bariloche department text: original x=-106 was way off-screen!
for el in root.iter():
    if el.attrib.get('id') == 'text2285':  # Bariloche dept
        el.attrib['x'] = "-10"
        el.attrib['y'] = "1040"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['x'] = "-10"
                ts.attrib['y'] = "1040"
    elif el.attrib.get('id') == 'text2277':  # San Carlos de Bariloche cabecera
        el.attrib['x'] = "-45"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['x'] = "-45"
    elif el.attrib.get('id') == 'text2229':  # 9 de Julio vertical text
        # Adjust y-spacing so the 'o' does not stick out of the southern border
        # tspans: 9, d, e, J, u, l, i, o
        # original y started at 617 and ended at 1097 (step 60)
        # Let's compress step to 50: start at 630, step 48
        y_start = 625
        step = 46
        idx = 0
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['y'] = str(y_start + idx * step)
                idx += 1

# Add a stylish institutional legend in the Atlantic ocean area (bottom right / east of San Antonio)
# In the original map, coordinates are ~1300 to 1700 in X, and 950 to 1200 in Y (ocean area)
legend_group = ET.Element('{http://www.w3.org/2000/svg}g', {
    'id': 'map_legend',
    'transform': 'translate(1080, 990)'
})

# Legend background card
legend_bg = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': '0', 'y': '0', 'width': '630', 'height': '210', 'rx': '12', 'ry': '12',
    'style': 'fill:#ffffff;fill-opacity:0.92;stroke:#cbd5e1;stroke-width:2px;'
})
legend_group.append(legend_bg)

# Legend Title
legend_title = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '25', 'y': '42',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:24px;font-weight:800;fill:#0f2d59;letter-spacing:1.5px;"
})
legend_title.text = "REFERENCIAS CARTOGRÁFICAS"
legend_group.append(legend_title)

# Item 1: Department sample
item1_box = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': '25', 'y': '68', 'width': '34', 'height': '24', 'rx': '4',
    'style': 'fill:#BBD6E8;stroke:#475569;stroke-width:1.5px;'
})
item1_text = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '75', 'y': '88',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:700;fill:#0f2d59;"
})
item1_text.text = "Nombre de Departamento (División Política)"
legend_group.append(item1_box)
legend_group.append(item1_text)

# Item 2: Capital departamental
item2_dot = ET.Element('{http://www.w3.org/2000/svg}circle', {
    'cx': '42', 'cy': '125', 'r': '9',
    'style': 'fill:#dc2626;stroke:#7f1d1d;stroke-width:2px;'
})
item2_text = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '75', 'y': '133',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:700;fill:#991b1b;"
})
item2_text.text = "Cabecera / Capital Departamental"
legend_group.append(item2_dot)
legend_group.append(item2_text)

# Item 3: Viedma (Capital Provincial / Sede CURZAS)
item3_dot = ET.Element('{http://www.w3.org/2000/svg}circle', {
    'cx': '42', 'cy': '170', 'r': '10',
    'style': 'fill:#c89632;stroke:#0f2d59;stroke-width:3px;'
})
item3_text = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '75', 'y': '178',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:800;fill:#0f2d59;"
})
item3_text.text = "Viedma: Capital Provincial y Sede Central CURZAS"
legend_group.append(item3_dot)
legend_group.append(item3_text)

root.append(legend_group)

# Save test SVG
test_svg_path = 'pruebas/RioNegro_improved_test.svg'
tree.write(test_svg_path, encoding='utf-8', xml_declaration=True)

# Render to PNG
doc = pymupdf.open(test_svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('pruebas/rionegro_improved.png')
print('Successfully generated pruebas/rionegro_improved.png:', pix.width, 'x', pix.height)
