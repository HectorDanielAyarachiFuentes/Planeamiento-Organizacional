#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from pathlib import Path

path = Path(r"Actividades/entregables/actividad_03/Avance_3_Estructura_Organigrama_Flujograma_GDE_CURZAS_Hector_Ayarachi.typ")
content = path.read_text(encoding="utf-8")

# 1. Tabla 3.1
target_t31 = """En consecuencia, estos valores *no son taxativos ni deben entenderse como datos reales o comprobados de la institución*, dado que no se ha realizado un trabajo de campo empírico para su medición directa. Su validez empírica requeriría una auditoría institucional futura basada en registros administrativos consolidados. Esta distinción transparenta el alcance del trabajo y permite formular una propuesta de control de gestión y modernización procedimental sin atribuir al CURZAS métricas no verificadas.

#v(2pt)

#table(
  columns: (1.2fr, 2fr, 1.8fr),"""

replace_t31 = """En consecuencia, estos valores *no son taxativos ni deben entenderse como datos reales o comprobados de la institución*, dado que no se ha realizado un trabajo de campo empírico para su medición directa. Su validez empírica requeriría una auditoría institucional futura basada en registros administrativos consolidados. Esta distinción transparenta el alcance del trabajo y permite formular una propuesta de control de gestión y modernización procedimental sin atribuir al CURZAS métricas no verificadas.

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 3.1: Matriz de Deslinde Metodológico: Registro Administrativo vs. Supuestos Analíticos] \\
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia para el encuadre epistemológico y metodológico del diagnóstico.]
]
#v(3pt)

#table(
  columns: (1.2fr, 2fr, 1.8fr),"""

assert target_t31 in content, "target_t31 not found"
content = content.replace(target_t31, replace_t31, 1)

# 2. Trazabilidad Analítica
target_traz = """- El marco jurídico-administrativo de la *organización del Estado y la Administración Pública Nacional* sistematizado por *Norberto Zeller y Darío Impala (2000)*, delimitando las fronteras entre descentralización institucional, autarquía y desconcentración.

== Eje 1: Relevamiento y Análisis del Organigrama y Manual de Funciones"""

replace_traz = """- El marco jurídico-administrativo de la *organización del Estado y la Administración Pública Nacional* sistematizado por *Norberto Zeller y Darío Impala (2000)*, delimitando las fronteras entre descentralización institucional, autarquía y desconcentración.

=== C. Trazabilidad Analítica: Conexión de los Ejes de los Avances 1 y 2 con el Diagnóstico de Procesos y Ecosistema Digital

De cara a la integración metodológica y analítica del informe en un único cuerpo coherente, resulta indispensable garantizar la consistencia en la trazabilidad de los hilos conductores explorados en los Avances 1 y 2, verificando cómo impactan de manera directa en el diagnóstico de la microestructura, los circuitos de personal y la transición al ecosistema digital (SUDOCU / SIU-Mapuche):

1. *La Tensión entre la Autonomía Universitaria y los Sistemas Centrales de Gestión:*
  En el Avance 1 se fundamentó que la autonomía universitaria consagrada en el Artículo 75 inciso 19 de la Constitución Nacional constituye un principio político de autogobierno democrático y pluralismo, diametralmente opuesto a la descentralización gerencial de la Nueva Gestión Pública (Cao & Blutman, 2019). Esta distinción conceptual se proyecta de manera determinante sobre el diseño de procesos y la soberanía tecnológica: mientras que los ministerios y organismos dependientes del Poder Ejecutivo Nacional fueron forzados a implementar el sistema verticalista GDE (Gestión Documental Electrónica, Decreto PEN N° 1063/2016), el sistema universitario nacional nucleado en el Consejo Interuniversitario Nacional (CIN) defendió su autonomía funcional desarrollando e implementando el sistema *SUDOCU* (Sistema Único de Documentación de las Universidades).
  SUDOCU fue diseñado específicamente para respetar los procedimientos colegiados, las firmas de autoridades electas y la validez legal interna de las resoluciones de Consejos Directivos y Superior. Sin embargo, en el diagnóstico operativo del CURZAS se advierte la contrapartida de esta conquista autonómica: al interactuar con el ecosistema de la Administración Pública Nacional o provincial (ANSES, ARCA/AFIP, Ministerios de Salud y Educación provinciales) que opera en otros estándares, surge una barrera de interoperabilidad externa que no puede subsanarse mediante directivas unilaterales, obligando al personal de Recursos Humanos a gestionar duplicaciones documentales y revalidaciones periciales en soporte papel.

2. *La Poligobernanza Territorial de los Nodos frente a la Centralidad del Circuito Administrativo:*
  El Avance 2 evidenció que el CURZAS no puede comprenderse como un edificio cerrado en la capital rionegrina, sino como una *red de poligobernanza reticular integrada por 10 Nodos Regionales* distribuidos a lo largo de la vasta estepa de la Línea Sur (Jacobacci, Maquinchao, Los Menucos, Sierra Colorada, Ramos Mexía, Valcheta) y la Costa Atlántica (San Antonio Oeste, Sierra Grande, Conesa) (Aguilar Villanueva, 2006).
  No obstante, al analizar el circuito formal de licencias médicas y extraordinarias en el Eje 3, queda al descubierto una profunda contradicción estructural: el procedimiento histórico fue modelado bajo el supuesto de proximidad física a la ventanilla de Viedma (entrega del certificado médico original con firma ológrafa en 48 a 72 horas). Para un docente o nodocente que cumple funciones en Los Menucos (a 400 kilómetros de Viedma) o en San Antonio Oeste (a casi 200 kilómetros), esta exigencia analógica impone una penalización logística gravosa, con riesgo constante de cómputo erróneo de "inasistencias injustificadas". En consecuencia, la plena digitalización a través de *SUDOCU* y la descentralización de la carga en *SIU-Mapuche* no son meras preferencias de modernización informática, sino los dispositivos técnicos e institucionales imprescindibles para hacer viable la *poligobernanza territorial*, transformando los nodos en terminales autogestivas de derechos y superando el aislamiento geográfico.

3. *El Rol de los Trabajadores (Docentes y Nodocentes) como Actores Estratégicos del Cambio:*
  Recuperando el enfoque de la Planificación Estratégica Situacional (PES) de Carlos Matus y la sociología de las organizaciones de Michel Crozier desarrollados en el Avance 2, los trabajadores universitarios no constituyen engranajes mecánicos o usuarios pasivos de la informática, sino *actores estratégicos dotados de cuotas reales de poder, intereses gremiales y capacidad de resistencia o veto*. El marco laboral del CURZAS se encuentra blindado por el Convenio Colectivo de Trabajo Nodocente (Decreto N° 366/2006) y el Docente (Decreto N° 1246/2015), otorgando a los sindicatos (APUNC y ADUNC) injerencia formal en las Comisiones Paritarias Particulares (COPAR).
  En el día a día del circuito de personal, ante la falla de integración informática directa entre SUDOCU y SIU-Mapuche, son los propios trabajadores nodocentes del Área de Personal quienes actúan como *"puentes humanos"* indispensables: leen las resoluciones en pantalla, interpretan las fechas y transcriben manualmente cada novedad al liquidador de haberes antes del cierre mensual de Rectorado. Esta mediación humana previene descuentos injustos en los haberes de sus compañeros, encarnando con precisión la *"política de salir del paso"* (*muddling through*) teorizada por John Forester (1984). Por tanto, cualquier propuesta de reingeniería procedimental que ignore la dimensión estratégica del factor humano o prescinda de la negociación paritaria estará condenada a la inercia estructural y al fracaso operativo.

== Eje 1: Relevamiento y Análisis del Organigrama y Manual de Funciones"""

