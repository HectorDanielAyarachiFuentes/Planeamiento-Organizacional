import typst
import os

workspace_root = os.path.abspath(".")
input_path = os.path.abspath(r"tareas\actividad_01\entregables\avance 2\Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.typ")
output_path = os.path.abspath(r"tareas\actividad_01\entregables\avance 2\Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")

try:
    typst.compile(input_path, output=output_path, root=workspace_root)
    print("Compiled successfully to PDF with root set to workspace_root!")
except Exception as e:
    print("Compilation error:", e)
