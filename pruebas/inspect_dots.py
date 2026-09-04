import xml.etree.ElementTree as ET

tree = ET.parse('tareas/actividad_01/entregables/avance 2/img/RioNegro.svg')
root = tree.getroot()

for el in root.iter():
    if el.attrib.get('id', '').startswith('path22') and len(el.attrib.get('d', '')) < 100:
        print(f"DOT {el.attrib.get('id')}: transform={el.attrib.get('transform')} | style={el.attrib.get('style')}")
