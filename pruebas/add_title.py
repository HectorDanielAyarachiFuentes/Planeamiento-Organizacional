import xml.etree.ElementTree as ET
import pymupdf

tree = ET.parse('tareas/actividad_01/entregables/avance 2/img/RioNegro.svg')
root = tree.getroot()

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')

# Title Group placed in top-right empty space (x: 950 to 1650, y: 70 to 220)
title_group = ET.Element('{http://www.w3.org/2000/svg}g', {
    'id': 'map_title',
    'transform': 'translate(980, 80)'
})

# Optional elegant title card or clean typography
title_card = ET.Element('{http://www.w3.org/2000/svg}rect', {
    'x': '0', 'y': '0', 'width': '680', 'height': '140', 'rx': '14', 'ry': '14',
    'style': 'fill:#ffffff;fill-opacity:0.96;stroke:#94a3b8;stroke-width:2px;'
})
title_group.append(title_card)

# Main Title: PROVINCIA DE RÍO NEGRO
main_title = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '340', 'y': '58',
    'text-anchor': 'middle',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:38px;font-weight:900;fill:#0f2d59;letter-spacing:2px;"
})
main_title.text = "PROVINCIA DE RÍO NEGRO"
title_group.append(main_title)

# Gold decorative accent line
accent_line = ET.Element('{http://www.w3.org/2000/svg}line', {
    'x1': '80', 'y1': '76', 'x2': '600', 'y2': '76',
    'style': 'stroke:#c89632;stroke-width:3.5px;stroke-linecap:round;'
})
title_group.append(accent_line)

# Subtitle: División Política Departamental y Cabeceras
subtitle = ET.Element('{http://www.w3.org/2000/svg}text', {
    'x': '340', 'y': '112',
    'text-anchor': 'middle',
    'style': "font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:600;fill:#475569;letter-spacing:0.5px;"
})
subtitle.text = "División Política Departamental y Cabeceras"
title_group.append(subtitle)

root.append(title_group)

test_svg_path = 'pruebas/RioNegro_with_title.svg'
tree.write(test_svg_path, encoding='utf-8', xml_declaration=True)

doc = pymupdf.open(test_svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('pruebas/rionegro_with_title.png')
print('Generated rionegro_with_title.png successfully')
