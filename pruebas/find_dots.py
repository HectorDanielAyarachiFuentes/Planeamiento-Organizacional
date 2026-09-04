import xml.etree.ElementTree as ET
import re

tree = ET.parse(r"tareas/actividad_01/entregables/avance 2/img/RioNegro.svg")
root = tree.getroot()

for elem in root.iter('{http://www.w3.org/2000/svg}path'):
    elem_id = elem.attrib.get('id', '')
    transform = elem.attrib.get('transform', '')
    if 'translate' in transform:
        m = re.search(r'translate\(([^,]+),([^)]+)\)', transform)
        if m:
            tx, ty = float(m.group(1)), float(m.group(2))
            cx = float(elem.attrib.get('{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}cx', '763.21429'))
            cy = float(elem.attrib.get('{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}cy', '266.35715'))
            print(f"Dot ID: {elem_id:10} root_pos=({tx+cx:.1f}, {ty+cy:.1f}) in_layer1_pos=({tx+cx-112.93:.1f}, {ty+cy-24.92:.1f})")
