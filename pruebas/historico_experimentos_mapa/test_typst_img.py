import typst

code = '''
#set page(paper: "a4")
#image("/Actividades/entregables/actividad_02/img/RioNegro.svg", width: 80%)
'''
with open("pruebas/test_img.typ", "w", encoding="utf-8") as f:
    f.write(code)

try:
    typst.compile("pruebas/test_img.typ", output="pruebas/test_img.pdf", root=".")
    print("Success with root leading slash!")
except Exception as e:
    print("Error:", e)

code2 = '''
#set page(paper: "a4")
#image("img/RioNegro.svg", width: 80%)
'''
with open("Actividades/entregables/actividad_02/test_rel.typ", "w", encoding="utf-8") as f:
    f.write(code2)

try:
    typst.compile("Actividades/entregables/actividad_02/test_rel.typ", output="pruebas/test_rel.pdf", root=".")
    print("Success with relative path!")
except Exception as e:
    print("Error:", e)
