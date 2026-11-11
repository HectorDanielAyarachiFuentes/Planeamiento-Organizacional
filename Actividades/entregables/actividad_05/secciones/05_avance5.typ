#import "/Actividades/entregables/actividad_02/modulos/config/estilos.typ": *
#import "/Actividades/entregables/actividad_02/modulos/components/cajas.typ": *

// ==============================================================================
// SECCIÓN: AVANCE 5 — SISTEMAS DE CONTROL, TABLERO DE COMANDO Y EVALUACIÓN
// UNIDAD V — VERSIÓN PRECISA Y CONCISA CENTRADA EN LA CONSIGNA
// ==============================================================================

#avance-banner(
  "AVANCE 5: Sistemas de Control, Tablero de Comando y Evaluación",
  "Medición del Desempeño, Auditoría y Transparencia en el CURZAS — UNCo (Unidad V)"
)

La evaluación y el control constituyen el cierre del ciclo de planeamiento institucional. Siguiendo a *Martínez Nogueira (2016)* y *Feinstein (2016)*, evaluar en el sector público excede la verificación formal de legalidad: implica contrastar intenciones con consecuencias reales para alimentar el aprendizaje organizacional y la rendición de cuentas. En un organismo donde el Inciso 1 absorbe el 90,2% del presupuesto y conviven la autonomía universitaria (Art. 75 inc. 19 CN), la poligobernanza en 10 nodos territoriales y la transición digital (SUDOCU/SIU-Mapuche), la medición mediante tableros e indicadores (*Ramírez, 2023*) y el *análisis de contribución* (*Mayne, 2016*) resultan indispensables para evaluar la eficiencia del factor humano.

== 1. Organismos de Control Externo e Interno y Auditoría sobre Personal

#callout-pregunta[
  ¿Qué organismos auditan externa e internamente al organismo? ¿Cuándo fue la última auditoría formal realizada al organismo y qué observaciones se le formularon al área de personal?
]

En el marco de la *Ley N° 24.156* de Administración Financiera, la *Ley de Educación Superior N° 24.521* (Art. 59 bis) y el *Estatuto de la UNCo* (Ord. N° 470/93 y modif.), el CURZAS —como unidad académica de la Entidad/SAF 809 UNCo— se encuentra sujeto a un esquema mixto de fiscalización externa, interna y académica:

#v(2pt)
#align(left)[
  #text(weight: "bold", fill: primary, size: 8.6pt)[Tabla 5.1: Ecosistema de Organismos de Control Externo e Interno en el CURZAS / UNCo] \
  #text(size: 7.4pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia en base a Ley 24.156, Ley 24.521, Estatuto UNCo, SIGEN (2025) y registros públicos AGN/UNCo.]
]
#v(2pt)

#table(
  columns: (72pt, 98pt, 105pt, 1.5fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.45pt + border-subtle,
  align: left + top,
  inset: (x: 6.5pt, y: 5pt),
  table.header(
    text(fill: white, weight: "bold", size: 7.8pt)[Tipo de Control],
    text(fill: white, weight: "bold", size: 7.8pt)[Organismo Auditor],
    text(fill: white, weight: "bold", size: 7.8pt)[Dependencia y Norma],
    text(fill: white, weight: "bold", size: 7.8pt)[Alcance y Particularidad en el CURZAS / UNCo]
  ),
  [*Control Externo*],
  [*Auditoría General de la Nación (AGN)*],
  [Congreso de la Nación (Art. 85 CN, Ley 24.156, Art. 59 bis LES).],
  [Control posterior externo de estados contables, Cuenta de Inversión (SAF 809), transferencias del Tesoro (Fuente 11) y convenios específicos. Es el órgano externo reconocido por el CIN en resguardo de la autonomía.],
  [*Control Interno Propio*],
  [*Unidad de Auditoría Interna (UAI — UNCo)*],
  [Consejo Superior / Estatuto UNCo (Titular: Cr. Oscar Rebolledo).],
  [La UNCo es pionera al otorgar *rango estatutario* a su UAI, blindando su independencia funcional respecto del Rectorado de turno. Audita legalidad, riesgo, circuitos administrativos y haberes en todas las sedes, incluido el CURZAS.],
  [*Órgano Rector de Control Interno*],
  [*Sindicatura General de la Nación (SIGEN)*],
  [Poder Ejecutivo Nacional (*Normas SIGEN 2025*, Ley 24.156).],
  [Fija pautas técnicas de auditoría basada en riesgos (Principios 7, 8 y 12). Su competencia directa sobre universidades generó tensión jurídica con la autonomía: restringida en 2022 por dictamen de la PTN y rehabilitada por dictamen PTN a fines de 2024.],
  [*Evaluación de Calidad*],
  [*CONEAU*],
  [Art. 44 Ley N° 24.521 (cada 6 años).],
  [Evaluación institucional externa sobre docencia, investigación, extensión y planta académica en Viedma y nodos regionales.]
)
#v(4pt)

