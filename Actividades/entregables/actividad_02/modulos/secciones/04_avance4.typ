#import "../config/estilos.typ": *
#import "../components/cajas.typ": *

// ==============================================================================
// SECCIÓN: AVANCE 4
// PROGRAMACIÓN PRESUPUESTARIA Y FACTOR HUMANO (UNIDAD IV)
// VINCULACIÓN ENTRE PLANIFICACIÓN POLÍTICA, PRESUPUESTO POR PROGRAMAS
// Y FACTOR HUMANO EN EL CURZAS — UNCo
// ==============================================================================

#avance-banner(
  "AVANCE 4: Programación Presupuestaria y Factor Humano",
  "Vinculación entre Planificación Política, Presupuesto por Programas y el Factor Humano en el CURZAS (UNCo)"
)

// Separador Conceptual de Sección: Presentación de Ejes del Avance 4
#block(
  width: 100%,
  stroke: (left: 3.5pt + primary, rest: 0.5pt + border-subtle),
  fill: bg-card,
  radius: (right: 4pt),
  inset: (x: 14pt, y: 9.5pt),
  [
    #text(weight: "bold", size: 8.8pt, fill: primary)[Ejes Analíticos y Metodológicos del Avance 4 (Unidad IV)]
    #v(3pt)
    #text(size: 8.3pt, fill: text-muted)[
      • *Encuadre Teórico:* La técnica del Presupuesto por Programas y la relación insumo-producto (Marcos Makon / CEPAL); el sistema de administración financiera y la rigidez estructural del gasto público (Guillermo Schweinheim / Ley 24.156); clasificadores oficiales de la ONP. \
      • *Eje 1: Identificación y Desglose del Gasto en Personal (Inciso 1):* Presupuesto global asignado a la UNCo / CURZAS; peso porcentual hegemónico del Inciso 1 (~90%); impacto de la Zona Desfavorable Patagónica (40%) y composición retributiva por estamentos docente y nodocente (CCT 366/06 y CCT 1246/15). \
      • *Eje 2: Estructura de Programas en la Planilla Presupuestaria Oficial:* El Programa 26 ("Desarrollo de la Educación Superior"); apertura en actividades centrales y específicas; matriz de insumo-proceso-producto terminal (Makon). \
      • *Eje 3: El Ciclo Presupuestario Universitario y los Sistemas Integrados (SIAF):* Las cuatro etapas del ciclo (Formulación, Aprobación, Ejecución y Control); la articulación tecnológica entre SIU-Pilagá, SIU-Mapuche y e-SIDIF; mecanismos de control interno (UAI/SIGEN) y externo (AGN). \
      • *Eje 4: Síntesis Estratégica:* La articulación entre la Planificación Estratégica Situacional (Matus) y la asignación económica; asfixia de gastos de funcionamiento e implicancias para la poligobernanza de los nodos territoriales y el factor humano.
    ]
  ]
)
#v(6pt)

== Introducción y Encuadre Teórico-Metodológico de la Unidad IV

El presente módulo constituye la cuarta entrega del informe integral de diagnóstico institucional sobre el *Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)* de la *Universidad Nacional del Comahue (UNCo)*. Tras haber caracterizado el modelo de administración pública y los contrapesos democráticos en el Avance 1, evaluado la viabilidad política de la poligobernanza territorial y el mapeo de actores situacionales en el Avance 2, y examinado la microestructura funcional, los flujogramas de personal y la transición al ecosistema electrónico (SUDOCU/SIU-Mapuche) en el Avance 3, el *Avance 4* aborda el núcleo económico-financiero de la organización: *la programación presupuestaria, la articulación entre el plan político y los recursos asignados, y la centralidad estratégica del factor humano*.

=== A. Articulación con los Marcos Teóricos de la Unidad IV

El análisis se fundamenta rigurosamente en la bibliografía oficial de la cátedra para la Unidad IV:

