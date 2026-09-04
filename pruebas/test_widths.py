import typst
import pymupdf

with open(r"tareas/actividad_01/entregables/avance 2/Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.typ", "r", encoding="utf-8") as f:
    content = f.read()

pos2 = content.find("2. *Proyectos de Extensión")
pos3 = content.find("3. *Mesas Técnicas")

for w in [82, 85, 88, 90, 92]:
    map_block = f'''
  #v(2pt)
  #align(center)[
    #block(
      width: 100%,
      breakable: false,
      fill: bg-card,
      stroke: 0.6pt + border-subtle,
      radius: 4pt,
      inset: (x: 8pt, top: 6pt, bottom: 6pt),
      [
        #image("/tareas/actividad_01/entregables/avance 2/img/RioNegro.svg", width: {w}%)
        #v(3pt)
        #text(size: 7.8pt, fill: text-muted, style: "italic")[
          *Figura 1:* Mapa institucional de Río Negro con división departamental, cabeceras y Sede Central CURZAS (Viedma), articulando la red de Nodos Regionales y proyectos de extensión territorial.
        ]
      ]
    )
  ]
  #v(2pt)
'''
    c_test = content[:pos2] + map_block + "\n" + content[pos2:pos3] + "#pagebreak()\n" + content[pos3:]
    with open(r"pruebas/test_w.typ", "w", encoding="utf-8") as f:
        f.write(c_test)
    typst.compile(r"pruebas/test_w.typ", output=r"pruebas/test_w.pdf", root=".")
    doc = pymupdf.open(r"pruebas/test_w.pdf")
    # Find page of Section B
    for i in range(len(doc)):
        t = doc[i].get_text()
        if "B. Evidencia Empírica" in t:
            p_b = i
            break
    has_item2 = "2. Proyectos de Extensión" in doc[p_b].get_text()
    print(f"Width {w}%: Page 8 has item 2? {has_item2}, Total pages: {len(doc)}")
    if has_item2:
        pix = doc[p_b].get_pixmap(dpi=150)
        pix.save(f"pruebas/w_{w}_p8.png")