assert target_traz in content, "target_traz not found"
content = content.replace(target_traz, replace_traz, 1)

# 3. Tabla 3.2
target_t32 = """  - *Dirección de Mantenimiento, Obras y Servicios Generales*.

#v(3pt)

#table(
  columns: (1.2fr, 2.2fr, 1.6fr),"""

replace_t32 = """  - *Dirección de Mantenimiento, Obras y Servicios Generales*.

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 3.2: Estructura Orgánica Formal y Misiones Estatutarias del CURZAS (Ordenanza N° 470/1993)] \\
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia sobre la base del Estatuto General de la UNCo y ordenanzas complementarias.]
]
#v(3pt)

#table(
  columns: (1.2fr, 2.2fr, 1.6fr),"""

assert target_t32 in content, "target_t32 not found"
content = content.replace(target_t32, replace_t32, 1)

# 4. Figura 3.1
target_f31 = """*Figura 1:* Organigrama Funcional y Estructural del CURZAS — UNCo: Dependencias Formales (De Jure) vs. Red Territorial Emergente de 10 Nodos Regionales (De Facto) y Área Crítica de Personal."""
replace_f31 = """*Figura 3.1:* Organigrama Funcional y Estructural del CURZAS — UNCo (Estructura Formal De Jure vs. Red Territorial Emergente De Facto de 10 Nodos Regionales y Área Crítica de Personal)."""
assert target_f31 in content, "target_f31 not found"
content = content.replace(target_f31, replace_f31, 1)

# 5. Tabla 3.3
target_t33 = """Para abordar la geometría de poder y decisión en el CURZAS, se aplica la distinción entre *centralización, desconcentración y descentralización* formulada por *Zeller e Impala (2000)* e integrada con la teoría de los *ámbitos organizativos (AO)* de *Jorge Hintze (2001)*.

#v(3pt)

#table(
  columns: (1.1fr, 2.3fr, 1.6fr),"""

replace_t33 = """Para abordar la geometría de poder y decisión en el CURZAS, se aplica la distinción entre *centralización, desconcentración y descentralización* formulada por *Zeller e Impala (2000)* e integrada con la teoría de los *ámbitos organizativos (AO)* de *Jorge Hintze (2001)*.

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 3.3: Geometría Decisional: Centralización, Desconcentración y Redes Territoriales] \\
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia a partir de Zeller e Impala (2000) e integración con la teoría de Ámbitos Organizativos de Hintze (2001).]
]
#v(3pt)

#table(
  columns: (1.1fr, 2.3fr, 1.6fr),"""

