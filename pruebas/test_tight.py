import typst, os, fitz

svg_path = r'tareas\actividad_01\entregables\avance 2\img\RioNegro.svg'
typ_path = r'tareas\actividad_01\entregables\avance 2\Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi.typ'

with open(svg_path, 'r', encoding='utf-8') as f:
    svg_data = f.read()

# Replace viewBox with tight bounding box: viewBox="15 40 1740 1100"
test_svg_data = svg_data.replace('viewBox="-90 0 1853 1260"', 'viewBox="15 40 1740 1100"')

test_svg_path = r'tareas\actividad_01\entregables\avance 2\img\RioNegro_tight.svg'
with open(test_svg_path, 'w', encoding='utf-8') as f:
    f.write(test_svg_data)

with open(typ_path, 'r', encoding='utf-8') as f:
    typ_content = f.read()

# Target block to replace
old_target = '''        #text(weight: "bold", fill: primary, size: 8.8pt)[Estructura Territorial y Oferta Académica del CURZAS en Río Negro]
        #v(4pt)
        #table(
          columns: (115pt, 1fr),
          stroke: 0.3pt + border-subtle,
          fill: (x, y) => if y == 0 { primary } else if calc.even(y) { rgb("#f8fafc") } else { white },
          align: (left + horizon, left + horizon),
          inset: (x: 7pt, y: 3.5pt),
          table.header(
            text(weight: "bold", fill: white, size: 8pt)[Eje Territorial y Académico],
            text(weight: "bold", fill: white, size: 8pt)[Detalle Institucional]
          ),
          [#text(weight: "bold", fill: primary, size: 8pt)[10 Nodos Regionales]],
          [#text(size: 8pt)[
            • *Línea Sur:* Ingeniero Jacobacci, Maquinchao, Los Menucos, Sierra Colorada, Ramos Mexía y Valcheta. \\
            • *Zona Atlántica y Valles:* San Antonio Oeste, Sierra Grande, General Conesa y Río Colorado.
          ]],
          [#text(weight: "bold", fill: primary, size: 8pt)[Carreras Dictadas]],
          [#text(size: 8pt)[
            • *Licenciatura en Recursos Humanos* (Ciclo de Complementación Curricular) \\
            • *Licenciatura en Arte y Sociedad* \\
            • _Entre otras propuestas formativas de grado, ciclos y tecnicaturas del CURZAS._
          ]]
        )
        #v(8pt)
        #image("img/RioNegro.svg", width: 96%)
        #v(4pt)
        #text(size: 7.8pt, fill: text-muted, style: "italic")[
          *Figura 1:* Mapa de la Provincia de Río Negro con división departamental, cabeceras y Sede Central CURZAS (Viedma), articulando la red de Nodos Regionales y proyectos de extensión territorial.
        ]'''

new_target = '''        #text(weight: "bold", fill: primary, size: 9pt)[Estructura Territorial y Oferta Académica del CURZAS en Río Negro]
        #v(6pt)
        #table(
          columns: (134pt, 1fr),
          stroke: 0.3pt + border-subtle,
          fill: (x, y) => if y == 0 { primary } else if calc.even(y) { rgb("#f8fafc") } else { white },
          align: (left + horizon, left + horizon),
          inset: (x: 8pt, y: 5pt),
          table.header(
            text(weight: "bold", fill: white, size: 8.2pt)[Eje Territorial y Académico],
            text(weight: "bold", fill: white, size: 8.2pt)[Detalle Institucional]
          ),
          [#text(weight: "bold", fill: primary, size: 8.2pt)[10 Nodos Regionales]],
          [#text(size: 8.2pt)[
            • *Línea Sur:* Ingeniero Jacobacci, Maquinchao, Los Menucos, Sierra Colorada, Ramos Mexía y Valcheta. \\
            • *Zona Atlántica y Valles:* San Antonio Oeste, Sierra Grande, General Conesa y Río Colorado.
          ]],
          [#text(weight: "bold", fill: primary, size: 8.2pt)[Carreras Dictadas]],
          [#text(size: 8.2pt)[
            • *Licenciatura en Recursos Humanos* (Ciclo de Complementación Curricular) \\
            • *Licenciatura en Arte y Sociedad* \\
            • _Entre otras propuestas formativas de grado, ciclos y tecnicaturas del CURZAS._
          ]]
        )
        #v(12pt)
        #image("img/RioNegro_tight.svg", width: 100%)
        #v(8pt)
        #text(size: 8pt, fill: text-muted, style: "italic")[
          *Figura 1:* Mapa de la Provincia de Río Negro con división departamental, cabeceras y Sede Central CURZAS (Viedma), articulando la red de Nodos Regionales y proyectos de extensión territorial.
        ]'''


print('Found old target:', old_target in typ_content)
mod_typ = typ_content.replace(old_target, new_target)
mod_typ = mod_typ.replace(
    'inset: (x: 10pt, top: 8pt, bottom: 8pt),',
    'inset: (x: 6pt, top: 12pt, bottom: 12pt),'
)



temp_typ = r'tareas\actividad_01\entregables\avance 2\temp_render.typ'
temp_pdf = r'pruebas\test_tight.pdf'

with open(temp_typ, 'w', encoding='utf-8') as f:
    f.write(mod_typ)

typst.compile(temp_typ, output=temp_pdf, root=os.path.abspath('.'))
doc = fitz.open(temp_pdf)
print('Total pages:', len(doc))
p8 = doc[8]
pix = p8.get_pixmap(dpi=150)
pix.save(r'pruebas\pagina_8_tight.png')
print('Rendered tight viewBox preview to pruebas\pagina_8_tight.png')
for d in p8.get_drawings():
    r = d['rect']
    if r.width > 400 and r.y0 > 200:
        print(f'Card bottom: {r.y1:.1f}, footer line at 794.3 (difference: {794.3 - r.y1:.1f} pt)')
        break

if os.path.exists(temp_typ): os.remove(temp_typ)
if os.path.exists(test_svg_path): os.remove(test_svg_path)