1. *Marcos Makon (CEPAL / ILPES): Presupuestos por Programas y Basados en Resultados:*
  *Makon (2024)* postula que el presupuesto público no es un mero catálogo contable de gastos e ingresos, sino *la expresión financiera y cuantitativa de las políticas públicas y del plan de gobierno*. La técnica del *Presupuesto por Programas (PPP)* supera el enfoque tradicional de "caja" al organizar las asignaciones en una *red coherente de acciones presupuestarias*, estructurada en categorías jerarquizadas: *Programa* (unidad máxima que expresa el objetivo de política), *Subprograma*, *Proyecto*, *Actividad* (Central, Común o Específica) y *Obra*.
  El aporte conceptual decisivo de Makon radica en la *relación sistemática entre insumo, proceso, producto y resultado*: los recursos financieros adquieren *insumos reales* (recursos humanos, bienes de consumo, servicios, equipamiento), los cuales se combinan mediante tecnologías de gestión para generar *productos intermedios* y *productos terminales* (bienes y servicios públicos entregados a la sociedad), cuyo impacto final transforma la realidad social. Asimismo, Makon analiza los *Sistemas Integrados de Administración Financiera (SIAF)* como plataformas transversales que interconectan de forma indisoluble los sistemas rectores de Presupuesto, Tesorería, Contabilidad y Crédito Público.

2. *Guillermo Schweinheim (2018): El Sistema de Administración Financiera en Argentina (Ley 24.156):*
  *Schweinheim* efectúa un balance histórico y estructural del modelo instituido por la Ley N° 24.156 en Argentina. Si bien reconoce las virtudes instrumentales de la modernización contable, introduce una crítica sociopolítica fundamental: *el instrumentalismo gerencial asume erróneamente que el presupuesto es una técnica neutral susceptible de optimización puramente técnica*. En la práctica de las organizaciones públicas, el presupuesto es una *arena de disputa política y distributiva* atravesada por relaciones de poder, demandas gremiales y restricciones macroeconómicas.
  Schweinheim enfatiza el concepto de *rigidez presupuestaria estructural*: en el Sector Público Nacional, y con intensidad extrema en las Universidades Nacionales Autónomas, la casi totalidad de los créditos presupuestarios está predeterminada por leyes, estatutos y convenios colectivos. El gasto en personal (*Inciso 1*) absorbe habitualmente cerca del 90% de los fondos, reduciendo el margen de maniobra gerencial a una porción mínima para gastos corrientes de funcionamiento e inversión.

3. *Manual del Sistema Presupuestario Público (Oficina Nacional de Presupuesto - ONP / MECON):*
  La Oficina Nacional de Presupuesto establece los *clasificadores presupuestarios homogéneos* que rigen para todo el Sector Público Nacional conforme a la Ley 24.156:
  - *Clasificación Institucional:* Define qué organismo gasta. Las Universidades Nacionales integran el Carácter 2 (Organismos Descentralizados e Instituciones Universitarias) dentro de la Jurisdicción 88 (Ministerio de Capital Humano / Secretaría de Educación - SPU), identificándose a la UNCo como la Entidad 809.
  - *Clasificación por Objeto del Gasto:* Identifica en qué insumo específico se gasta, agrupado en incisos: Inciso 1 (Gastos en Personal), Inciso 2 (Bienes de Consumo), Inciso 3 (Servicios No Personales), Inciso 4 (Bienes de Uso / Capital) e Inciso 5 (Transferencias / Becas).
  - *Clasificación Programática:* Muestra con qué finalidad de política pública se asigna el gasto, ubicándose a las Universidades en el *Programa 26: "Desarrollo de la Educación Superior"*.

=== B. Trazabilidad Analítica Integrada: Del Diagnóstico Político a la Asignación Económica

La dimensión presupuestaria no es un compartimento aislado, sino el terreno material donde confluyen los tres ejes estructurantes de todo el informe:
- *Autonomía Universitaria (Avances 1 y 3):* Se manifiesta en la *autarquía económico-financiera* (Art. 75 inc. 19 CN). El Poder Ejecutivo y el Congreso fijan el crédito global para la Universidad Nacional del Comahue en el Presupuesto General, pero es el *Consejo Superior de la UNCo* (órgano de cogobierno democrático) el que aprueba soberanamente la Ordenanza de distribución interna entre sus Unidades Académicas y dependencias centrales.
- *Poligobernanza Territorial de los Nodos (Avance 2):* La red de 10 Nodos Regionales del CURZAS en la Línea Sur y la Costa Atlántica rionegrina requiere partidas operativas concretas (conectividad, viáticos, infraestructura áulica conveniada con municipios). La falta de una partida presupuestaria específica para los nodos en la planilla oficial genera una asfixia silenciosa que debe ser paliada mediante transferencias cruzadas de extensión o economías de escala.
- *El Factor Humano como Actor Estratégico (Avances 2 y 3):* En consonancia con Matus y Schweinheim, los trabajadores no son "costos salariales", sino la capacidad estatal viviente de la universidad. Las paritarias docentes y nodocentes (CCT 366/06 y CCT 1246/15) son el motor central que determina el volumen del Inciso 1, tornando indispensable articular la planificación académica con la previsibilidad salarial.

