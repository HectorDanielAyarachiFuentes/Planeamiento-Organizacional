import re
import xml.etree.ElementTree as ET

tree = ET.parse(r"tareas/actividad_01/entregables/avance 2/img/RioNegro.svg")
root = tree.getroot()

# Find texts
for elem in root.iter('{http://www.w3.org/2000/svg}text'):
    elem_id = elem.attrib.get('id', '')
    text_content = " ".join("".join(t.itertext()).strip() for t in elem)
    x = elem.attrib.get('x', '')
    y = elem.attrib.get('y', '')
    print(f"ID: {elem_id:15} x={x:8} y={y:8} text={text_content[:40]}")
