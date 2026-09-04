import xml.etree.ElementTree as ET
import pymupdf

svg_target = 'tareas/actividad_01/entregables/avance 2/img/RioNegro.svg'
tree = ET.parse(svg_target)
root = tree.getroot()

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')

# Remove all bulky boxes / cards (top-left, top-right, bottom)
for el in list(root):
    if el.attrib.get('id') in ['map_legend', 'map_title', 'bottom_reading_guide']:
        root.remove(el)

# Set clean, balanced viewBox and dimensions
root.attrib['width'] = "1853"
root.attrib['height'] = "1260"
root.attrib['viewBox'] = "-90 0 1853 1260"

# Harmonious, modern, soothing editorial palette (soft, elegant, matte tones)
dept_colors = {
    'path2278': '#F5CAC2',  # Gral Roca (Alto Valle)
    'path2290': '#FDE8BE',  # Avellaneda (Valle Medio)
    'path2300': '#EAD7C5',  # Pichi Mahuida
    'path2191': '#D3EADB',  # Conesa
    'path2205': '#C5DCF0',  # Adolfo Alsina
    'path2204': '#BDE5DE',  # San Antonio
    'path2216': '#E6D4EB',  # Valcheta
    'path2220': '#EFE0CC',  # 9 de Julio
    'path2249': '#D7EBD0',  # 25 de Mayo
    'path2256': '#EAE0D5',  # El Cuy
    'path2289': '#DED8F0',  # Pilcaniyeu
    'path2263': '#F7E5C3',  # Ñorquinco
    'path2275': '#C2D7EB',  # Bariloche
}

# Typography: refined, clean, uncluttered
dept_style = (
    "font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;"
    "font-size:38px;font-weight:700;letter-spacing:1px;"
    "fill:#0f2d59;fill-opacity:0.95;stroke:none;"
)

cap_style = (
    "font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;"
    "font-size:24px;font-weight:600;letter-spacing:0.3px;"
    "fill:#881337;fill-opacity:0.95;stroke:none;"
)

# Apply paths
for el in root.iter():
    if el.tag.endswith('path'):
        pid = el.attrib.get('id')
        if pid in dept_colors:
            el.attrib['style'] = f"fill:{dept_colors[pid]};fill-rule:evenodd;stroke:#475569;stroke-width:1.4px;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:0.85;"
        elif pid and pid.startswith('path22') and len(el.attrib.get('d', '')) < 100:
            if pid == 'path2230':  # Viedma
                el.attrib['style'] = "fill:#c89632;fill-rule:evenodd;stroke:#0f2d59;stroke-width:2.5px;"
            else:  # Cabeceras
                el.attrib['style'] = "fill:#dc2626;fill-rule:evenodd;stroke:#7f1d1d;stroke-width:1.2px;"

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

# Apply styles to text elements
for el in root.iter():
    if el.tag.endswith('text'):
        tid = el.attrib.get('id')
        if tid in dept_text_ids:
            el.attrib['style'] = dept_style
            for ts in el.iter():
                if ts.tag.endswith('tspan'):
                    ts.attrib['style'] = dept_style
        elif tid in cap_text_ids and tid != 'text2207':
            el.attrib['style'] = cap_style
            for ts in el.iter():
                if ts.tag.endswith('tspan'):
                    ts.attrib['style'] = cap_style

