# -*- coding: utf-8 -*-
import os
from pathlib import Path

BASE_DIR = Path(r"Actividades/entregables/actividad_02/modulos/secciones")
SOURCE_FILE = BASE_DIR / "04_avance4.typ"
TARGET_DIR = BASE_DIR / "avance_04"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

with open(SOURCE_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line slices (0-indexed)
# 1-66 -> index 0 to 66
# 67-324 -> index 66 to 324
# 325-472 -> index 324 to 472
# 473-565 -> index 472 to 565
# 566-end -> index 565 to end

HEADER = '''#import "../../config/estilos.typ": *
#import "../../components/cajas.typ": *

'''

# 01_introduccion_marcos.typ
# Omit line 1 and 2 if they are already imports
lines_01 = lines[3:66] # starting after import lines
with open(TARGET_DIR / "01_introduccion_marcos.typ", "w", encoding="utf-8") as f:
    f.write(HEADER + "".join(lines_01).lstrip())

# 02_eje1_presupuesto_inciso1.typ
lines_02 = lines[66:324]
with open(TARGET_DIR / "02_eje1_presupuesto_inciso1.typ", "w", encoding="utf-8") as f:
    f.write(HEADER + "".join(lines_02).lstrip())

# 03_eje2_programas_makon.typ
lines_03 = lines[324:472]
with open(TARGET_DIR / "03_eje2_programas_makon.typ", "w", encoding="utf-8") as f:
    f.write(HEADER + "".join(lines_03).lstrip())

# 04_eje3_ciclo_siaf.typ
lines_04 = lines[472:565]
with open(TARGET_DIR / "04_eje3_ciclo_siaf.typ", "w", encoding="utf-8") as f:
    f.write(HEADER + "".join(lines_04).lstrip())

# 05_eje4_sintesis_matus.typ
lines_05 = lines[565:]
with open(TARGET_DIR / "05_eje4_sintesis_matus.typ", "w", encoding="utf-8") as f:
    f.write(HEADER + "".join(lines_05).lstrip())

print("Archivos modulares generados con éxito en:", TARGET_DIR)

