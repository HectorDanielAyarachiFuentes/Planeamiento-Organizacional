import typst
import pymupdf
import re

with open(r"tareas/actividad_01/entregables/avance 2/Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.typ", "r", encoding="utf-8") as f:
    content = f.read()

# Let's define the map block to insert
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
        #image("/tareas/actividad_01/entregables/avance 2/img/RioNegro.svg", width: 85%)
        #v(3pt)
        #text(size: 7.8pt, fill: text-muted, style: "italic")[
          *Figura 1:* Mapa de la Provincia de Río Negro con división departamental, cabeceras y Sede Central del CURZAS (Viedma), base territorial para el despliegue de los Nodos Regionales y proyectos de extensión.
        ]
      ]
    )
  ]
  #v(2pt)
'''

# Option A: Right after the table in Item 1
pos = content.find("2. *Proyectos de Extensión")
content_a = content[:pos] + map_block + "\n" + content[pos:]

with open(r"pruebas/test_page8_a.typ", "w", encoding="utf-8") as f:
    f.write(content_a)

typst.compile(r"pruebas/test_page8_a.typ", output=r"pruebas/test_page8_a.pdf", root=".")

doc = pymupdf.open(r"pruebas/test_page8_a.pdf")
print("Total pages in Option A:", len(doc))
for i in range(len(doc)):
    text = doc[i].get_text()
    if "B. Evidencia Empírica" in text or "Evidencia Empírica Territorial" in text:
        print(f"Option A: Section B starts on page {i+1}")
        pix = doc[i].get_pixmap(dpi=150)
        pix.save(f"pruebas/opt_a_page_{i+1}.png")
        if i+1 < len(doc):
            pix2 = doc[i+1].get_pixmap(dpi=150)
            pix2.save(f"pruebas/opt_a_page_{i+2}.png")
        if i+2 < len(doc):
            pix3 = doc[i+2].get_pixmap(dpi=150)
            pix3.save(f"pruebas/opt_a_page_{i+3}.png")
        break
