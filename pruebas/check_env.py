import os
try:
    import fitz # PyMuPDF
    print("PyMuPDF (fitz) is available")
except ImportError:
    print("PyMuPDF not available")

try:
    import typst
    print("typst is available")
except ImportError:
    print("typst not available")

material_dir = r"tareas\actividad_01\material"
for f in os.listdir(material_dir):
    print(f, os.path.getsize(os.path.join(material_dir, f)))
