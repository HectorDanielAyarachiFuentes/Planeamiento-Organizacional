import fitz

svg_path = 'Actividades/entregables/actividad_02/img/RioNegro.svg'
doc = fitz.open(svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('pruebas/rionegro_before.png')
print('Saved rionegro_before.png:', pix.width, 'x', pix.height)
