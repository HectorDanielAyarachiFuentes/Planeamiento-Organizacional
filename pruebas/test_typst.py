import typst

# Test compilation of existing file
input_path = r"tareas\actividad_01\entregables\avance 2\Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.typ"
output_path = r"pruebas\test_output.pdf"

try:
    typst.compile(input_path, output=output_path)
    print("Compilation successful! Output saved to:", output_path)
except Exception as e:
    print("Compilation error:", e)
