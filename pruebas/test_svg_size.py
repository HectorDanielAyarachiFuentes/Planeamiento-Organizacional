import typst, os, fitz

typ_path = r'tareas\actividad_01\entregables\avance 2\Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi.typ'

with open(typ_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '#image("img/RioNegro.svg", width: 96%)'
print("Target present:", target in content)

# Check page 8 layout with various widths / insets
for test_w in ['width: 98%', 'width: 100%', 'height: 250pt', 'height: 270pt', 'height: 290pt', 'height: 300pt', 'height: 315pt', 'height: 330pt', 'height: 340pt', 'height: 350pt']:
    test_typ = r'tareas\actividad_01\entregables\avance 2\temp_test.typ'
    test_pdf = r'pruebas\test_size.pdf'
    new_c = content.replace(target, f'#image("img/RioNegro.svg", {test_w})')
    with open(test_typ, 'w', encoding='utf-8') as tf:
        tf.write(new_c)
    try:
        typst.compile(test_typ, output=test_pdf, root=os.path.abspath('.'))
        doc = fitz.open(test_pdf)
        print(f'{test_w} -> Total pages: {len(doc)}')
    except Exception as e:
        print(f'{test_w} -> Error: {e}')
    finally:
        if os.path.exists(test_typ):
            os.remove(test_typ)

