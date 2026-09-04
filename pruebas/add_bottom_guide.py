import xml.etree.ElementTree as ET
import pymupdf

base_svg = 'tareas/actividad_01/entregables/avance 2/img/RioNegro.svg'
tree = ET.parse(base_svg)
root = tree.getroot()

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')

# Expand height from 1246 to 1340 to accommodate the bottom reading guide banner
root.attrib['width'] = "1853"
root.attrib['height'] = "1340"
root.attrib['viewBox'] = "-90 0 1853 1340"

# Remove any previous bottom guide or old elements
for el in list(root):
    if el.attrib.get('id') in ['bottom_reading_guide']:
        root.remove(el)

# 1. Update Viedma label on the map to include "(Sede CURZAS)"
for el in root.iter():
    if el.attrib.get('id') == 'text2207':
        # Clear existing tspans and add two clean tspans
        for child in list(el):
            el.remove(child)
        el.attrib['x'] = "1480"
        el.attrib['y'] = "855"
        
        # Line 1: ★ Viedma
        ts1 = ET.Element('{http://www.w3.org/2000/svg}tspan', {
            'x': '1480', 'y': '855',
            'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:30px;font-weight:900;fill:#0f2d59;"
        })
        ts1.text = "★ Viedma"
        el.append(ts1)
        
        # Line 2: (Sede CURZAS)
        ts2 = ET.Element('{http://www.w3.org/2000/svg}tspan', {
            'x': '1480', 'y': '885',
            'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:21px;font-weight:700;font-style:italic;fill:#c89632;"
        })
        ts2.text = "(Sede CURZAS)"
        el.append(ts2)

# 2. Add Bottom Reading Guide Banner ("CÓMO LEER EL MAPA")
guide_group = ET.Element('{http://www.w3.org/2000/svg}g', {
    'id': 'bottom_reading_guide',
    'transform': 'translate(80, 1170)'
})

# Background container card
guide_bg = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': '0', 'y': '0', 'width': '1550', 'height': '115', 'rx': '16', 'ry': '16',
    'style': 'fill:#ffffff;fill-opacity:0.97;stroke:#94a3b8;stroke-width:2px;'
})
guide_group.append(guide_bg)

# Banner Title / Badge on the left
badge_bg = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': '18', 'y': '22', 'width': '230', 'height': '71', 'rx': '10', 'ry': '10',
    'style': 'fill:#0f2d59;'
})
guide_group.append(badge_bg)

badge_t1 = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '133', 'y': '50', 'text-anchor': 'middle',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:800;fill:#ffffff;letter-spacing:1px;"
})
badge_t1.text = "GUÍA DE LECTURA"
guide_group.append(badge_t1)

badge_t2 = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '133', 'y': '74', 'text-anchor': 'middle',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:600;fill:#f8fafc;letter-spacing:0.5px;"
})
badge_t2.text = "CÓMO LEER EL MAPA"
guide_group.append(badge_t2)

# Column 1: DEPARTAMENTO
col1_x = 280
col1_icon = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': str(col1_x), 'y': '43', 'width': '34', 'height': '28', 'rx': '5',
    'style': 'fill:#BCD7EB;stroke:#334155;stroke-width:2px;'
})
guide_group.append(col1_icon)

col1_title = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': str(col1_x + 48), 'y': '53',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:800;fill:#0f2d59;"
})
col1_title.text = "Texto Azul Marino"
guide_group.append(col1_title)

col1_desc = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': str(col1_x + 48), 'y': '78',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:600;fill:#475569;"
})
col1_desc.text = "= Departamento (División Política)"
guide_group.append(col1_desc)

# Vertical divider 1
div1 = ET.Element('{http://www.w3.org/2000/svg}line', {
    'x1': '665', 'y1': '24', 'x2': '665', 'y2': '91',
    'style': 'stroke:#e2e8f0;stroke-width:2px;'
})
guide_group.append(div1)

# Column 2: CABECERA
col2_x = 700
col2_dot = ET.Element('{http://www.w3.org/2000/svg}circle', {
    'cx': str(col2_x + 15), 'cy': '57', 'r': '11',
    'style': 'fill:#dc2626;stroke:#7f1d1d;stroke-width:2.5px;'
})
guide_group.append(col2_dot)

col2_title = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': str(col2_x + 42), 'y': '53',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:800;fill:#991b1b;"
})
col2_title.text = "Punto y Texto Rojo Bordó"
guide_group.append(col2_title)

col2_desc = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': str(col2_x + 42), 'y': '78',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:600;fill:#475569;"
})
col2_desc.text = "= Cabecera / Capital Departamental"
guide_group.append(col2_desc)

# Vertical divider 2
div2 = ET.Element('{http://www.w3.org/2000/svg}line', {
    'x1': '1110', 'y1': '24', 'x2': '1110', 'y2': '91',
    'style': 'stroke:#e2e8f0;stroke-width:2px;'
})
guide_group.append(div2)

# Column 3: VIEDMA / SEDE CURZAS
col3_x = 1145
col3_dot = ET.Element('{http://www.w3.org/2000/svg}circle', {
    'cx': str(col3_x + 15), 'cy': '57', 'r': '13',
    'style': 'fill:#c89632;stroke:#0f2d59;stroke-width:3.5px;'
})
guide_group.append(col3_dot)

col3_title = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': str(col3_x + 44), 'y': '53',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:900;fill:#0f2d59;"
})
col3_title.text = "★ Viedma"
guide_group.append(col3_title)

col3_desc = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': str(col3_x + 44), 'y': '78',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:700;fill:#c89632;"
})
col3_desc.text = "= Capital Provincial y Sede Central CURZAS"
guide_group.append(col3_desc)

root.append(guide_group)

# Save to destination SVG
tree.write(base_svg, encoding='utf-8', xml_declaration=True)
print('Successfully saved updated RioNegro.svg!')

# Render to PNG
doc = pymupdf.open(base_svg)
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('pruebas/rionegro_with_bottom_guide.png')
print('Generated pruebas/rionegro_with_bottom_guide.png successfully:', pix.width, 'x', pix.height)
