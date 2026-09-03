import pymupdf

doc = pymupdf.open(r"tareas\actividad_01\material\Escenarios futuros para la adm publica-Cao y Blutman.pdf")
print("=== Escenarios futuros - Table of Contents or Text on Poligobernanza ===")
for p in range(len(doc)):
    text = doc[p].get_text()
    if "poligobernanza" in text.lower() or "gobernanza" in text.lower():
        print(f"--- Page {p+1} ---")
        for line in text.split('\n'):
            if any(k in line.lower() for k in ["poligobernanza", "plataforma", "ad hoc", "neoweberian", "ngp", "gerencia"]):
                print("  ", line)

doc2 = pymupdf.open(r"tareas\actividad_01\material\aguilar-villanueva-gobernanza-y-gestion-publica.pdf")
print(f"=== Aguilar Villanueva: Pages {len(doc2)} ===")
for p in range(min(15, len(doc2))):
    text = doc2[p].get_text()
    if "gobernanza" in text.lower():
        print(f"--- Page {p+1} ---")
        print(text[:300])
