import fitz

svg_path = 'tareas/actividad_01/entregables/avance 2/img/RioNegro.svg'
doc = fitz.open(svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('pruebas/rionegro_before.png')
print('Saved rionegro_before.png:', pix.width, 'x', pix.height)
