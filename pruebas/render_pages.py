import pymupdf
import os

doc = pymupdf.open(r"tareas\actividad_01\entregables\avance 2\Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")
os.makedirs("pruebas/rendered_pages", exist_ok=True)

for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    pix.save(f"pruebas/rendered_pages/page_{i+1}.png")
print("Rendered all pages to pruebas/rendered_pages/")
