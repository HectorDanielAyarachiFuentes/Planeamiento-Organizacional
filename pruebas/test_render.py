import pymupdf

doc = pymupdf.open(r"tareas/actividad_01/entregables/avance 2/img/RioNegro.svg")
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save(r"pruebas/render_test.png")
print("Rendered successfully to pruebas/render_test.png, size:", pix.width, pix.height)
