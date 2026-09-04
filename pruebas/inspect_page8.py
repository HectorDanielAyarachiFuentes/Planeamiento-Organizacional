import pymupdf

doc = pymupdf.open(r"tareas/actividad_01/entregables/avance 2/Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")
print("Total pages:", len(doc))

for i in range(len(doc)):
    text = doc[i].get_text()
    if "B. Evidencia Empírica" in text or "Evidencia Empírica Territorial" in text:
        print(f"Section B is on page {i+1}")
        # render page i
        pix = doc[i].get_pixmap(dpi=150)
        pix.save(f"pruebas/page_{i+1}.png")
    if i+1 == 9:
        pix = doc[i].get_pixmap(dpi=150)
        pix.save(f"pruebas/page_{i+1}.png")