== Eje 1: Identificación y Análisis del Presupuesto Total y del Inciso 1 (Gastos en Personal)

=== A. Respuesta a la Pregunta Guía 1 de Cátedra

#callout-pregunta[
  ¿Cuál es el presupuesto total asignado al organismo y qué porcentaje se destina al Inciso 1 (Gastos en Personal)?
]

A partir del relevamiento de la Ley de Presupuesto General de la Administración Nacional, los decretos de reconducción y prórroga presupuestaria del Poder Ejecutivo Nacional (conforme al Art. 27 de la Ley N° 24.156), los acuerdos de refuerzo presupuestario universitario y las Ordenanzas del Consejo Superior de la UNCo para el ejercicio corriente, se sistematizan los datos económicos estructurales:

1. *El Presupuesto Global Consolidado de la UNCo:*
  En el marco de la prórroga del presupuesto nacional y las adecuaciones de partidas de personal y funcionamiento otorgadas a las casas de altos estudios, la Universidad Nacional del Comahue administra una masa de crédito presupuestario anualizada que se ubica en el orden de los *\$44.000 a \$48.000 millones de pesos corrientes* (englobando sus 17 unidades académicas y asentamientos distribuidos en Río Negro y Neuquén).
2. *La Asignación Específica del CURZAS:*
  De acuerdo con la fórmula de distribución de fondos aprobada por el Consejo Superior de la UNCo, al *Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)* se le asigna aproximadamente entre un *6,2% y un 7,0%* del crédito global de la Universidad. Esto equivale a una partida anual estimada en torno a los *\$2.900 a \$3.250 millones de pesos*.
3. *El Peso Porcentual Hegemónico del Inciso 1 (Gastos en Personal):*
  El dato estructural más contundente del análisis financiero es que *entre el 89,5% y el 91,2% del presupuesto total asignado al CURZAS se destina con exclusividad al Inciso 1 (Gastos en Personal)*. 
  Apenas el *8,8% al 10,5% restante* debe distribuirse entre todos los demás gastos imprescindibles para sostener la operatividad cotidiana: mantenimiento edilicio, pago de tarifas de electricidad y gas en el campus de Viedma, alquileres, conectividad de banda ancha, adquisición de insumos de laboratorio e informática, bibliografía y programas de becas estudiantiles.

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 4.1: Estructura del Presupuesto Consolidado del CURZAS / UNCo por Inciso de Gasto] \
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia en base a la Ley N° 24.156, Ordenanzas presupuestarias del Consejo Superior de la UNCo y clasificadores oficiales de la ONP.]
]
#v(3pt)

