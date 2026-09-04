import xml.etree.ElementTree as ET
import re

tree = ET.parse('tareas/actividad_01/entregables/avance 2/img/RioNegro.svg')
root = tree.getroot()

# Let's inspect all paths and their bounding boxes approx from 'd'
for el in root.iter():
    if el.tag.endswith('path'):
        pid = el.attrib.get('id')
        d = el.attrib.get('d', '')
        # extract all coordinates
        coords = re.findall(r'[-+]?[0-9]*\.?[0-9]+', d)
        if len(coords) >= 4:
            pts = [float(c) for c in coords]
            xs = pts[0::2]
            ys = pts[1::2]
            if xs and ys:
                min_x, max_x = min(xs), max(xs)
                min_y, max_y = min(ys), max(ys)
                cx = (min_x + max_x) / 2
                cy = (min_y + max_y) / 2
                print(f"PATH {pid:<10}: bbox=({min_x:.1f}, {min_y:.1f}) to ({max_x:.1f}, {max_y:.1f}), center=({cx:.1f}, {cy:.1f}), fill={el.attrib.get('style','')[:25]}")

print("\n--- ALL TEXTS ---")
for el in root.iter():
    if el.tag.endswith('text'):
        tid = el.attrib.get('id')
        full_text = ' '.join(''.join(el.itertext()).split())
        x = el.attrib.get('x', '')
        y = el.attrib.get('y', '')
        # check tspans
        tspans = [ts for ts in el.iter() if ts.tag.endswith('tspan')]
        if tspans:
            x = tspans[0].attrib.get('x', x)
            y = tspans[0].attrib.get('y', y)
        print(f"TEXT {tid:<10}: pos=({x}, {y}) | text='{full_text}' | style={el.attrib.get('style','')[:40]}")
