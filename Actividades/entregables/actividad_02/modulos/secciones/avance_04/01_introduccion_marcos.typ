#import "../../config/estilos.typ": *
#import "../../components/cajas.typ": *

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
  - *Clasificación por Fuente de Financiamiento:* Según el clasificador de la ONP, el presupuesto universitario se financia de manera abrumadoramente mayoritaria a través de la *Fuente 11 (Tesoro Nacional)*, que cubre aproximadamente el *98%* del presupuesto ordinario (destinado a la masa salarial y funcionamiento básico), mientras que la *Fuente 12 (Recursos Propios)* representa apenas el *2%* restante (generado por aranceles de carreras de posgrado, diplomaturas y convenios de servicios o transferencias técnicas a terceros). Esta marcada asimetría confirma la extrema dependencia financiera respecto a las transferencias del Estado Nacional.
  - *Clasificación por Objeto del Gasto:* Identifica en qué insumo específico se gasta, agrupado en incisos: Inciso 1 (Gastos en Personal), Inciso 2 (Bienes de Consumo), Inciso 3 (Servicios No Personales), Inciso 4 (Bienes de Uso / Capital) e Inciso 5 (Transferencias / Becas).
  - *Clasificación Programática:* Muestra con qué finalidad de política pública se asigna el gasto, ubicándose a las Universidades en el *Programa 26: "Desarrollo de la Educación Superior"*.

=== B. Trazabilidad Analítica Integrada: Del Diagnóstico Político a la Asignación Económica

La dimensión presupuestaria no es un compartimento aislado, sino el terreno material donde confluyen los tres ejes estructurantes de todo el informe:
- *Autonomía Universitaria (Avances 1 y 3):* Se manifiesta en la *autarquía económico-financiera* (Art. 75 inc. 19 CN). El Poder Ejecutivo y el Congreso fijan el crédito global para la Universidad Nacional del Comahue en el Presupuesto General, pero es el *Consejo Superior de la UNCo* (órgano de cogobierno democrático) el que aprueba soberanamente la Ordenanza de distribución interna entre sus Unidades Académicas y dependencias centrales.
- *Poligobernanza Territorial de los Nodos (Avance 2):* La red de 10 Nodos Regionales del CURZAS en la Línea Sur y la Costa Atlántica rionegrina requiere partidas operativas concretas (conectividad, viáticos, infraestructura áulica conveniada con municipios). La falta de una partida presupuestaria específica para los nodos en la planilla oficial genera una asfixia silenciosa que debe ser paliada mediante transferencias cruzadas de extensión o economías de escala.
- *El Factor Humano como Actor Estratégico (Avances 2 y 3):* En consonancia con Matus y Schweinheim, los trabajadores no son "costos salariales", sino la capacidad estatal viviente de la universidad. Las paritarias docentes y nodocentes (CCT 366/06 y CCT 1246/15) son el motor central que determina el volumen del Inciso 1, tornando indispensable articular la planificación académica con la previsibilidad salarial.

