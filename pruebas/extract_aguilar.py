import pymupdf

doc_cao = pymupdf.open(r"tareas\actividad_01\material\continuidades-y-rupturas-en-las-ideas-sobre-reforma-y-modernizacion-del-estado- Cao Horacio.pdf")
print("=== Cao Continuidades y Rupturas ===")
for p in range(len(doc_cao)):
    text = doc_cao[p].get_text()
    if any(k in text.lower() for k in ["gobernanza", "autonom", "autarq", "ngp", "gerencia"]):
        print(f"--- Page {p+1} ---")
        for line in text.split('\n'):
            if any(k in line.lower() for k in ["gobernanza", "autonom", "autarq", "ngp", "gerencial", "weber"]):
                print("  ", line)

doc_aguilar = pymupdf.open(r"tareas\actividad_01\material\aguilar-villanueva-gobernanza-y-gestion-publica.pdf")
print("=== Aguilar Villanueva (Index and Chapter 1 search) ===")
for p in range(10, 35):
    text = doc_aguilar[p].get_text()
    if "gobernanza" in text.lower() or "red" in text.lower():
        print(f"--- Page {p+1} ---")
        lines = text.split('\n')
        for i, l in enumerate(lines):
            if any(k in l.lower() for k in ["concepto", "definici", "red", "sociedad", "silo", "coordinaci", "horizontal"]):
                print("  [L]:", l)

