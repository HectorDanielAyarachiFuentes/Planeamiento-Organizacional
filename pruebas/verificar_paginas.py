import fitz  # PyMuPDF
import os

pdf3_path = r"Actividades\entregables\actividad_03\Avance_3_Estructura_Organigrama_Flujograma_GDE_CURZAS_Hector_Ayarachi.pdf"
doc3 = fitz.open(pdf3_path)
print(f"Actividad 3 total pages: {len(doc3)}")

for i, page in enumerate(doc3):
    text = page.get_text()
    first_line = text.strip().split("\n")[0] if text.strip() else "[VACIA]"
    print(f"Pág {i+1}: {len(text)} chars | Inicio: {first_line[:60]}")
    if "Organigrama" in text or "Estructura Orgánica Funcional" in text:
        print(f" -> Encontrada referencia a organigrama en pág {i+1}")
        # Render this page as image to inspect
        pix = page.get_pixmap(dpi=150)
        out_img = f"pruebas/preview_act3_pag_{i+1}.png"
        pix.save(out_img)
        print(f" -> Guardada preview en {out_img}")

pdf2_path = r"Actividades\entregables\actividad_02\Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi.pdf"
doc2 = fitz.open(pdf2_path)
print(f"\nActividad 2 total pages: {len(doc2)}")
for i, page in enumerate(doc2):
    text = page.get_text()
    if "Organigrama" in text or "Estructura Orgánica Funcional" in text:
        print(f" -> Encontrada referencia en Act 2 pág {i+1}")
        pix = page.get_pixmap(dpi=150)
        out_img = f"pruebas/preview_act2_pag_{i+1}.png"
        pix.save(out_img)
        print(f" -> Guardada preview en {out_img}")
