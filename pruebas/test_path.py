import typst
import os

workspace_root = os.path.abspath(".")
code_test = """
#set page(paper: "a4", margin: 2cm)
#image("/assets/img/CURZAS.png", height: 50pt)
= Test Title
Hello World
"""

with open("pruebas/temp_test.typ", "w", encoding="utf-8") as f:
    f.write(code_test)

try:
    typst.compile("pruebas/temp_test.typ", output="pruebas/temp_test.pdf", root=workspace_root)
    print("SUCCESS: root + /assets/img/CURZAS.png works perfectly!")
except Exception as e:
    print("Error:", e)
