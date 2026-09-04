import xml.etree.ElementTree as ET
import pymupdf

tree = ET.parse('tareas/actividad_01/entregables/avance 2/img/RioNegro.svg')
root = tree.getroot()

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')

root.attrib['width'] = "1853"
root.attrib['height'] = "1246"
root.attrib['viewBox'] = "-90 0 1853 1246"

dept_colors = {
    'path2278': '#F5CAC2',  # Gral Roca (Alto Valle)
    'path2290': '#FCE7B8',  # Avellaneda (Valle Medio)
    'path2300': '#EAD7C5',  # Pichi Mahuida
    'path2191': '#CEE7D0',  # Conesa
    'path2205': '#BCD7EB',  # Adolfo Alsina (Costa / Viedma)
    'path2204': '#B7E2DB',  # San Antonio (Golfo)
    'path2216': '#E4D1E8',  # Valcheta
    'path2220': '#ECD8C1',  # 9 de Julio
    'path2249': '#D2E8CA',  # 25 de Mayo
    'path2256': '#E8DCCF',  # El Cuy
    'path2289': '#DAD4EC',  # Pilcaniyeu
    'path2263': '#F5E1BA',  # Ñorquinco
    'path2275': '#B9D1E6',  # Bariloche (Andes)
}

dept_text_style = (
    "font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;"
    "font-size:42px;font-weight:bold;letter-spacing:0.5px;"
    "fill:#0f2d59;fill-opacity:1;stroke:none;"
)

cap_text_style = (
    "font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;"
    "font-size:27px;font-weight:bold;letter-spacing:0.2px;"
    "fill:#991b1b;fill-opacity:1;stroke:none;"
)

viedma_text_style = (
    "font-family:'Segoe UI', 'Helvetica Neue', Arial, sans-serif;"
    "font-size:30px;font-weight:900;letter-spacing:0.5px;"
    "fill:#0f2d59;fill-opacity:1;stroke:none;"
)

# Apply department fills and borders
for el in root.iter():
    if el.tag.endswith('path'):
        pid = el.attrib.get('id')
        if pid in dept_colors:
            new_fill = dept_colors[pid]
            el.attrib['style'] = f"fill:{new_fill};fill-rule:evenodd;stroke:#334155;stroke-width:1.8px;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1;"
        elif pid and pid.startswith('path22') and len(el.attrib.get('d', '')) < 100:
            if pid == 'path2230':  # Viedma
                el.attrib['style'] = "fill:#c89632;fill-rule:evenodd;stroke:#0f2d59;stroke-width:3px;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1;"
            else:  # Cabeceras
                el.attrib['style'] = "fill:#dc2626;fill-rule:evenodd;stroke:#7f1d1d;stroke-width:1.5px;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1;"

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
                    ts.text = "★ Viedma"
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

# Fine-tune positionings
for el in root.iter():
    tid = el.attrib.get('id')
    if tid == 'text2212':  # San Antonio (Department name)
        # Restore nice position in the center of San Antonio department
        el.attrib['x'] = "1105"
        el.attrib['y'] = "950"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['x'] = "1105"
                ts.attrib['y'] = "950"
    elif tid == 'text2285':  # Bariloche dept
        style_bari = dept_text_style.replace('42px', '32px')
        el.attrib['style'] = style_bari
        el.attrib['x'] = "-80"
        el.attrib['y'] = "1045"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['style'] = style_bari
                ts.attrib['x'] = "-80"
                ts.attrib['y'] = "1045"
    elif tid == 'text2277':  # San Carlos de Bariloche cabecera
        style_scb = cap_text_style.replace('27px', '22px')
        el.attrib['style'] = style_scb
        el.attrib['x'] = "-45"
        idx = 0
        y_scb = [920, 948, 976]
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['style'] = style_scb
                ts.attrib['x'] = "-45"
                ts.attrib['y'] = str(y_scb[idx])
                idx += 1
    elif tid == 'text2269':  # Ñorquinco dept
        el.attrib['x'] = "145"
        el.attrib['y'] = "1045"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['x'] = "145"
                ts.attrib['y'] = "1045"
    elif tid == 'text2291':  # Pilcaniyeu dept
        el.attrib['x'] = "85"
        el.attrib['y'] = "805"
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['x'] = "85"
                ts.attrib['y'] = "805"
    elif tid == 'text2229':  # 9 de Julio vertical text
        y_start = 625
        step = 46
        idx = 0
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['y'] = str(y_start + idx * step)
                idx += 1

# Place legend in the LEFT SIDE (costado izquierdo superior: completely empty space!)
legend_group = ET.Element('{http://www.w3.org/2000/svg}g', {
    'id': 'map_legend',
    'transform': 'translate(-60, 60)'
})

legend_bg = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': '0', 'y': '0', 'width': '630', 'height': '225', 'rx': '14', 'ry': '14',
    'style': 'fill:#ffffff;fill-opacity:0.96;stroke:#94a3b8;stroke-width:2px;'
})
legend_group.append(legend_bg)

legend_title = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '28', 'y': '42',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:24px;font-weight:800;fill:#0f2d59;letter-spacing:1px;"
})
legend_title.text = "REFERENCIAS CARTOGRÁFICAS"
legend_group.append(legend_title)

div_line = ET.Element('{http://www.w3.org/2000/svg}line', {
    'x1': '28', 'y1': '54', 'x2': '602', 'y2': '54',
    'style': 'stroke:#e2e8f0;stroke-width:2px;'
})
legend_group.append(div_line)

# Item 1: Department
item1_box = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': '28', 'y': '74', 'width': '34', 'height': '24', 'rx': '4',
    'style': 'fill:#BCD7EB;stroke:#334155;stroke-width:1.5px;'
})
item1_text = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '78', 'y': '93',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:700;fill:#0f2d59;"
})
item1_text.text = "Nombre de Departamento (División Política)"
legend_group.append(item1_box)
legend_group.append(item1_text)

# Item 2: Cabecera departamental
item2_dot = ET.Element('{http://www.w3.org/2000/svg}circle', {
    'cx': '45', 'cy': '133', 'r': '9',
    'style': 'fill:#dc2626;stroke:#7f1d1d;stroke-width:2px;'
})
item2_text = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '78', 'y': '141',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:700;fill:#991b1b;"
})
item2_text.text = "Cabecera / Capital Departamental"
legend_group.append(item2_dot)
legend_group.append(item2_text)

# Item 3: Viedma (Capital Provincial / Sede CURZAS)
item3_dot = ET.Element('{http://www.w3.org/2000/svg}circle', {
    'cx': '45', 'cy': '180', 'r': '10',
    'style': 'fill:#c89632;stroke:#0f2d59;stroke-width:3px;'
})
item3_text = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '78', 'y': '188',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:800;fill:#0f2d59;"
})
item3_text.text = "★ Viedma: Capital Provincial y Sede CURZAS"
legend_group.append(item3_dot)
legend_group.append(item3_text)

root.append(legend_group)

test_svg_path = 'pruebas/RioNegro_legend_left.svg'
tree.write(test_svg_path, encoding='utf-8', xml_declaration=True)

doc = pymupdf.open(test_svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('pruebas/rionegro_legend_left.png')
print('Generated rionegro_legend_left.png successfully')
