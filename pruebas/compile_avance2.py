import typst
import os

workspace_root = os.path.abspath(".")
input_path = os.path.abspath(r"tareas\actividad_01\entregables\avance 2\Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.typ")
output_path = os.path.abspath(r"tareas\actividad_01\entregables\avance 2\Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")

try:
    typst.compile(input_path, output=output_path, root=workspace_root)
    print("PDF compilation SUCCESSFUL!")
    print("Output file size:", os.path.getsize(output_path), "bytes")
except Exception as e:
    print("PDF compilation FAILED with error:", e)