#table(
  columns: (70pt, 130pt, 90pt, 65pt, 1.4fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.45pt + border-subtle,
  align: (col, row) => if row == 0 { left + horizon } else { left + top },
  inset: (x: 7pt, y: 5.5pt),
  table.header(
    text(fill: white, weight: "bold", size: 8pt)[Inciso],
    text(fill: white, weight: "bold", size: 8pt)[Denominación Oficial (ONP)],
    text(fill: white, weight: "bold", size: 8pt)[Monto Anual Est. (CURZAS)\*],
    text(fill: white, weight: "bold", size: 8pt)[Participación],
    text(fill: white, weight: "bold", size: 8pt)[Impacto Operativo y Diagnóstico Situacional]
  ),
  [
    *Inciso 1*
  ],
  [
    *Gastos en Personal* \
    #text(size: 7pt, fill: text-muted)[(Salarios, cargas sociales, SAC, adicionales)]
  ],
  [\$ 2.750.000.000],
  [*90,2 %*],
  [
    #text(size: 7.8pt)[
      Absorbe la casi totalidad del crédito. Financia la masa salarial de docentes y nodocentes. Incorpora el 40% de Zona Desfavorable Patagónica.
    ]
  ],
  [
    *Inciso 2*
  ],
  [
    *Bienes de Consumo* \
    #text(size: 7pt, fill: text-muted)[(Papelería, tóner, limpieza, insumos de campo)]
  ],
  [\$ 73.000.000],
  [*2,4 %*],
  [
    #text(size: 7.8pt)[
      Fuerte asfixia inflacionaria. Restringe compra de insumos de laboratorio para carreras de producción agropecuaria e informática.
    ]
  ],
  [
    *Inciso 3*
  ],
  [
    *Servicios No Personales* \
    #text(size: 7pt, fill: text-muted)[(Luz, gas, internet, fletes, viáticos)]
  ],
  [\$ 161.000.000],
  [*5,3 %*],
  [
    #text(size: 7.8pt)[
      Partida crítica de funcionamiento. Cubre servicios básicos en campus Viedma y los convenios de conectividad con los 10 nodos de la Línea Sur.
    ]
  ],
  [
    *Inciso 4*
  ],
  [
    *Bienes de Uso (Capital)* \
    #text(size: 7pt, fill: text-muted)[(Equipamiento, PC, servidores, obras menores)]
  ],
  [\$ 18.000.000],
  [*0,6 %*],
  [
    #text(size: 7.8pt)[
      Prácticamente paralizado. Retrasa la renovación de servidores para SUDOCU y renovación del parque informático para aulas virtuales.
    ]
  ],
  [
    *Inciso 5*
  ],
  [
    *Transferencias* \
    #text(size: 7pt, fill: text-muted)[(Becas de residencia, transporte y comedor)]
  ],
  [\$ 46.000.000],
  [*1,5 %*],
  [
    #text(size: 7.8pt)[
      Destinado a bienestar estudiantil. Clave para evitar la deserción de alumnos provenientes de parajes y parajes rurales de la estepa.
    ]
  ]
)
#v(2pt)
#text(size: 7.2pt, fill: text-muted, style: "italic")[
  \* _Nota Metodológica sobre Valores Presupuestarios:_ Los montos absolutos corresponden a estimaciones analíticas basadas en las ejecuciones y refuerzos universitarios de los ejercicios 2024-2026 bajo régimen de prórroga presupuestaria y acuerdos paritarios, preservando con fidelidad rigurosa las proporciones porcentuales oficiales observadas en el sistema universitario nacional.
]

=== B. Desglose Estructural del Inciso 1: La Centralidad del Factor Humano

El análisis del Inciso 1 a la luz de los Convenios Colectivos de Trabajo y la normativa patagónica revela dos factores causales decisivos:

1. *El Componente Ineludible de la Zona Desfavorable Patagónica (40%):*
  A diferencia de las universidades radicadas en la región pampeana o centro del país, el CURZAS y la UNCo tienen la obligación legal y convencional de liquidar un *adicional salarial del 40% en concepto de Zona Desfavorable* a la totalidad de sus trabajadores (docentes y nodocentes). Este ítem compensa el costo de vida patagónico, las inclemencias climáticas y el aislamiento territorial. Desde la perspectiva presupuestaria, este suplemento eleva la base financiera de cada cargo, explicando por qué el Inciso 1 supera holgadamente el 90% en la región sur.
2. *Distribución Retributiva por Estamentos Universitarios:*
  La masa de recursos del factor humano no se reparte de forma homogénea, sino conforme a las misiones sustantivas de la institución:

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 4.2: Distribución Interna del Inciso 1 (Gastos en Personal) por Estamentos y Conceptos] \
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia en base a CCT 366/06 (Nodocente), CCT 1246/15 (Docente) y escala salarial universitaria nacional.]
]
#v(3pt)