# Fine-tune department labels & cabeceras so they breathe
for el in root.iter():
    tid = el.attrib.get('id')
    if tid == 'text2285':  # Bariloche
        s = dept_style.replace('38px', '30px')
        el.attrib['style'] = s
        el.attrib['x'] = "-80"
        el.attrib['y'] = "1040"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['style'] = s
                ts.attrib['x'] = "-80"
                ts.attrib['y'] = "1040"
    elif tid == 'text2277':  # San Carlos de Bariloche
        s = cap_style.replace('24px', '20px')
        el.attrib['style'] = s
        el.attrib['x'] = "-45"
        ys = [920, 946, 972]
        idx = 0
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['style'] = s
                ts.attrib['x'] = "-45"
                ts.attrib['y'] = str(ys[idx])
                idx += 1
    elif tid == 'text2269':  # Ñorquinco
        el.attrib['x'] = "145"
        el.attrib['y'] = "1035"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['x'] = "145"
                ts.attrib['y'] = "1035"
    elif tid == 'text2291':  # Pilcaniyeu
        el.attrib['x'] = "85"
        el.attrib['y'] = "795"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['x'] = "85"
                ts.attrib['y'] = "795"
    elif tid == 'text2212':  # San Antonio
        el.attrib['x'] = "1100"
        el.attrib['y'] = "940"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['x'] = "1100"
                ts.attrib['y'] = "940"
    elif tid == 'text2218':  # Valcheta vertical
        # Slightly softer vertical spacing
        y_start = 650
        step = 55
        idx = 0
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['y'] = str(y_start + idx * step)
                idx += 1
    elif tid == 'text2229':  # 9 de Julio vertical
        y_start = 640
        step = 45
        idx = 0
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['y'] = str(y_start + idx * step)
                idx += 1
    elif tid == 'text2207':  # Viedma
        for child in list(el):
            el.remove(child)
        el.attrib['x'] = "1540"
        el.attrib['y'] = "852"
        el.attrib['text-anchor'] = "end"
        
        ts1 = ET.Element('{http://www.w3.org/2000/svg}tspan', {
            'x': '1540', 'y': '852',
            'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:26px;font-weight:800;fill:#0f2d59;"
        })
        ts1.text = "★ Viedma"
        el.append(ts1)
        
        ts2 = ET.Element('{http://www.w3.org/2000/svg}tspan', {
            'x': '1540', 'y': '876',
            'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:700;fill:#c89632;"
        })
        ts2.text = "(Sede CURZAS)"
        el.append(ts2)

# Now, add a SINGLE, MINIMALIST, HIGH-END TITLE & LEGEND at the top-left (no bulky white boxes!)
# Transparent, clean, typography-driven (National Geographic / Apple Maps style)
header_group = ET.Element('{http://www.w3.org/2000/svg}g', {
    'id': 'clean_header',
    'transform': 'translate(30, 80)'
})

# Province Title (Direct, elegant typography without heavy card)
h_title = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '0', 'y': '45',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:44px;font-weight:900;fill:#0f2d59;letter-spacing:2px;"
})
h_title.text = "RÍO NEGRO"
header_group.append(h_title)

# Subtle golden accent line under title
h_line = ET.Element('{http://www.w3.org/2000/svg}line', {
    'x1': '0', 'y1': '62', 'x2': '260', 'y2': '62',
    'style': 'stroke:#c89632;stroke-width:3px;stroke-linecap:round;'
})
header_group.append(h_line)

# Subtitle
h_sub = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '0', 'y': '95',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:20px;font-weight:600;fill:#64748b;letter-spacing:0.5px;"
})
h_sub.text = "División Departamental y Cabeceras"
header_group.append(h_sub)

# Clean, minimalist inline guide right below subtitle (no cards, just sleek indicators!)
# Item 1: Departamento
g_rect = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': '0', 'y': '125', 'width': '22', 'height': '16', 'rx': '3',
    'style': 'fill:#C5DCF0;stroke:#475569;stroke-width:1.2px;'
})
g_text1 = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '32', 'y': '139',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:700;fill:#0f2d59;"
})
g_text1.text = "Departamento (Azul)"
header_group.append(g_rect)
header_group.append(g_text1)

# Item 2: Cabecera
g_dot = ET.Element('{http://www.w3.org/2000/svg}circle', {
    'cx': '11', 'cy': '170', 'r': '7',
    'style': 'fill:#dc2626;stroke:#7f1d1d;stroke-width:1.5px;'
})
g_text2 = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '32', 'y': '176',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:700;fill:#881337;"
})
g_text2.text = "Cabecera Departamental (Bordó)"
header_group.append(g_dot)
header_group.append(g_text2)

# Item 3: Viedma / Sede CURZAS
g_viedma = ET.Element('{http://www.w3.org/2000/svg}circle', {
    'cx': '11', 'cy': '207', 'r': '8',
    'style': 'fill:#c89632;stroke:#0f2d59;stroke-width:2px;'
})
g_text3 = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '32', 'y': '213',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:800;fill:#0f2d59;"
})
g_text3.text = "★ Viedma: Capital Provincial y Sede CURZAS"
header_group.append(g_viedma)
header_group.append(g_text3)

root.append(header_group)

# Write directly to SVG!
tree.write(svg_target, encoding='utf-8', xml_declaration=True)
print(f"Successfully written minimalist redesign directly to {svg_target}!")

# Render preview for internal inspection
doc = pymupdf.open(svg_target)
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('pruebas/rionegro_clean_preview.png')
print('Preview saved to pruebas/rionegro_clean_preview.png')
