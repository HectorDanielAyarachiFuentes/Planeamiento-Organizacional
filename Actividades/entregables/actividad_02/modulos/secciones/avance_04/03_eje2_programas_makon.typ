#import "../../config/estilos.typ": *
#import "../../components/cajas.typ": *

== Eje 2: Estructura de Programas y la Técnica de Presupuesto por Programas (Makon)

=== A. Respuesta a la Pregunta Guía 2 de Cátedra

#callout-pregunta[
  ¿Cómo se estructuran los programas del organismo en la planilla presupuestaria oficial?
]

En la planilla presupuestaria oficial de la Administración Pública Nacional, confeccionada con arreglo a las directivas de la *Oficina Nacional de Presupuesto (ONP)*, la Universidad Nacional del Comahue y sus unidades académicas dependientes se estructuran bajo un esquema programático formalizado:

1. *El Programa Presupuestario Rector: Programa 26:*
  A nivel nacional, la totalidad de los créditos asignados a las Universidades Nacionales dentro de la *Jurisdicción 88 (Ministerio de Capital Humano / Secretaría de Educación)* se agrupan en el:
  - *Programa 26: "Desarrollo de la Educación Superior"*
  Este programa macro define como objetivo de política pública la formación de profesionales, la generación de conocimientos científicos y la extensión hacia la comunidad.
2. *Apertura en Subprogramas y Actividades en la Planilla de la UNCo / CURZAS:*
  Para canalizar la ejecución presupuestaria hacia el territorio, el presupuesto del CURZAS se desagrega internamente en *categorías programáticas específicas*, diferenciando claramente las *Actividades Centrales de Conducción* de las *Actividades Específicas de Producción Académica y Extensión*:
  - *Actividad 01 — Conducción Institucional y Gestión Administrativa Central:* Agrupa los gastos de gobierno (Consejo Directivo y Decanato), las Secretarías de gestión, la Dirección de Personal, Mesa de Entradas, Tesorería y Contable. Su objetivo es brindar soporte y gobernabilidad a toda la sede.
  - *Actividad 02 — Formación Académica de Grado, Pregrado y Posgrado:* Es el núcleo terminal sustantivo. Asigna los cargos docentes a los Departamentos de Administración, Psicopedagogía, Humanidades y Lengua, y Producción Agropecuaria.
  - *Actividad 03 — Extensión Universitaria, Vinculación y Territorialidad:* Financia los proyectos comunitarios y la logística de acompañamiento de los *10 Nodos Regionales de la Línea Sur y la Costa*.
  - *Actividad 04 — Investigación Científica y Transferencia Tecnológica:* Financia los Proyectos de Investigación (PIN/PI) y programas de becas científicas en convenio con CONICET.

=== B. Aplicación Situada de la Matriz de Insumo-Proceso-Producto (Marcos Makon)

Aplicando la metodología de *Marcos Makon (2024)*, el presupuesto del CURZAS se conceptualiza como un sistema articulado donde los créditos monetarios se transforman en *insumos reales* para ejecutar *procesos formativos* y entregar *productos públicos tangibles*:

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 4.3: Matriz de Categorías Programáticas y Relación Insumo-Producto en el CURZAS (Makon / ONP)] \
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia a partir de la metodología de Presupuesto por Programas de Marcos Makon (CEPAL, 2024) y planilla oficial ONP.]
]
#v(3pt)

