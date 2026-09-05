import typst, os, fitz

svg_path = r'tareas\actividad_01\entregables\avance 2\img\RioNegro.svg'
typ_path = r'tareas\actividad_01\entregables\avance 2\Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi.typ'

with open(svg_path, 'r', encoding='utf-8') as f:
    svg_data = f.read()

# Trim viewBox to eliminate outer transparent padding
# Path bounds: -63.3 to 1611.8, Y: 1.0 to 1116.4
# Text bounds: -80.0 to 1535.0, Y: 45.0 to 1098.4
# So X from -85 to 1635 (width 1720), Y from 0 to 1130 (height 1130)
new_svg_data = svg_data.replace('viewBox="-90 0 1853 1260"', 'viewBox="-85 0 1720 1130"')

test_svg_path = r'tareas\actividad_01\entregables\avance 2\img\RioNegro_opt.svg'
with open(test_svg_path, 'w', encoding='utf-8') as f:
    f.write(new_svg_data)

with open(typ_path, 'r', encoding='utf-8') as f:
    typ_content = f.read()

for opt in ['width: 100%']:
    test_snippet = f'''        #v(10pt)
        #image("img/RioNegro_opt.svg", {opt})
        #v(6pt)
        #text(size: 8pt, fill: text-muted, style: "italic")[
          *Figura 1:* Mapa de la Provincia de Río Negro con división departamental, cabeceras y Sede Central CURZAS (Viedma), articulando la red de Nodos Regionales y proyectos de extensión territorial.
        ]'''

    mod_typ = typ_content.replace('''        #v(8pt)
        #image("img/RioNegro.svg", width: 96%)
        #v(4pt)
        #text(size: 7.8pt, fill: text-muted, style: "italic")[
          *Figura 1:* Mapa de la Provincia de Río Negro con división departamental, cabeceras y Sede Central CURZAS (Viedma), articulando la red de Nodos Regionales y proyectos de extensión territorial.
        ]''', test_snippet)

    mod_typ = mod_typ.replace(
        'inset: (x: 10pt, top: 8pt, bottom: 8pt),',
        'inset: (x: 10pt, top: 10pt, bottom: 10pt),'
    )

    temp_typ = r'tareas\actividad_01\entregables\avance 2\temp_render.typ'
    temp_pdf = r'pruebas\test_opt.pdf'

    with open(temp_typ, 'w', encoding='utf-8') as f:
        f.write(mod_typ)

    typst.compile(temp_typ, output=temp_pdf, root=os.path.abspath('.'))
    doc = fitz.open(temp_pdf)
    p8 = doc[8]
    pix = p8.get_pixmap(dpi=150)
    pix.save(r'pruebas\pagina_8_w100.png')
    print('Rendered width 100% preview to pruebas\pagina_8_w100.png')
    for d in p8.get_drawings():
        r = d['rect']
        if r.width > 400 and r.y0 > 200:
            print(f'Card bottom: {r.y1:.1f}, footer line at 794.3')
            break




if os.path.exists(temp_typ): os.remove(temp_typ)
if os.path.exists(test_svg_path): os.remove(test_svg_path)
