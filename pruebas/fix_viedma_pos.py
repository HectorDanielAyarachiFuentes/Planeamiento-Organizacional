import xml.etree.ElementTree as ET
import pymupdf

base_svg = 'tareas/actividad_01/entregables/avance 2/img/RioNegro.svg'
tree = ET.parse(base_svg)
root = tree.getroot()

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')

# Fix Viedma text position so it does not touch the dot
for el in root.iter():
    if el.attrib.get('id') == 'text2207':
        el.attrib['x'] = "1545"
        el.attrib['y'] = "850"
        el.attrib['text-anchor'] = "end"
        
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                ts.attrib['text-anchor'] = "end"
                ts.attrib['x'] = "1545"
                if "Viedma" in (ts.text or ""):
                    ts.attrib['y'] = "850"
                    ts.attrib['style'] = "font-family:'Segoe UI',Arial,sans-serif;font-size:29px;font-weight:900;fill:#0f2d59;"
                elif "CURZAS" in (ts.text or ""):
                    ts.attrib['y'] = "878"
                    ts.attrib['style'] = "font-family:'Segoe UI',Arial,sans-serif;font-size:20px;font-weight:800;font-style:italic;fill:#c89632;"

# Save to destination SVG
tree.write(base_svg, encoding='utf-8', xml_declaration=True)

# Render to PNG
doc = pymupdf.open(base_svg)
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('pruebas/rionegro_with_bottom_guide_v2.png')
print('Successfully updated Viedma position and saved RioNegro.svg!')