#table(
  columns: (65pt, 85pt, 105pt, 1.25fr, 1.1fr, 1.1fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.45pt + border-subtle,
  align: (col, row) => if row == 0 { left + horizon } else { left + top },
  inset: (x: 5.5pt, y: 5pt),
  table.header(
    text(fill: white, weight: "bold", size: 7.2pt)[Categoría],
    text(fill: white, weight: "bold", size: 7.2pt)[Denominación],
    text(fill: white, weight: "bold", size: 7.2pt)[Insumos Reales Críticos],
    text(fill: white, weight: "bold", size: 7.2pt)[Acción Presupuestaria (Proceso)],
    text(fill: white, weight: "bold", size: 7.2pt)[Producto Intermedio],
    text(fill: white, weight: "bold", size: 7.2pt)[Producto Terminal (Impacto)]
  ),
  [
    *Actividad 01* \
    #text(size: 6.8pt, fill: text-muted)[Central]
  ],
  [
    *Gobierno y Administración*
  ],
  [
    - Horas nodocente (Dir. Personal/Hacienda).
    - Licencias SUDOCU.
    - Suministros oficina.
  ],
  [
    Gestión de legajos, liquidación en SIU-Mapuche, compras, mantenimiento edilicio y resoluciones de Decanato.
  ],
  [
    Expedientes tramitados en SUDOCU; resoluciones emitidas; haberes liquidados en término.
  ],
  [
    Sostenibilidad institucional y gobernabilidad democrática del complejo.
  ],
  [
    *Actividad 02* \
    #text(size: 6.8pt, fill: text-muted)[Específica]
  ],
  [
    *Enseñanza de Grado y Posgrado*
  ],
  [
    - Horas docentes titulares/adjuntos.
    - Aulas físicas y plataforma Moodle (PED).
  ],
  [
    Dictado de cátedras teóricas y prácticas en Administración, RRHH, Psicopedagogía, Arte y Enfermería.
  ],
  [
    Comisiones dictadas; mesas de examen registradas en SIU-Guaraní; estudiantes regulares.
  ],
  [
    *Graduados Universitarios* insertos en el mercado laboral y sector público norpatagónico.
  ],
  [
    *Actividad 03* \
    #text(size: 6.8pt, fill: text-muted)[Específica]
  ],
  [
    *Extensión y Red de Nodos*
  ],
  [
    - Asistentes técnicos locales en Nodos.
    - Viáticos y traslados de docentes.
    - Conectividad satelital / banda ancha (Inciso 3).
    - Espacios físicos municipales conveniados.
  ],
  [
    Articulación de poligobernanza con municipios locales; tutorías a distancia y clases híbridas en la estepa; talleres productivos en territorio (Valcheta, Jacobacci, Conesa).
  ],
  [
    10 Nodos regionales operativos; población rural capacitada; conectividad y logística costeados con cargo al Inciso 3 (\$258,6 M para todo el CURZAS).
  ],
  [
    *Inclusión territorial y democratización social* de la educación superior en la estepa, superando la brecha geográfica mediante cogestión municipal.
  ],
  [
    *Actividad 04* \
    #text(size: 6.8pt, fill: text-muted)[Específica]
  ],
  [
    *Investigación y Posgrado*
  ],
  [
    - Docentes con dedicación exclusiva.
    - Reactivos campo.
    - Becas posgrado.
  ],
  [
    Ejecución de proyectos de investigación sobre recursos hídricos, producción ovina y políticas sociales.
  ],
  [
    Informes de avance de PIN; tesis dirigidas; ponencias en congresos científicos.
  ],
  [
    *Conocimiento científico situado* y soluciones socioambientales para la Patagonia.
  ]
)

#v(3pt)

#callout("El Impacto Concreto del Financiamiento en la Actividad 03 (Nodos Territoriales y Poligobernanza)")[
  El análisis programático bajo la metodología de *Marcos Makon* pone de relieve un condicionante estructural crucial: los *10 Nodos Regionales del CURZAS en la Línea Sur y la Costa Atlántica* dependen casi con exclusividad del *Inciso 3 (Servicios No Personales)* para financiar la conectividad a internet de banda ancha satelital, los servicios básicos de los espacios áulicos y los viáticos y movilidad de las comisiones docentes.
  Dado que la totalidad del Inciso 3 asignado al CURZAS asciende a apenas *\$258.640.000 anuales* para atender de forma conjunta las demandas del campus central de Viedma (electricidad, gas, mantenimiento, telefonía e informática) y de toda la sede, el margen presupuestario remanente para los nodos resulta extraordinariamente exiguo. Esta restricción material demuestra técnicamente la necesidad imperiosa de la *poligobernanza reticular* (analizada en el Avance 2): sin los acuerdos de cooperación y cogestión formalizados con los municipios locales —que aportan los edificios comunales, la energía y el personal de apoyo local—, el CURZAS no podría sostener su despliegue territorial únicamente con sus partidas presupuestarias ordinarias.
]

#v(3pt)

#callout("Aporte Metodológico de Marcos Makon al Diagnóstico del CURZAS")[
  La aplicación de la matriz de *Marcos Makon* permite superar el mero control de legalidad del gasto y enfocarse en la *eficiencia asignativa y la eficacia social*: cada peso invertido en el Inciso 1 (docentes y nodocentes) no es un fin en sí mismo, sino el insumo catalizador indispensable para que la universidad rionegrina entregue graduados calificados, investigación situada y democratización territorial.
]

#pagebreak()

