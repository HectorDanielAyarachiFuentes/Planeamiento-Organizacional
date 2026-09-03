import pymupdf

doc = pymupdf.open(r"tareas\actividad_01\material\Escenarios futuros para la adm publica-Cao y Blutman.pdf")
pages_to_extract = [39, 40, 59, 60, 61, 88, 89]

for p in pages_to_extract:
    print(f"=== PAGE {p} ===")
    print(doc[p-1].get_text())