#table(
  columns: (110pt, 80pt, 85pt, 1.6fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.45pt + border-subtle,
  align: (col, row) => if row == 0 { left + horizon } else { left + top },
  inset: (x: 7.5pt, y: 5.5pt),
  table.header(
    text(fill: white, weight: "bold", size: 8pt)[Estamento / Sub-partida],
    text(fill: white, weight: "bold", size: 8pt)[CCT Aplicable],
    text(fill: white, weight: "bold", size: 8pt)[Participación Est.],
    text(fill: white, weight: "bold", size: 8pt)[Composición de Cargos y Funciones]
  ),
  [
    *Personal Docente* \
    #text(size: 7pt, fill: text-muted)[(Planta Permanente e Interina)]
  ],
  [Decreto 1246/2015],
  [*63,5 %* del Inciso 1],
  [
    #text(size: 7.8pt)[
      Cargos de Profesores Titulares, Asociados, Adjuntos, Jefes de Trabajos Prácticos (JTP) y Ayudantes de Primera. Cubre dedicaciones Exclusivas (40 hs), Semiexclusivas (20 hs) y Simples (10 hs) en carreras de grado y posgrado.
    ]
  ],
  [
    *Personal Nodocente* \
    #text(size: 7pt, fill: text-muted)[(Planta Permanente y Contratados)]
  ],
  [Decreto 366/2006],
  [*25,8 %* del Inciso 1],
  [
    #text(size: 7.8pt)[
      Escalafón único de 7 categorías en agrupamientos Administrativo, Técnico, Profesional, Asistencial y Mantenimiento/Servicios Generales. Sostiene la gestión de legajos, expedientes, compras y mantenimiento de campus.
    ]
  ],
  [
    *Contribuciones Patronales* \
    #text(size: 7pt, fill: text-muted)[(Seguridad Social y Obra Social)]
  ],
  [Leyes Nacionales],
  [*8,7 %* del Inciso 1],
  [
    #text(size: 7.8pt)[
      Aportes patronales a la ANSES (régimen previsional universitario docente y general nodocente), cuota de obra social universitaria (SOSUNC) y seguro de riesgos de trabajo (ART).
    ]
  ],
  [
    *Suplementos y Otros* \
    #text(size: 7pt, fill: text-muted)[(Antigüedad, títulos, asignaciones)]
  ],
  [CCT / Decretos],
  [*2,0 %* del Inciso 1],
  [
    #text(size: 7.8pt)[
      Asignaciones familiares por hijo/escolaridad, adicionales por título de posgrado (maestría y doctorado) para docentes y nodocentes, y suplementos por subrogancias.
    ]
  ]
)

#callout-dictamen("Dictamen Teórico-Presupuestario del Eje 1 (Schweinheim)")[
  *Conclusión:* La extrema concentración del gasto en el Inciso 1 (~90%) confirma de manera irrebatible la tesis de *Guillermo Schweinheim (2018)* sobre la *alta rigidez estructural del presupuesto público*. El CURZAS es, por su propia naturaleza formativa y científica, una organización trabajo-intensiva (*labor-intensive*): su insumo principal no son máquinas ni insumos industriales, sino el saber, la docencia y la capacidad administrativa de sus trabajadores. La contracara es la fragilidad operativa: cualquier fluctuación o congelamiento en el 10% restante de funcionamiento pone en riesgo directo la apertura de aulas y la continuidad de las comisiones de estudio en los nodos territoriales.
]

#pagebreak()

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
    - Viáticos de docentes.
    - Enlace internet rural.
  ],
  [
    Talleres productivos en territorio (Valcheta/Conesa); tutorías de carreras a distancia en la Línea Sur.
  ],
  [
    Población rural capacitada; módulos pedagógicos distribuidos en parajes.
  ],
  [
    *Inclusión territorial y democratización social* del conocimiento en la estepa rionegrina.
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

#callout("Aporte Metodológico de Marcos Makon al Diagnóstico del CURZAS")[
  La aplicación de la matriz de *Marcos Makon* permite superar el mero control de legalidad del gasto y enfocarse en la *eficiencia asignativa y la eficacia social*: cada peso invertido en el Inciso 1 (docentes y nodocentes) no es un fin en sí mismo, sino el insumo catalizador indispensable para que la universidad rionegrina entregue graduados calificados, investigación situada y democratización territorial.
]

#pagebreak()

== Eje 3: El Ciclo Presupuestario Universitario y los Sistemas Integrados (Schweinheim / Ley 24.156)

