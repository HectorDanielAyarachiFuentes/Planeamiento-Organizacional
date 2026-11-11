#import "/Actividades/entregables/actividad_02/modulos/config/estilos.typ": *
#import "/Actividades/entregables/actividad_02/modulos/components/cajas.typ": *

// ==============================================================================
// PREVIEW RÁPIDO: AVANCE 5 — SISTEMAS DE CONTROL, TABLERO DE COMANDO Y EVALUACIÓN
// Compilación ultrarrápida para edición ágil y verificación visual inmediata
// ==============================================================================

#set page(
  paper: "a4",
  margin: (x: 2.3cm, top: 2.4cm, bottom: 2.4cm),
  header: [
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      text(size: 8pt, fill: text-muted)[Planeamiento y Control de las Organizaciones | CURZAS — Avance 5],
      text(size: 8pt, fill: primary, weight: "bold")[UNCo — CURZAS]
    )
    #v(3pt)
    #line(length: 100%, stroke: 0.5pt + border-line)
  ],
  footer: [
    #line(length: 100%, stroke: 0.3pt + border-subtle)
    #v(3pt)
    #grid(
      columns: (1fr, auto, 1fr),
      align: (left + horizon, center + horizon, right + horizon),
      text(size: 8pt, fill: text-muted)[Téc. Sup. en RR. HH. Héctor Daniel Ayarachi Fuentes],
      image("/assets/img/CURZAS.png", height: 13pt),
      text(size: 8pt, fill: text-muted)[
        #context [Página #counter(page).display("1") de #counter(page).final().at(0)]
      ]
    )
  ]
)

// Inclusión del Avance 5
#include "secciones/05_avance5.typ"

// Bibliografía Consolidada
#pagebreak()
#include "secciones/06_bibliografia.typ"

