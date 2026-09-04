import xml.etree.ElementTree as ET

tree = ET.parse('tareas/actividad_01/entregables/avance 2/img/RioNegro.svg')
root = tree.getroot()

print("--- TEXT ELEMENTS ---")
for el in root.iter():
    if el.tag.endswith('text'):
        full_text = ' '.join(''.join(el.itertext()).split())
        tspans = [t.attrib for t in el.iter() if t.tag.endswith('tspan')]
        print(f"ID: {el.attrib.get('id'):<10} | Tag: {el.tag} | Text: '{full_text}' | Style: {el.attrib.get('style')} | x={el.attrib.get('x')} y={el.attrib.get('y')} | tspans={len(tspans)}")
        for ts in el.iter():
            if ts.tag.endswith('tspan'):
                print(f"   tspan: '{ts.text}' | style={ts.attrib.get('style')} | x={ts.attrib.get('x')} y={ts.attrib.get('y')}")

print("\n--- PATH ELEMENTS ---")
for el in root.iter():
    if el.tag.endswith('path'):
        pid = el.attrib.get('id')
        style = el.attrib.get('style', '')
        d = el.attrib.get('d', '')
        print(f"ID: {pid:<10} | style: {style} | d_len={len(d)}")