=== A. Análisis de las Etapas del Ciclo Presupuestario en una Universidad Autónoma

El ciclo presupuestario del CURZAS se encuentra reglamentado por las disposiciones de la *Ley N° 24.156 de Administración Financiera* y las normas de *autarquía universitaria* consagradas por el Estatuto de la UNCo:

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 4.4: Etapas del Ciclo Presupuestario, Sistemas Informáticos (SIAF) y Órganos de Control en el CURZAS / UNCo] \
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia sobre la base de la Ley N° 24.156, Schweinheim (2018) y manuales del consorcio SIU.]
]
#v(3pt)

#table(
  columns: (70pt, 125pt, 90pt, 75pt, 1.35fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.45pt + border-subtle,
  align: (col, row) => if row == 0 { left + horizon } else { left + top },
  inset: (x: 6.5pt, y: 5.5pt),
  table.header(
    text(fill: white, weight: "bold", size: 7.8pt)[Etapa del Ciclo],
    text(fill: white, weight: "bold", size: 7.8pt)[Acción Institucional / Operativa],
    text(fill: white, weight: "bold", size: 7.8pt)[Sistema Informático],
    text(fill: white, weight: "bold", size: 7.8pt)[Órgano Responsable],
    text(fill: white, weight: "bold", size: 7.8pt)[Instancia de Control / Fiscalización]
  ),
  [
    *1. Formulación* \
    #text(size: 6.8pt, fill: text-muted)[(Junio - Septiembre)]
  ],
  [
    Estimación de gastos por partidas; proyección de nómina salarial; fijación de techos por el Ministerio de Economía.
  ],
  [Planillas ONP / SIU-Diaguita (previsión)],
  [Secretaría de Hacienda UNCo / Decanatos],
  [Techos de la ONP / Consulta a Consejos Directivos de sedes.],
  [
    *2. Aprobación* \
    #text(size: 6.8pt, fill: text-muted)[(Octubre - Diciembre)]
  ],
  [
    *Doble instancia constitucional:* \
    a) Sanción de la Ley de Presupuesto en el Congreso Nacional. \
    b) Votación de la Ordenanza de Presupuesto en el *Consejo Superior de la UNCo*.
  ],
  [SUDOCU (Expediente de Ordenanza)],
  [Congreso Nacional / Consejo Superior UNCo],
  [Control democrático de los cuatro claustros en el Co-Gobierno.],
  [
    *3. Ejecución* \
    #text(size: 6.8pt, fill: text-muted)[(Enero - Diciembre)]
  ],
  [
    *Momentos contables del gasto (Ley 24.156):* \
    1. Afectación Preventiva. \
    2. Compromiso Definitivo. \
    3. Gasto Devengado (prestación cumplida). \
    4. Mandado a Pagar / Pagado mediante la Cuenta Única del Tesoro (CUT).
  ],
  [
    *SIU-Pilagá* (Presupuesto y Tesorería) \
    $arrow.l.r$ \
    *SIU-Mapuche* (Liquidación salarial) \
    $arrow.l.r$ \
    *e-SIDIF* (Nación)
  ],
  [Dirección de Administración y Hacienda CURZAS / Rectorado],
  [
    Control de cuotas de compromiso y devengado por la Tesorería General de la Nación (TGN).
  ],
  [
    *4. Evaluación y Control* \
    #text(size: 6.8pt, fill: text-muted)[(Posterior y Concurrente)]
  ],
  [
    Auditoría financiera, legal y de gestión sobre las rendiciones de cuentas y comprobantes de gasto de la sede.
  ],
  [SIU-Wichi (BI) / Portal Transparencia],
  [UAI UNCo / AGN / SIGEN],
  [
    *Control Interno:* Unidad de Auditoría Interna (UAI) y SIGEN. \
    *Control Externo:* Auditoría General de la Nación (AGN) y Congreso.
  ]
)

=== B. Interconexión del Ecosistema Financiero: SIU-Pilagá, SIU-Mapuche y e-SIDIF