assert target_t33 in content, "target_t33 not found"
content = content.replace(target_t33, replace_t33, 1)

# 6. Figura 3.2
target_f32 = """*Figura 1:* Mapeo estructurado por carriles (*swimlanes*) del circuito de licencias en el CURZAS (UNCo)."""
replace_f32 = """*Figura 3.2:* Mapeo Estructurado por Carriles (*swimlanes*) del Circuito de Tramitación de Licencias Médicas en el CURZAS (UNCo)."""
assert target_f32 in content, "target_f32 not found"
content = content.replace(target_f32, replace_f32, 1)

# 7. Tabla 3.4
target_t34 = """=== C. Matriz Operativa de Etapas, Insumos y Responsables

#table(
  columns: (45pt, 85pt, 110pt, 100pt, 75pt),"""

replace_t34 = """=== C. Matriz Operativa de Etapas, Insumos y Responsables

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 3.4: Matriz Operativa del Circuito de Tramitación de Licencias Médicas (SUDOCU / SIU-Mapuche)] \\
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia en base a la modelación procedimental en el CURZAS.]
]
#v(3pt)

#table(
  columns: (45pt, 85pt, 110pt, 100pt, 75pt),"""

assert target_t34 in content, "target_t34 not found"
content = content.replace(target_t34, replace_t34, 1)

# 8. Tabla 3.5
target_t35 = """A partir del análisis formal del procedimiento y de la contrastación con dinámicas burocráticas típicas observadas en ámbitos públicos y privados, se plantean como hipótesis analíticas exploratorias *cuatro cuellos de botella críticos* que podrían ralentizar la gestión administrativa:

#v(2pt)

#table(
  columns: (1.2fr, 2.2fr, 1.6fr),"""

replace_t35 = """A partir del análisis formal del procedimiento y de la contrastación con dinámicas burocráticas típicas observadas en ámbitos públicos y privados, se plantean como hipótesis analíticas exploratorias *cuatro cuellos de botella críticos* que podrían ralentizar la gestión administrativa:

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 3.5: Diagnóstico Exploratorio de Cuellos de Botella en la Transición al Ecosistema Digital] \\
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración analítica a partir del modelado del circuito de licencias y patrones de la administración pública.]
]
#v(3pt)

#table(
  columns: (1.2fr, 2.2fr, 1.6fr),"""

assert target_t35 in content, "target_t35 not found"
content = content.replace(target_t35, replace_t35, 1)

# 9. Tabla 3.6
target_t36 = """Aplicando el marco metodológico del *INAP (1997)* (basado en el modelo de análisis multidimensional de organizaciones públicas y los aportes de Aldo Schlemenson), la problemática del Área de Personal del CURZAS se desagrega en sus dimensiones constitutivas:

#v(2pt)

#table(
  columns: (95pt, 1.6fr, 1.4fr),"""

replace_t36 = """Aplicando el marco metodológico del *INAP (1997)* (basado en el modelo de análisis multidimensional de organizaciones públicas y los aportes de Aldo Schlemenson), la problemática del Área de Personal del CURZAS se desagrega en sus dimensiones constitutivas:

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 3.6: Análisis Multidimensional de la Problemática Organizacional (INAP / Schlemenson)] \\
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia en base a Dirección Nacional de Estudios e Investigaciones (INAP, 1997) y Schlemenson.]
]
#v(3pt)

#table(
  columns: (95pt, 1.6fr, 1.4fr),"""

assert target_t36 in content, "target_t36 not found"
content = content.replace(target_t36, replace_t36, 1)

# 10. Tabla 3.7
target_t37 = """Para estructurar la futura evaluación empírica del procedimiento, se presenta la siguiente matriz dividida en indicadores propuestos, supuestos de referencia iniciales y métodos de verificación para la construcción de una línea de base comprobada:

#v(2pt)

#table(
  columns: (90pt, 1.25fr, 75pt, 1.25fr, 72pt),"""

replace_t37 = """Para estructurar la futura evaluación empírica del procedimiento, se presenta la siguiente matriz dividida en indicadores propuestos, supuestos de referencia iniciales y métodos de verificación para la construcción de una línea de base comprobada:

#v(3pt)

#align(left)[
  #text(weight: "bold", fill: primary, size: 8.8pt)[Tabla 3.7: Matriz Integral de Indicadores de Gestión para el Rediseño del Procedimiento] \\
  #text(size: 7.5pt, fill: text-muted, style: "italic")[Fuente: Elaboración propia: supuestos iniciales de referencia y métodos de auditoría para línea de base.]
]
#v(3pt)

#table(
  columns: (90pt, 1.25fr, 75pt, 1.25fr, 72pt),"""

assert target_t37 in content, "target_t37 not found"
content = content.replace(target_t37, replace_t37, 1)

path.write_text(content, encoding="utf-8")
print("✅ Standalone Actividad 3 actualizado con éxito!")

