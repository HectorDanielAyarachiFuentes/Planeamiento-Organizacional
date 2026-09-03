# Let's test the optimized typst layout in a test script first
test_content = """// ==========================================
// CONFIGURACIÓN GENERAL Y TIPOGRAFÍA
// ==========================================
#set document(
  title: "Avance 2: Modelo de Gestión, Gobernanza y Poligobernanza Institucional - CURZAS", 
  author: "Héctor Daniel Ayarachi Fuentes"
)
#set text(font: "Segoe UI", size: 9.2pt, fill: rgb("#24292f"), lang: "es")
#set par(justify: true, leading: 0.65em)

// Paleta de Colores Institucional
#let primary = rgb("#0f2d59")       // Azul marino institucional profundo
#let accent = rgb("#c89632")        // Dorado elegante
#let text-main = rgb("#1f2937")     // Gris carbón para lectura descansada
#let text-muted = rgb("#6b7280")    // Gris suave para subtítulos y metadatos
#let bg-card = rgb("#f8fafc")       // Fondo neutro premium
#let border-subtle = rgb("#e2e8f0") // Bordes sutiles

// Componente: Fila de Metadatos con Separador Horizontal
#let meta-row(label, value) = [
  #grid(
    columns: (135pt, 1fr),
    align: (left + horizon, left + horizon),
    text(size: 9pt, weight: "bold", fill: primary)[#label],
    text(size: 9pt, fill: rgb("#323232"))[#value]
  )
  #v(2pt)
  #line(length: 100%, stroke: 0.4pt + border-subtle)
  #v(2pt)
]

// Componente: Caja Destacada (Callout)
#let callout(title, body) = [
  #v(4pt)
  #block(
    width: 100%,
    fill: bg-card,
    stroke: (left: 3.5pt + primary, rest: 0.5pt + border-subtle),
    inset: (x: 11pt, y: 8pt),
    radius: (right: 4pt),
    [
      #text(weight: "bold", fill: primary, size: 8.2pt, tracking: 0.08em)[#upper(title)] \
      #v(2.5pt)
      #text(size: 8.8pt, fill: text-main)[#body]
    ]
  )
  #v(4pt)
]

// Estilos de Títulos con Protección Anti-Huérfanos
#show heading: set block(keep-with-next: true)

#show heading.where(level: 1): it => block(keep-with-next: true)[
  #v(11pt)
  #box(rect(width: 3.5pt, height: 10.5pt, fill: accent, radius: 1pt))
  #h(5pt)
  #text(weight: "bold", size: 11.5pt, fill: primary)[#it.body]
  #v(4pt)
]

#show heading.where(level: 2): it => block(keep-with-next: true)[
  #v(8pt)
  #text(weight: "bold", size: 9.8pt, fill: primary)[#it.body]
  #v(3pt)
]

// ==========================================
// 1. PORTADA ESTÉTICA CON LOGOTIPO DESTACADO
// ==========================================
#page(
  paper: "a4",
  margin: (x: 2.2cm, top: 2.2cm, bottom: 1.8cm),
  header: none,
  footer: none
)[
  // Encabezado con Logotipo Destacado
  #grid(
    columns: (1fr, auto),
    gutter: 16pt,
    align: (left + horizon, right + horizon),
    [
      #text(size: 13pt, weight: "bold", fill: primary, tracking: 0.04em)[UNIVERSIDAD NACIONAL DEL COMAHUE] \
      #v(4pt)
      #text(size: 10pt, weight: "semibold", fill: accent)[COMPLEJO UNIVERSITARIO REGIONAL ZONA ATLÁNTICA Y SUR (CURZAS)]
    ],
    image("/assets/img/CURZAS.png", height: 60pt)
  )
  
  #v(6pt)
  #line(length: 100%, stroke: 0.8pt + primary)
  #v(14pt)
  
  // Bloque de Título con Barra Lateral
  #block(
    stroke: (left: 3.5pt + primary),
    inset: (left: 14pt, y: 4pt),
    [
      #text(size: 8.8pt, style: "italic", fill: rgb("#646464"))[PLANEAMIENTO Y CONTROL DE LAS ORGANIZACIONES] \
      #v(4pt)
      #text(size: 18pt, weight: "bold", fill: primary, hyphenate: false)[
        Avance 2: Modelo de Gestión, Gobernanza y Poligobernanza
      ] \
      #v(4pt)
      #text(size: 11pt, fill: rgb("#285082"), weight: "regular")[
        Análisis Organizacional Integral del CURZAS (UNCo) frente a los Desafíos del Estado Plataforma, Redes Ad Hoc y Co-Gobierno
      ]
    ]
  )
  
  #v(18pt)
  
  // Tabla de Metadatos con Separadores Horizontales
  #meta-row("Alumno:", "Héctor Daniel Ayarachi Fuentes")
  #meta-row("Equipo Docente:", "Mgter. Susana Lopez — Lic. Carlos Jauge")
  #meta-row("Carrera:", "Licenciatura en Recursos Humanos")
  #meta-row("Institución:", "Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)")
  #meta-row("Sede Académica:", "Viedma, Provincia de Río Negro")
  #meta-row("Marco Teórico:", "Cao & Blutman, Aguilar Villanueva, Abal Medina, Oszlak")
  #meta-row("Año Académico:", "2026")
  
  #align(bottom + center)[
    #text(size: 8.8pt, fill: rgb("#969696"))[Viedma, Río Negro — República Argentina]
  ]
]

// ==========================================
// 2. CUERPO DEL INFORME (PIE CON LOGO NÍTIDO)
// ==========================================
#counter(page).update(1)

#set page(
  paper: "a4",
  margin: (x: 2.2cm, top: 2.3cm, bottom: 2.4cm),
  header: [
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      text(size: 8pt, fill: text-muted)[Avance 2: Modelo de Gestión, Gobernanza y Poligobernanza | CURZAS],
      text(size: 8pt, fill: primary, weight: "bold")[UNCo — CURZAS]
    )
    #v(2pt)
    #line(length: 100%, stroke: 0.4pt + border-subtle)
  ],
  footer: [
    #line(length: 100%, stroke: 0.3pt + border-subtle)
    #v(2pt)
    #grid(
      columns: (1fr, auto, 1fr),
      align: (left + horizon, center + horizon, right + horizon),
      text(size: 8pt, fill: text-muted)[Planeamiento y Control de las Organizaciones],
      image("/assets/img/CURZAS.png", height: 18pt),
      text(size: 8pt, fill: text-muted)[
        #context [Página #counter(page).display("1") de #counter(page).final().at(0)]
      ]
    )
  ]
)

= 1. Identificación y Marco Institucional de la Organización

El objeto de estudio del presente trabajo es el *Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)*, unidad académica y territorial dependiente de la Universidad Nacional del Comahue (UNCo), asentada en la ciudad de Viedma, Provincia de Río Negro. Su estatus institucional responde al principio de *autonomía y autarquía universitaria* consagrado en el Artículo 75 inciso 19 de la Constitución Nacional Argentina y reglamentado por la Ley de Educación Superior N° 24.521.

Su marco operativo se encuentra formalizado por el *Estatuto de la Universidad Nacional del Comahue* (Ordenanza N° 470/1993 y modificatorias), que establece los órganos colegiados co-gobernados de decisión y las misiones fundamentales indisolubles de docencia, investigación y extensión universitaria.

#callout("Misión y Funciones Estratégicas Territoriales")[
  El CURZAS tiene por misión la generación, transferencia y democratización del conocimiento científico, técnico y humanístico en el territorio de la Patagonia Norte y la Línea Sur rionegrina. Su estructura organizativa combina departamentos docentes, secretarías de gestión (Académica, de Investigación y Posgrado, de Extensión Universitaria, y de Gestión Administrativa) y órganos de gobierno colegiados.
]

= 2. Modelo de Administración Predominante y Ajuste Conceptual

Para analizar el modelo de gestión del CURZAS, se coteja su dinámica real con las tipologías analizadas por Cao y Blutman (2019, 2022) y Abal Medina (2014). A partir de la revisión conceptual del avance inicial, se profundiza la distinción epistemológica entre el mandato histórico de autonomía y las técnicas gerenciales.

== A. Ajuste Conceptual: Frontera Teórica entre Autonomía/Autarquía y Nueva Gestión Pública (NGP)

Resulta imprescindible clarificar que la *autonomía académica y la autarquía económico-financiera* del CURZAS/UNCo responden a una conquista histórica originada en la *Reforma Universitaria de 1918*, consolidada constitucionalmente en 1994 como resguardo de autogobierno democrático frente a las injerencias del poder central. Por ende, *no constituyen un derivado de las reformas gerenciales de la Nueva Gestión Pública (NGP)* de los años 90.

#callout("Distinción Teórica: Autonomía Democrática vs. Descentralización Gerencial NGP")[
  - *La Descentralización de la NGP:* Busca fragmentar las estructuras públicas en agencias autónomas o centros de costos para introducir mecanismos de mercado, cuasi-mercados, competencia interinstitucional por recursos, contratos individuales de rendimiento mercantil y arancelamiento o financiamiento ligado a "vouchers" o tasas de egreso.
  - *La Autonomía del CURZAS:* Constituye un *mecanismo institucional de resguardo democrático*, deliberación plural y co-gobierno claustral, donde la asignación presupuestaria se debate en cuerpos representativos orientados al bien público social, no a la rentabilidad comercial.
]

== B. Rasgos del Modelo Burocrático Tradicional (Weberiano) — PREDOMINANTE

La matriz estructural dominante del CURZAS se asienta con nitidez en el *Modelo Burocrático Tradicional Weberiano*:

- *Estructura Jerárquico-Estatutaria:* La pirámide de autoridad está fijada en el Estatuto (Asamblea Universitaria $arrow$ Consejo Superior / Decanato $arrow$ Consejo Directivo $arrow$ Secretarías $arrow$ Departamentos).
- *Principio de Legalidad y Formalismo Procedimental:* Los actos administrativos se articulan rígidamente mediante expedientes formalizados, resoluciones fundadas, ordenanzas y dictámenes jurídicos vinculantes.
- *Carrera Administrativa y Estabilidad Paritaria:* Rige un sistema estricto de ingreso y promoción mediante concursos públicos de antecedentes y oposición, garantizado por Convenios Colectivos de Trabajo regulados por ley (Decreto 366/06 para Nodocentes y Decreto 1246/15 para Docentes), garantizando estabilidad laboral, carrera e imparcialidad técnica.

== C. Rasgos Instrumentales de Modernización e Hibridación Tecnológica

Las manifestaciones de la NGP en el CURZAS no alteran su lógica política ni presupuestaria, sino que operan a nivel *instrumental y procedimental*:
- *Digitalización orientada al usuario:* Autogestión de trámites por parte de los estudiantes mediante módulos de autoservicio (ecosistema SIU-Guaraní y portales web).
- *Gestión documental electrónica:* Trazabilidad de procesos administrativos y expedientes digitales a través del sistema SUDOCU, reduciendo tiempos muertos y uso de papel.

#callout("Dictamen Sintético del Modelo")[
  *Conclusión:* El CURZAS se configura como un *Modelo Burocrático-Estatutario Tradicional Fuertemente Institucionalizado*, cimentado en la autonomía democrática reformista, con incorporación de *herramientas tecnológicas instrumentales de modernización procedimental*.
]

#pagebreak()

= 3. Mecanismos de Rendición de Cuentas (Accountability)

Siguiendo la matriz teórica de Guillermo O'Donnell sintetizada por Abal Medina (2014), el control institucional y la rendición de cuentas en el CURZAS se despliega en tres dimensiones complementarias:

#v(2pt)

#table(
  columns: (1.15fr, 2.45fr, 1.8fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.5pt + border-subtle,
  inset: (x: 8pt, y: 6.5pt),
  [#text(fill: white, weight: "bold", size: 8.5pt)[Dimensión de Accountability]],
  [#text(fill: white, weight: "bold", size: 8.5pt)[Mecanismos Institucionales en CURZAS / UNCo]],
  [#text(fill: white, weight: "bold", size: 8.5pt)[Sustento Normativo / Documental]],
  
  [
    *Horizontal* \
    #text(size: 7.5pt, fill: text-muted)[(Controles intra-estatales e inter-órganos)]
  ],
  [
    - Unidad de Auditoría Interna (UAI) de la UNCo.
    - Control externo de legalidad y gasto por la Auditoría General de la Nación (AGN) y SIGEN.
    - Control de pesos y contrapesos entre el Decanato y el Consejo Directivo (aprobación de balances y designaciones).
  ],
  [
    - Ley 24.156 de Administración Financiera y Sistemas de Control.
    - Informes de auditoría y cuentas de inversión.
    - Resoluciones del Consejo Directivo.
  ],
  
  [
    *Vertical* \
    #text(size: 7.5pt, fill: text-muted)[(Electoral y Representativa)]
  ],
  [
    - Elección directa, periódica y obligatoria de Decano/a y Vicedecano/a.
    - Co-gobierno cuatripartito: renovación democrática de consejeros docentes, nodocentes, graduados y estudiantes.
  ],
  [
    - Estatuto General UNCo (Ordenanza N° 470/93).
    - Cronograma electoral y resoluciones de la Junta Electoral General.
  ],
  
  [
    *Social* \
    #text(size: 7.5pt, fill: text-muted)[(Ciudadanía y Sociedad Civil)]
  ],
  [
    - Portal institucional de Transparencia Activa.
    - Régimen de Acceso a la Información Pública.
    - Publicación abierta de presupuestos, contrataciones, resoluciones y nóminas de autoridades.
  ],
  [
    - Ley Nacional N° 27.275 de Acceso a la Información Pública.
    - Portal Web de Datos Abiertos UNCo.
  ]
)

= 4. La Paradoja del Co-Gobierno frente a la Gobernanza (Aguilar Villanueva y Cao & Blutman)

El análisis de la conducción institucional requiere confrontar los modelos de *Gobernabilidad tradicional* con el paradigma contemporáneo de *Gobernanza* desarrollado por Luis F. Aguilar Villanueva (2006, 2010) y los enfoques de *Poligobernanza* de Horacio Cao y Gustavo Blutman (2019, 2022).

== A. De la Gobernabilidad Unilateral a la Gobernanza en Red
Aguilar Villanueva conceptualiza a la gobernanza no como el simple ejercicio unilateral y jerárquico del poder estatal, sino como un *proceso de co-dirección de la sociedad*, caracterizado por la articulación horizontal, la coordinación multiactoral y la co-producción de políticas públicas entre el Estado, el sector productivo y las organizaciones de la sociedad civil.

== B. Diagnóstico del Co-Gobierno Universitario: ¿Dirección Compartida o Silo Endogámico?
Los cuerpos colegiados del CURZAS (Consejo Directivo local y Consejo Superior de la UNCo) encarnan una experiencia avanzada de "dirección social compartida" dentro del Estado, al integrar en la mesa de decisiones a cuatro claustros: docentes, estudiantes, trabajadores nodocentes y graduados. Sin embargo, al examinar su articulación externa con el entorno territorial, se revela una marcada tensión estructural:

#callout("La Paradoja Institucional: Cogobierno como 'Silo Endogámico'")[
  - *La Fortaleza Democrática Interna:* El co-gobierno garantiza la legitimidad interna, la pluralidad de voces y un balance equilibrado de intereses corporativos y académicos.
  - *El Riesgo de Encapsulamiento Endogámico:* Al no contar con instancias formales de votación o co-decisión destinadas a actores externos (municipios de la Línea Sur, cámaras productivas, sindicatos territoriales, cooperativas de la economía social o comunidades originarias), los órganos colegiados tienden a *encapsularse como silos autorreferenciales*. La agenda del Consejo Directivo se focaliza predominantemente en disputas presupuestarias internas, concursos de cátedras y reglamentaciones académicas, relegando la construcción de una gobernanza horizontal participativa de largo plazo con la comunidad circundante.
]

#pagebreak()

= 5. Escenarios de Poligobernanza y Desafíos Organizacionales en el CURZAS (Cao y Blutman)

El enfoque de *Poligobernanza* planteado por Cao y Blutman (2022) proyecta un Estado flexible, relacional y descentralizado, estructurado a partir de las demandas heterogéneas de la ciudadanía y sustentado en dos pilares: la infraestructura del *Estado Plataforma* y los *tramados institucionales ad hoc*. A continuación se evalúa la operatividad del CURZAS frente a estos dos desafíos:

== A. Primer Desafío: El "Estado Plataforma" frente a la Persistencia de Silos Informacionales

#callout("Pregunta de Análisis")[
  _¿El CURZAS funciona de manera interoperable compartiendo datos integrados con otros organismos públicos e institutos científicos (como el CONICET o el INTA), o persisten los sistemas aislados de información?_
]

- *El Marco Teórico del Estado Plataforma:* Cao y Blutman (2022) y Oszlak (2020) definen al Estado Plataforma como una infraestructura digital integrada basada en estándares comunes, protocolos de intercambio y arquitecturas de APIs abiertas que permiten la interoperabilidad en tiempo real entre múltiples agencias estatales, centros de investigación y la ciudadanía, evitando la duplicación de datos y la fragmentación burocrática.
- *La Realidad Empírica del CURZAS (Islas Tecnológicas):* El análisis organizacional demuestra que en el CURZAS persisten *silos informacionales y sistemas cerrados*. Si bien a nivel interno existe un ecosistema integrado provisto por el Consorcio SIU (SIU-Guaraní para gestión académica, SIU-Mapuche para personal y haberes, SIU-Diaguita para compras, SIU-Pilagá para presupuesto y SUDOCU para expedientes), este opera como un *circuito cerrado intra-universitario*.
- *Déficit de Interoperabilidad Externa:*
  - *Con el Sistema Científico Nacional (CONICET / SIGEVA):* La información académica de los investigadores docentes no se sincroniza automáticamente; los docentes deben duplicar manualmente sus producciones tanto en los repositorios de la UNCo como en la plataforma SIGEVA del CONICET.
  - *Con Organismos Provinciales y Técnicos (INTA, SENASA, IPAP, Ministerios Provinciales):* No existen pasarelas de datos automatizadas ni servicios web interoperables. El intercambio de información técnica o de matrícula se realiza mediante planillas estáticas (archivos Excel), notas formales en papel o correos electrónicos bilaterales, evidenciando que el CURZAS aún se encuentra en la etapa de "islas tecnológicas" distantes del Estado Plataforma.

== B. Segundo Desafío: "Tramados Institucionales Ad Hoc" en Extensión e Investigación Territorial

#callout("Pregunta de Análisis")[
  _¿Las secretarías de Extensión o Investigación configuran redes flexibles y temporales con municipios locales para resolver demandas socio-productivas de urgencia regional, rompiendo la rigidez de los departamentos tradicionales?_
]

- *El Concepto de Tramados Ad Hoc:* Cao y Blutman (2022) describen a las estructuras ad hoc como dispositivos matriciales y temporales orientados a misiones concretas, capaces de conformar redes flexibles interinstitucionales que trascienden los límites rígidos de las jerarquías y departamentos burocráticos tradicionales.
- *Evidencia en el CURZAS (Extensión e Investigación como Articuladores de Red):* En el CURZAS, las *Secretarías de Extensión Universitaria y de Investigación y Posgrado* actúan como los verdaderos vectores de poligobernanza, configurando tramados ad hoc para dar respuesta a demandas críticas de la Patagonia Norte y la Línea Sur:
  - *Proyectos de Extensión y Transferencia Situada:* Se conforman equipos de trabajo multidisciplinarios ad hoc integrados por docentes y estudiantes de distintas carreras (Licenciatura en Administración Pública, Licenciatura en Recursos Humanos, Ciencia Política, Enfermería, Psicopedagogía, Agronomía) que se despliegan en el territorio.
  - *Articulación en Red con Municipios y Actores Productivos:* Estos equipos configuran redes temporales con municipios locales de la Línea Sur (Los Menucos, Maquinchao, Ingeniero Jacobacci, Valcheta, Ramos Mexía) y comisiones de fomento, agencias de extensión del INTA, cooperativas ganaderas lanares y organizaciones campesinas y originarias. Abordan problemas de urgencia productiva (recursos hídricos, gestión municipal, economía popular y salud rural).
- *Tensión Organizacional entre Flexibilidad y Burocracia:* Estos tramados ad hoc logran *romper transitoriamente la rigidez vertical de los departamentos académicos disciplinares*, pero conviven con la fricción de tener que reconducir sus convenios y financiamientos a través de los lentos circuitos formales del Consejo Directivo, reflejando la coexistencia cotidiana entre la innovación en red y el control burocrático tradicional.

#pagebreak()

= 6. Evaluación de Gobernanza Pública Inteligente (Según Oszlak)

Conforme a la perspectiva de Oscar Oszlak (2020) sobre el tránsito desde el Gobierno Electrónico hacia el *Estado Inteligente* y la gobernanza algorítmica, se evaluó la incorporación de tecnologías predictivas e Inteligencia Artificial en la gestión de recursos humanos del CURZAS.

- *Ausencia de Algoritmos Predictivos:* No existen proyectos normativos ni herramientas de software destinadas al perfilamiento algorítmico, monitoreo biométrico automatizado o selección predictiva de aspirantes.
- *Blindaje Paritario y Garantía de Control Humano:* La selección, recategorización y régimen disciplinario del personal docente y nodocente se encuentran estrictamente regulados por los Convenios Colectivos de Trabajo (Decretos 366/06 y 1246/15). Los concursos de oposición y antecedentes exigen tribunales humanos colegiados y veedurías gremiales obligatorias, lo que constituye un dique institucional e ideológico contra la delegación de decisiones en sistemas autónomos de IA.
- *Diagnóstico Evolutivo:* El CURZAS se sitúa en un estadio consolidado de *Digitalización y Gobierno Electrónico*, pero mantiene a la Inteligencia Artificial como un horizonte distante y condicionado por el marco de garantías sociolaborales.

= 7. Matriz Síntesis de Tensiones del Modelo Organizacional

A modo de integración analítica, la siguiente matriz sintetiza las tensiones entre los marcos teóricos estudiados y la realidad institucional del CURZAS:

#v(2pt)

#table(
  columns: (1.2fr, 1.4fr, 1.9fr, 1.8fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.5pt + border-subtle,
  inset: (x: 7pt, y: 5.5pt),
  [#text(fill: white, weight: "bold", size: 8.2pt)[Dimensión]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Paradigma Teórico]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Manifestación Real en CURZAS]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Tensión o Desafío Central]],
  
  [
    *Estructura y Jerarquía*
  ],
  [
    Burocracia Weberiana vs. Flexibilidad Matricial
  ],
  [
    Pirámide estatutaria rígida, departamentos académicos y normativas formalizadas.
  ],
  [
    Lentitud procedimental frente a demandas socio-territoriales urgentes.
  ],
  
  [
    *Autonomía y Gestión*
  ],
  [
    Autarquía Democrática vs. NGP Gerencialista
  ],
  [
    Autonomía política e histórica (Reforma 1918) con herramientas técnicas de NGP (SIU).
  ],
  [
    Preservar el financiamiento público sin caer en la mercantilización por vouchers.
  ],
  
  [
    *Gobierno y Conducción*
  ],
  [
    Co-Gobierno vs. Gobernanza en Red (Aguilar Villanueva)
  ],
  [
    Cuerpos colegiados con representación de cuatro claustros internos.
  ],
  [
    Riesgo de silo endogámico; escasa participación decisoria de actores de la Línea Sur.
  ],
  
  [
    *Sistemas e Información*
  ],
  [
    Islas Tecnológicas vs. Estado Plataforma (Cao y Blutman)
  ],
  [
    Ecosistema SIU/SUDOCU integrado hacia adentro pero desconectado hacia afuera.
  ],
  [
    Ausencia de interoperabilidad automática con CONICET (SIGEVA), INTA y provincia.
  ],
  
  [
    *Articulación Territorial*
  ],
  [
    Tramados Institucionales Ad Hoc (Poligobernanza)
  ],
  [
    Redes flexibles temporales en Extensión e Investigación con municipios y cooperativas.
  ],
  [
    Fricción entre la agilidad del trabajo de campo y los tiempos del trámite burocrático.
  ]
)

= 8. Conclusiones Estratégicas y Prospectiva

El análisis multidimensional del CURZAS confirma que la institución se encuentra atravesada por tres fuerzas concurrentes:
1. Una *sólida columna vertebral burocrático-weberiana* y de autogobierno reformista que garantiza estabilidad, derechos laborales y legitimidad democrática interna.
2. Una *modernización instrumental electrónica* que ha optimizado los trámites y la transparencia interna (SIU, SUDOCU), pero que aún debe evolucionar hacia la interoperabilidad abierta del *Estado Plataforma*.
3. Emergentes dinámicas de *poligobernanza territorial* a través de sus secretarías de Extensión e Investigación, las cuales demuestran que es posible tejer tramados ad hoc flexibles con los municipios y comunidades de la Patagonia Norte, superando los silos disciplinarios y acercando la universidad a los desafíos reales de su territorio.

#v(8pt)

// ==========================================
// 3. CAJA DE FUENTES Y BIBLIOGRAFÍA
// ==========================================

#rect(
  width: 100%,
  fill: bg-card,
  stroke: 0.5pt + border-subtle,
  radius: 5pt,
  inset: (x: 14pt, y: 11pt)
)[
  #text(weight: "bold", size: 10pt, fill: primary)[Bibliografía y Fuentes Consultadas]
  #v(4pt)
  #line(length: 100%, stroke: 0.6pt + accent)
  #v(6pt)
  
  #set text(size: 8.2pt, fill: text-main)
  - *Abal Medina, Juan Manuel (2014).* _Manual de Administración Pública._ Buenos Aires: Ariel. Capítulos 1 y 5.
  - *Aguilar Villanueva, Luis F. (2006).* _Gobernanza y gestión pública._ México D.F.: Fondo de Cultura Económica.
  - *Aguilar Villanueva, Luis F. (2010).* _El futuro de la gestión pública y la gobernanza después de la crisis._ Frontera Norte, 22(43), 187-213.
  - *Cao, Horacio y Blutman, Gustavo (2019).* _Continuidades y rupturas en las ideas sobre reforma y modernización del Estado._ Buenos Aires: INAP / Universidad de Buenos Aires.
  - *Cao, Horacio y Blutman, Gustavo (2022).* _Escenarios futuros para el Estado y la Administración Pública._ Colección, Vol. 34, N° 1, pp. 33-66. Buenos Aires: UCA / INAP.
  - *Cao, Horacio; Blutman, Gustavo; Estévez, Alejandro e Iturburu, Mónica (2022).* _El futuro del empleo público, tecnologías digitales y estructuras estatales._ Buenos Aires: CIAP / UBA.
  - *Oszlak, Oscar (2020).* _El Estado en la era exponencial: Tecnologías disruptivas y gestión pública._ Buenos Aires: Editorial INAP.
  - *Universidad Nacional del Comahue (1993/2023).* _Estatuto de la Universidad Nacional del Comahue._ Neuquén y Viedma: UNCo.
  - *Normativa Nacional:* Constitución Nacional (Art. 75 inc. 19); Ley de Educación Superior N° 24.521; Ley de Administración Financiera N° 24.156; Ley N° 27.275 de Acceso a la Información Pública; Convenios Colectivos Decretos PEN N° 366/06 (Nodocentes) y N° 1246/15 (Docentes).
]
"""

with open("tareas/actividad_01/entregables/avance 2/Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.typ", "w", encoding="utf-8") as f:
    f.write(test_content)

print("Updated typst file")