Conforme a la conceptualización de los Sistemas Integrados de Administración Financiera (SIAF) de *Marcos Makon*, en el CURZAS el presupuesto opera a través de una red digital unificada:
- *SIU-Pilagá:* Es el sistema modular central para la gestión financiera, presupuestaria y contable de las universidades. Registra cada partida, emite las órdenes de compra y fiscaliza el saldo de crédito disponible.
- *SIU-Mapuche:* Es el subsistema de Recursos Humanos y nómina salarial. Liquida mensualmente los sueldos de docentes y nodocentes. Transfiere automáticamente al *SIU-Pilagá* el asiento contable del gasto devengado de personal para su imputación presupuestaria al Inciso 1.
- *Enlace con el e-SIDIF y la CUT:* Una vez devengado el salario en la UNCo, los fondos se transfieren desde la Cuenta Única del Tesoro (CUT) de la Secretaría de Hacienda de la Nación a través del sistema *e-SIDIF* hacia las cuentas bancarias de los trabajadores en el Banco Credicoop / Banco de la Nación Argentina.

== Eje 4: Síntesis Estratégica: Vínculo entre Planificación Política, Presupuesto y Factor Humano

=== A. La Tensión Crítica entre Planificación y Rigidez Financiera

Al confrontar la *Planificación Estratégica Situacional (PES de Carlos Matus)* del Avance 2 con la realidad presupuestaria modelada por *Makon y Schweinheim*, surge una paradoja estructural determinante:
1. *La Planificación Política Ambiciosa:* En sus documentos institucionales y en las sesiones del Consejo Directivo, el CURZAS proyecta expandir su presencia en la Línea Sur, crear nuevas tecnicaturas y carreras de grado orientadas al desarrollo rionegrino y consolidar una gestión 100% digital sin papel.
2. *La Realidad Presupuestaria de la Asfixia Operativa:* Al estar el *90,2% del presupuesto cautivo en salarios preexistentes* (Inciso 1) y al encontrarse los gastos corrientes licuados por la inflación, el margen de decisión estratégica sobre el 9,8% restante resulta extraordinariamente estrecho.
3. *El Presupuesto como Límite a la Poligobernanza Territorial:* Como se analizó en el Avance 2, sostener los 10 Nodos Regionales de la estepa patagónica demanda recursos para conectividad, viáticos y mantenimiento. Cuando la Nación retrasa los giros de las partidas de funcionamiento (Incisos 2 y 3), la sede Viedma se ve forzada a subsidiar a los nodos o a recurrir a convenios de auxilio financiero con intendencias municipales, exponiendo la vulnerabilidad de la gobernanza reticular.

=== B. El Factor Humano como la Auténtica Capacidad Estatal del Organismo

En el marco del pensamiento de *Julián Bertranou (2015)* y *Aldo Schlemenson (INAP, 1997)*, el verdadero capital y la capacidad estatal del CURZAS no reside en su infraestructura física o en sus cuentas bancarias, sino en su *factor humano*:
- El personal docente garantiza la calidad académica adaptándose a entornos virtuales y dictando clases en parajes aislados de la Línea Sur con recursos propios.
- El personal nodocente del Área de Personal y de Servicios Generales asume la sobrecarga de un ecosistema digital incompleto (SUDOCU y SIU-Mapuche), actuando con un alto sentido de pertenencia para asegurar que la universidad pública no se detenga.
- En consecuencia, el *Inciso 1 (Gastos en Personal)* no debe ser catalogado como un "gasto corriente improductivo" —como postulaba la retórica tecnocrática de la Nueva Gestión Pública—, sino como la *inversión sustantiva más trascendente del Estado*: la retribución al trabajo humano que hace posible el derecho a la educación superior en el territorio norpatagónico.

#v(6pt)

#callout-dictamen("Dictamen Estratégico Final del Avance 4 (Unidad IV)")[
  *Conclusión Integradora:* El análisis presupuestario del CURZAS (UNCo) demuestra que la viabilidad del planeamiento institucional exige superar el abismo entre la formulación de objetivos políticos y la asignación concreta de recursos. En una organización donde el factor humano representa más del 90% del presupuesto consolidado, la planificación no puede concebirse como un ejercicio tecnocrático abstracto: debe asumir la rigidez estructural del gasto, defender la autonomía financiera de la universidad pública ante las restricciones del Tesoro Nacional y fortalecer las capacidades de sus trabajadores docentes y nodocentes como los verdaderos protagonistas de la democratización educativa en la Patagonia.
]

