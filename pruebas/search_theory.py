import pymupdf
import os
import re

material_dir = r"tareas\actividad_01\material"

def search_pdf(filename, terms):
    filepath = os.path.join(material_dir, filename)
    if not os.path.exists(filepath):
        return
    doc = pymupdf.open(filepath)
    print(f"=== {filename} (Pages: {len(doc)}) ===")
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        for term in terms:
            if re.search(term, text, re.IGNORECASE):
                print(f"--- Page {page_num + 1} for term '{term}' ---")
                # print matching snippet
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if re.search(term, line, re.IGNORECASE):
                        snippet = "\n".join(lines[max(0, i-2):min(len(lines), i+3)])
                        print(f"[Line ~{i}]:\n{snippet}\n")
                break

print("Searching Cao y Blutman...")
search_pdf("Escenarios futuros para la adm publica-Cao y Blutman.pdf", ["plataforma", "poligobernanza", "tramado", "ad hoc", "interoperab", "redes", "gobernanza"])
search_pdf("El futuro del empleo publico, tecnologias digitales y estructuras estatales.pdf", ["plataforma", "poligobernanza", "tramado", "ad hoc", "interoperab"])