*Última Auditoría Formal y Observaciones al Área de Personal:*
- *Periodicidad y registro oficial:* Según registros institucionales de la UNCo y del buscador oficial de la AGN, las revisiones externas integrales recientes de la *AGN* sobre la universidad se ubican en torno al ejercicio *2021* (junto con el seguimiento anual del SAF 809 en la Cuenta de Inversión y exámenes especiales), complementadas de forma continua por los planes anuales de la *UAI estatutaria de la UNCo*. A partir de fines de 2024, la *SIGEN* reactivó su esquema de fiscalización sobre universidades nacionales poniendo foco prioritario en el gasto en personal y rendiciones.
- *Foco y observaciones en Recursos Humanos:* Dado que la masa salarial absorbe entre el *90,2% y el 95%* de los recursos universitarios, las auditorías internas (UAI / *SIGEN 2025*) sobre el Área de Personal se concentran en: *(a)* trazabilidad entre los actos administrativos de altas, bajas y licencias (en transición de papel a *SUDOCU*) y la liquidación mensual en *SIU-Mapuche*; *(b)* control de legajos, topes horarios e incompatibilidades docentes; y *(c)* correcta aplicación del *CCT 366/06*, *CCT 1246/15* y el adicional legal del 40% por Zona Desfavorable Patagónica. *Precisiones metodológicas:* En los repositorios abiertos de la AGN no constan informes individuales desagregados exclusivamente para la oficina de personal de la sede CURZAS Viedma, canalizándose los hallazgos operativos a nivel central de la Entidad 809 UNCo.

== 2. Evaluación Laboral Vigente y Tablero de Control Preliminar de RR. HH.

#callout-pregunta[
  ¿Qué metas cuantitativas o indicadores clave de desempeño (KPIs) utiliza formalmente la institución para evaluar el rendimiento laboral? Diseño de un Tablero de Control preliminar con al menos 3 KPIs específicos para medir la eficiencia de los recursos humanos.
]

*Diagnóstico de los Mecanismos Formales de Evaluación Vigentes:*
1. *Estamento Nodocente (CCT Decreto N° 366/06, Título IX):* El convenio prevé evaluaciones anuales de desempeño basadas en conocimiento del puesto, puntualidad, trabajo en equipo y capacitación. No obstante, las actas paritarias particulares entre la *UNCo y APUNC* evidencian un *diferimiento histórico* en la aplicación sistemática de dicha calificación ordinaria, suplido mediante mecanismos compensatorios y promociones paritarias por antigüedad.
2. *Estamento Docente (CCT Decreto N° 1246/15 y Estatuto UNCo):* Se evalúa mediante concursos públicos, reválidas periódicas, informes académicos anuales, categorización de investigación (SIGEVA) y encuestas estudiantiles de cátedra registradas en *SIU-Guaraní*.
3. *Brecha de Medición Estratégica:* Tal como advierte *Telma Ramírez (2023)*, el CURZAS opera principalmente con *registros administrativos de insumo y cumplimiento formal* (cantidad de cargos en *SIU-Mapuche* y Anuarios Estadísticos), careciendo de un *Tablero de Comando* con metas cuantitativas e indicadores de eficiencia, calidad y contribución (*Mayne, 2016*) vinculados al desempeño real del factor humano.

