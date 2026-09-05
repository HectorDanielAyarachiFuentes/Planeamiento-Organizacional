import typst, os, pymupdf

svg_path = r'tareas\actividad_01\entregables\avance 2\img\RioNegro.svg'
typ_path = r'tareas\actividad_01\entregables\avance 2\Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi.typ'

with open(svg_path, 'r', encoding='utf-8') as f:
    svg_data = f.read()

test_svg_data = svg_data.replace('viewBox="-90 0 1853 1260"', 'viewBox="-85 0 1735 1140"')
test_svg_path = r'tareas\actividad_01\entregables\avance 2\img\RioNegro_test.svg'
with open(test_svg_path, 'w', encoding='utf-8') as f:
    f.write(test_svg_data)

with open(typ_path, 'r', encoding='utf-8') as f:
    typ_content = f.read()

for opt in ['height: 315pt']:
    modified_typ = typ_content.replace('image("img/RioNegro.svg", width: 96%)', f'image("img/RioNegro_test.svg", {opt})')
    temp_typ = r'tareas\actividad_01\entregables\avance 2\temp_render.typ'
    temp_pdf = r'pruebas\test_viewbox.pdf'

    with open(temp_typ, 'w', encoding='utf-8') as f:
        f.write(modified_typ)

    typst.compile(temp_typ, output=temp_pdf, root=os.path.abspath('.'))
    doc = pymupdf.open(temp_pdf)
    print(f'{opt} -> pages: {len(doc)}')
    p8 = doc[8]
    pix = p8.get_pixmap(dpi=150)
    pix.save(r'pruebas\pagina_8_315pt.png')
    print('Saved to pruebas\pagina_8_315pt.png')


if os.path.exists(temp_typ): os.remove(temp_typ)
if os.path.exists(test_svg_path): os.remove(test_svg_path)

