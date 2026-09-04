import typst
import pymupdf

with open(r"tareas/actividad_01/entregables/avance 2/Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.typ", "r", encoding="utf-8") as f:
    content = f.read()

# Let's test placing a clean pagebreak before item 3 or adjusting map size so item 2 finishes page 8
map_block = '''
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
        #image("/tareas/actividad_01/entregables/avance 2/img/RioNegro.svg", width: 80%)
        #v(3pt)
        #text(size: 7.8pt, fill: text-muted, style: "italic")[
          *Figura 1:* Mapa institucional de Río Negro con división departamental, cabeceras y Sede Central CURZAS (Viedma), articulando la red de Nodos Regionales y proyectos de extensión territorial.
        ]
      ]
    )
  ]
  #v(2pt)
'''

# We place map after item 1 table
pos2 = content.find("2. *Proyectos de Extensión")
pos3 = content.find("3. *Mesas Técnicas")

# Test 1: Pagebreak before item 3
content_test1 = content[:pos2] + map_block + "\n" + content[pos2:pos3] + "#pagebreak()\n" + content[pos3:]

with open(r"pruebas/test_clean_break.typ", "w", encoding="utf-8") as f:
    f.write(content_test1)

typst.compile(r"pruebas/test_clean_break.typ", output=r"pruebas/test_clean_break.pdf", root=".")

doc = pymupdf.open(r"pruebas/test_clean_break.pdf")
print("Total pages in Clean Break test:", len(doc))
for i in range(len(doc)):
    text = doc[i].get_text()
    if "B. Evidencia Empírica" in text or "Evidencia Empírica Territorial" in text:
        p8 = doc[i].get_pixmap(dpi=150)
        p8.save(f"pruebas/clean_p8.png")
        p9 = doc[i+1].get_pixmap(dpi=150)
        p9.save(f"pruebas/clean_p9.png")
        p10 = doc[i+2].get_pixmap(dpi=150)
        p10.save(f"pruebas/clean_p10.png")
        break
