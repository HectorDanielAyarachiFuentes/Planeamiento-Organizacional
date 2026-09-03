import pymupdf

doc = pymupdf.open(r"tareas\actividad_01\entregables\avance 2\Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")
print(f"Total pages: {len(doc)}")

for i, page in enumerate(doc):
    print(f"\n--- Page {i+1} ---")
    text = page.get_text()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    print(f"Number of lines: {len(lines)}")
    print("First 3 lines:", lines[:3])
    print("Last 3 lines:", lines[-3:] if len(lines) >= 3 else lines)