*Diseño de Tablero de Control Preliminar de Eficiencia en RR. HH. (CURZAS — UNCo):*
Siguiendo los criterios de pertinencia, validez y economía informativa de *Ramírez (2023)* y la ficha técnica de la *Guía Metodológica de Indicadores (PI-2027)*, se propone un tablero inicial con **4 KPIs** articulados a la matriz insumo-proceso-producto (*Avance 4*) y al ecosistema digital (*Avance 3*):

#v(2pt)
#align(left)[
  #text(weight: "bold", fill: primary, size: 8.6pt)[Tabla 5.2: Tablero de Control Preliminar de Eficiencia en Recursos Humanos — CURZAS (UNCo)] \
  #text(size: 7.4pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia en base a Ramírez (2023), Mayne (2016) y Guía Metodológica para Diseño de Indicadores (PI-2027).]
]
#v(2pt)

#table(
  columns: (62pt, 96pt, 128pt, 68pt, 95pt),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.45pt + border-subtle,
  align: left + top,
  inset: (x: 6pt, y: 5pt),
  table.header(
    text(fill: white, weight: "bold", size: 7.6pt)[Código / Tipo],
    text(fill: white, weight: "bold", size: 7.6pt)[Indicador (KPI)],
    text(fill: white, weight: "bold", size: 7.6pt)[Fórmula de Cálculo],
    text(fill: white, weight: "bold", size: 7.6pt)[Base → Meta],
    text(fill: white, weight: "bold", size: 7.6pt)[Frecuencia y Fuente]
  ),
  [*KPI-1* \ #text(size: 7pt, fill: text-muted)[Eficiencia de Procesos]],
  [*Tiempo Medio de Tramitación de Novedades de Personal*],
  [(Sumatoria de días hábiles desde alta/licencia en *SUDOCU* hasta impacto en *SIU-Mapuche*) / Total trámites],
  [Base: \~12 días \ *Meta: ≤ 5 días hábiles*],
  [Mensual \ Logs SUDOCU y SIU-Mapuche],
  [*KPI-2* \ #text(size: 7pt, fill: text-muted)[Calidad y Control Interno]],
  [*Tasa de Liquidaciones Sin Observaciones ni Ajustes*],
  [(Liquidaciones mensuales sin rectificativas ni errores de carga / Total liquidaciones emitidas) × 100],
  [Base: \~94,0% \ *Meta: ≥ 99,0%*],
  [Mensual \ Reportes Área Personal / UAI UNCo],
  [*KPI-3* \ #text(size: 7pt, fill: text-muted)[Eficiencia y Capacitación]],
  [*Cobertura de Capacitación Digital del Personal (SUDOCU / SIU)*],
  [(Agentes nodocentes y de nodos certificados en herramientas digitales / Planta activa total) × 100],
  [Base: \~45,0% \ *Meta: ≥ 90,0% anual*],
  [Semestral \ Registros Capacitación / CCT 366/06],
  [*KPI-4* \ #text(size: 7pt, fill: text-muted)[Contribución Territorial]],
  [*Índice de Continuidad Docente en Nodos Regionales*],
  [(Comisiones y tutorías efectivamente sostenidas en los 10 nodos / Comisiones programadas) × 100],
  [Base: \~82,0% \ *Meta: ≥ 95,0%*],
  [Cuatrimestral \ SIU-Guaraní y Coord. Nodos]
)
#v(2pt)
#text(size: 7pt, fill: text-muted, style: "italic")[
  \* Nota: Las líneas base (\~) representan estimaciones diagnósticas preliminares (Avances 2 y 3) para parametrizar la medición inicial del tablero.
]
#v(3pt)

#callout-dictamen("Dictamen Final de Control y Evaluación (Unidad V)")[
  *Síntesis:* El CURZAS posee una sólida arquitectura de legalidad —respaldada por una *UAI con rango estatutario* única en el país y el control externo de la *AGN*—, pero exhibe un déficit de *evaluación pragmática de gestión* (*Feinstein, 2016*). Implementar el Tablero de Comando propuesto permite cerrar la brecha entre la planificación política (*Avance 2*), los procesos digitales (*Avance 3*) y la rigidez presupuestaria del Inciso 1 (*Avance 4*), transformando el control burocrático en aprendizaje institucional continuo al servicio de la comunidad patagónica.
]
