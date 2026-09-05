// ==============================================================================
// CONFIGURACIÓN GENERAL Y TIPOGRAFÍA INSTITUCIONAL
// ==============================================================================
#set document(
  title: "Informe Integral de Planeamiento Organizacional - CURZAS (UNCo)",
  author: "Héctor Daniel Ayarachi Fuentes"
)
#set text(font: "Segoe UI", size: 9.2pt, fill: rgb("#24292f"), lang: "es")
#set par(justify: true, leading: 0.65em)

// Paleta de Colores Institucional
#let primary = rgb("#0f2d59")       // Azul marino institucional profundo
#let accent = rgb("#c89632")        // Dorado elegante / Acento
#let text-main = rgb("#1f2937")     // Gris carbón para lectura descansada
#let text-muted = rgb("#6b7280")    // Gris suave para metadatos y subtítulos
#let bg-card = rgb("#f8fafc")       // Fondo neutro suave
#let border-subtle = rgb("#e2e8f0") // Bordes sutiles

// Componente: Fila de Metadatos con Separador Horizontal
#let meta-row(label, value) = [
  #grid(
    columns: (140pt, 1fr),
    align: (left + horizon, left + horizon),
    text(size: 9pt, weight: "bold", fill: primary)[#label],
    text(size: 9pt, fill: rgb("#323232"))[#value]
  )
  #v(3pt)
  #line(length: 100%, stroke: 0.4pt + border-subtle)
  #v(3pt)
]

// Componente: Banner de Sección / Avance con Integración al Índice
#let avance-banner(titulo, subtitulo) = [
  #v(4pt)
  #heading(level: 1, outlined: true, bookmarked: true)[#titulo]
  #block(
    width: 100%,
    fill: primary,
    inset: (x: 16pt, y: 10pt),
    radius: 4pt,
    [
      #grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        [
          #text(fill: white, weight: "bold", size: 11.5pt, tracking: 0.03em)[#titulo] \
          #if subtitulo != "" [
            #v(2pt)
            #text(fill: rgb("#e2e8f0"), size: 8.5pt, style: "italic")[#subtitulo]
          ]
        ],
        text(fill: accent, size: 9pt, weight: "bold")[UNCo — CURZAS]
      )
    ]
  )
  #v(8pt)
]

// Componente: Caja Destacada (Callout - Indivisible)
#let callout(title, body) = [
  #v(4pt)
  #block(
    width: 100%,
    breakable: false,
    fill: bg-card,
    stroke: (left: 3.5pt + primary, rest: 0.5pt + border-subtle),
    inset: (x: 11pt, y: 7.5pt),
    radius: (right: 4pt),
    [
      #text(weight: "bold", fill: primary, size: 8.2pt, tracking: 0.07em)[#upper(title)] \
      #v(2.5pt)
      #text(size: 8.9pt, fill: text-main)[#body]
    ]
  )
  #v(4pt)
]

// Estilos de Títulos y Jerarquía Visual
#show heading.where(level: 1): it => none // Oculto en el cuerpo porque se despliega en el banner estilizado

#show heading.where(level: 2): it => [
  #v(11pt)
  #box(rect(width: 3.5pt, height: 10.5pt, fill: accent, radius: 1pt))
  #h(5pt)
  #text(weight: "bold", size: 10.5pt, fill: primary)[#it.body]
  #v(4pt)
]

#show heading.where(level: 3): it => [
  #v(7pt)
  #text(weight: "bold", size: 9.3pt, fill: primary)[#it.body]
  #v(3pt)
]

#show heading.where(level: 4): it => [
  #v(5pt)
  #text(weight: "bold", size: 8.8pt, fill: rgb("#174075"))[#it.body]
  #v(2.5pt)
]

#show heading.where(level: 5): it => [
  #v(4pt)
  #text(weight: "bold", size: 8.4pt, fill: rgb("#0f2d59"))[#it.body]
  #v(2pt)
]

// ==============================================================================
// 1. PORTADA INSTITUCIONAL FORMAL (LIMPIA Y SIN ÍNDICE EN PORTADA)
// ==============================================================================
#page(
  paper: "a4",
  margin: (x: 2.3cm, top: 2.4cm, bottom: 2.2cm),
  header: none,
  footer: none
)[
  // Encabezado Institucional con Logotipo Oficial
  #grid(
    columns: (1fr, auto),
    gutter: 16pt,
    align: (left + horizon, right + horizon),
    [
      #text(size: 13pt, weight: "bold", fill: primary, tracking: 0.04em)[UNIVERSIDAD NACIONAL DEL COMAHUE] \
      #v(3pt)
      #text(size: 9.5pt, weight: "semibold", fill: accent)[COMPLEJO UNIVERSITARIO REGIONAL ZONA ATLÁNTICA Y SUR (CURZAS)]
    ],
    image("/assets/img/CURZAS.png", height: 60pt)
  )
  
  #v(6pt)
  #line(length: 100%, stroke: 0.8pt + primary)
  #v(20pt)
  
  // Bloque de Título Principal Integrador
  #block(
    stroke: (left: 3.5pt + primary),
    inset: (left: 14pt, y: 5pt),
    [
      #text(size: 8.5pt, style: "italic", fill: rgb("#646464"), tracking: 0.05em)[CÁTEDRA DE PLANEAMIENTO Y CONTROL DE LAS ORGANIZACIONES] \
      #v(5pt)
      #text(size: 19pt, weight: "bold", fill: primary, hyphenate: false)[
        Informe Integral de Planeamiento y Gestión Organizacional
      ] \
      #v(5pt)
      #text(size: 12pt, fill: rgb("#285082"), weight: "medium")[
        Diagnóstico Institucional, Modelos de Gestión y Poligobernanza en el CURZAS (UNCo)
      ]
    ]
  )
  
  #v(24pt)
  
  // Tabla de Metadatos del Documento
  #meta-row("Estudiante:", "Téc. Sup. en RR. HH. Héctor Daniel Ayarachi Fuentes")
  #meta-row("Equipo Docente:", "Mgter. Susana Lopez — Lic. Carlos Jauge")
  #meta-row("Carrera:", "Licenciatura en Recursos Humanos")
  #meta-row("Institución Analizada:", "Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)")
  #meta-row("Sede Académica:", "Viedma, Provincia de Río Negro")
  #meta-row("Marco Teórico:", "Bertranou, Matus, Cao & Blutman, Aguilar Villanueva, Abal Medina, Oszlak, Hintze")
  #meta-row("Ciclo Lectivo:", "2026")
  
  #align(bottom + center)[
    #text(size: 8.5pt, fill: rgb("#969696"))[Viedma, Río Negro — República Argentina]
  ]
]

// ==============================================================================
// 2. HOJA DEDICADA: ÍNDICE GENERAL DE CONTENIDOS (DESPUÉS DE LA PORTADA)
// ==============================================================================
#counter(page).update(1)

#set page(
  paper: "a4",
  margin: (x: 2.3cm, top: 2.4cm, bottom: 2.4cm),
  header: [
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      text(size: 8pt, fill: text-muted)[Planeamiento y Control de las Organizaciones | CURZAS],
      text(size: 8pt, fill: primary, weight: "bold")[UNCo — CURZAS]
    )
    #v(2pt)
    #line(length: 100%, stroke: 0.4pt + border-subtle)
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

#v(15pt)

#rect(
  width: 100%,
  fill: bg-card,
  stroke: 0.5pt + border-subtle,
  radius: 6pt,
  inset: (x: 18pt, y: 18pt)
)[
  #text(weight: "bold", size: 12pt, fill: primary)[Índice General de Contenidos]
  #v(6pt)
  #line(length: 100%, stroke: 0.6pt + accent)
  #v(12pt)
  
  #outline(
    title: none,
    depth: 2,
    indent: 1.5em
  )
]

#pagebreak()

// ==============================================================================
// 3. CUERPO DEL INFORME
// ==============================================================================

// ==============================================================================
// SECCIÓN: AVANCE 1
// ==============================================================================

#avance-banner(
  "AVANCE 1: Contexto, Modelo de Gestión y Gobernanza",
  "Caracterización Institucional, Modelo de Administración y Mecanismos de Control"
)

== 1. Identificación y Marco Institucional de la Organización

El objeto de estudio del presente trabajo es el *Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)*, unidad académica territorial dependiente de la *Universidad Nacional del Comahue (UNCo)*, con sede central en la ciudad de Viedma, Provincia de Río Negro. Su radio de influencia abarca la comarca Atlántica y se proyecta sobre la vasta geografía social y productiva de la Línea Sur rionegrina.

El estatus institucional del organismo se asienta en el principio de *autonomía académica e institucional y autarquía económico-financiera*, consagrado en el Artículo 75 inciso 19 de la Constitución Nacional Argentina y regulado por la Ley de Educación Superior N° 24.521. Su estructura y dinámica decisoria se rigen por el Estatuto General de la UNCo (Ordenanza N° 470/1993 y modificatorias), el cual consagra el principio del *co-gobierno democrático cuatripartito* (integrado por docentes, estudiantes, graduados y personal nodocente) como el órgano colegiado soberano para la definición de políticas académicas, normativas y de asignación de recursos.

#callout("Misión Institucional y Despliegue Territorial")[
  El CURZAS tiene como misión primordial la creación, formación y democratización del conocimiento científico, técnico y humanístico en el territorio norpatagónico. Su estructura formal articula departamentos académicos, secretarías sustantivas y de apoyo (Académica, de Investigación y Posgrado, de Extensión y de Administración) y órganos de gobierno colegiados (Consejo Directivo y Decanato).
]

== 2. Identificación del Modelo de Administración Predominante

Para caracterizar el modelo de administración del CURZAS, se coteja su realidad funcional con los paradigmas teóricos analizados por *Cao y Blutman (2019)* y *Abal Medina (2014)*, estableciendo una distinción conceptual rigurosa entre la matriz burocrática clásica, el régimen de autonomía universitaria y la Nueva Gestión Pública (NGP).

=== A. Rasgos de la Burocracia Tradicional Weberiana (Matriz Predominante)

El análisis institucional confirma la prevalencia estructural de una *Burocracia Profesional y Weberiana*:

- *Estructura Jerárquica y Centralizada:* Las líneas de autoridad, reporte y delegación de competencias administrativas se encuentran taxativamente fijadas por el organigrama estatutario (Decanato $arrow.r$ Secretarías $arrow.r$ Direcciones $arrow.r$ Departamentos y Divisiones).
- *Principio de Legalidad y Procedimentalismo Normativo:* Los actos administrativos carecen de validez sin el respaldo de resoluciones fundadas, expedientes foliados y dictámenes jurídicos previos, supeditando la discrecionalidad funcionarial al estricto cumplimiento reglamentario.
- *Estatuto del Empleo Público y Carrera Administrativa:* El trabajo docente y nodocente se encuentra regulado por Convenios Colectivos de Trabajo de alcance nacional (Decretos N° 366/06 y N° 1246/15). El régimen garantiza ingreso y promoción por concursos públicos de oposición y antecedentes, estabilidad laboral absoluta y un sistema escalafonario rígido que previene la arbitrariedad política.

=== B. Autonomía Universitaria frente a la Descentralización Gerencial de la NGP

Un aspecto analítico fundamental radica en no confundir la autonomía universitaria con las reformas gerencialistas de los años noventa. Como demuestran *Cao y Blutman (2019)*, la *Nueva Gestión Pública (NGP)* promueve la descentralización como una técnica de *desagregación funcional y fragmentación estructural*, cuyo objetivo es descomponer la administración central en agencias radiales o "unidades de negocios" autónomas que compitan internamente por recursos presupuestarios, orienten su accionar bajo una lógica mercantil y traten al ciudadano como un mero "cliente".

En contraste, la autonomía y la autarquía presupuestaria que ejerce el CURZAS a través de su Consejo Directivo responden a una *conquista histórica y constitucional preexistente* —arraigada en la Reforma Universitaria de 1918 y blindada por la Constitución Nacional— cuyo fin es constituir un *mecanismo político de resguardo democrático, pluralismo ideológico y libertad académica* frente al poder central del Estado. 

En el CURZAS no existen lógicas de mercado propias de la NGP: el financiamiento no se estructura sobre esquemas de *vouchers*, no existe arancelamiento de grado, los presupuestos no dependen de metas mercantiles de egreso ni se celebran contratos individuales de rendimiento por productividad corporativa.

=== C. Rasgos Instrumentales y Modernizadores de la NGP Presentes en la Gestión

La influencia de la NGP en el organismo no es doctrinaria sino *instrumental*, incorporando herramientas para optimizar la gestión pública:

- *Orientación al Usuario/Estudiante en Servicios Académicos:* Incorporación de plataformas de autogestión y ventanilla virtual mediante el ecosistema SIU (Guaraní para gestión académica, Mocoví para gestión presupuestaria de extensión, Wichi/Diaguita) y el sistema de gestión documental electrónica SUDOCU, simplificando trámites, firmas digitales y tiempos de resolución.
- *Evaluación de Calidad y Rendición por Estándares:* Procesos de autoevaluación institucional y acreditación periódica ante la Comisión Nacional de Evaluación y Acreditación Universitaria (CONEAU), incorporando parámetros de mejora continua y transparencia formativa.

#callout("Dictamen de la Matriz Organizacional")[
  *Conclusión:* El CURZAS se define como una *Burocracia Tradicional Weberiana de Base Profesional*, vertebrada por el autogobierno democrático y complementada con herramientas instrumentales de modernización digital.
]

== 3. Análisis de Mecanismos de Rendición de Cuentas (Accountability)

A partir de la conceptualización de Guillermo O'Donnell sistematizada por *Abal Medina (2014)*, la rendición de cuentas institucional en el CURZAS se despliega en tres dimensiones interconectadas:

#v(2pt)

#table(
  columns: (1.1fr, 2.3fr, 1.6fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.5pt + border-subtle,
  inset: (x: 7pt, y: 5.5pt),
  [#text(fill: white, weight: "bold", size: 8.2pt)[Dimensión]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Mecanismos Institucionales en CURZAS / UNCo]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Sustento Normativo / Evidencia]],
  
  [
    *Horizontal* \
    #text(size: 7.2pt, fill: text-muted)[(Control intraestatal e interorgánico)]
  ],
  [
    - Unidad de Auditoría Interna de la UNCo (UAI).
    - Control externo por la Auditoría General de la Nación (AGN) y SIGEN.
    - Contrapesos orgánicos: el Consejo Directivo fiscaliza, aprueba o rechaza la ejecución presupuestaria del Decanato.
  ],
  [
    - Ley 24.156 de Adm. Financiera.
    - Dictámenes de auditoría UAI/AGN.
    - Memoria Anual y Balance de Gestión.
  ],
  
  [
    *Vertical* \
    #text(size: 7.2pt, fill: text-muted)[(Control electoral y representativo)]
  ],
  [
    - Elecciones periódicas, directas y ponderadas para Decano/a y Vicedecano/a.
    - Renovación democrática de los representantes de los cuatro claustros (Docentes, Nodocentes, Estudiantes y Graduados) ante el Consejo Directivo.
  ],
  [
    - Estatuto General de la UNCo.
    - Resoluciones de Junta Electoral y padrones públicos transparentes.
  ],
  
  [
    *Social* \
    #text(size: 7.2pt, fill: text-muted)[(Transparencia y control ciudadano)]
  ],
  [
    - Portal Web de Transparencia Activa y Datos Abiertos.
    - Publicación obligatoria de compras, licitaciones y escalas salariales.
    - Tramitación pública de solicitudes ciudadanas de acceso a la información.
  ],
  [
    - Ley 27.275 de Acceso a la Información Pública.
    - Portal de Transparencia Abierta UNCo.
  ]
)

== 4. Gobernanza y Poligobernanza: La Paradoja del Co-Gobierno Universitario

El análisis de la conducción institucional exige articular los postulados de la *Gobernanza* desarrollados por *Luis Aguilar Villanueva (2006)* con la teoría de la *Poligobernanza y Gobernación Reticular* formulada por *Cao y Blutman (2019, 2021)*.

=== A. Gobernanza Reticular y Poligobernanza en el Marco Teórico

*Aguilar Villanueva (2006)* define la gobernanza como el *proceso de dirección social mediante el cual el gobierno y la sociedad civil interactúan de forma interdependiente*, superando la histórica "insuficiencia directiva del Estado en solitario". La gobernanza implica construir conjuntamente la *intencionalidad social* (los objetivos y valores colectivos) y la *capacidad social* (los recursos y arreglos organizativos para alcanzarlos), transitando desde el monopolio estatal jerárquico hacia sistemas de coordinación reticular y coproducción pública.

Por su parte, *Cao y Blutman (2019, 2021)* profundizan esta visión a través del concepto de *Poligobernanza*, concebida como un modelo de gobernación en red con lógica *bottom-up* (de abajo hacia arriba). Este paradigma propone transformar el Estado en un "Estado plataforma", articulando horizontalmente a organismos públicos con comunidades de práctica, movimientos sociales y organizaciones civiles para romper la inercia, la compartimentación en "silos" y el anquilosamiento normativo que caracteriza a las burocracias tradicionales.

=== B. Análisis Crítico: La Paradoja del Co-Gobierno Institucional

Al examinar la dinámica del CURZAS a la luz de estos conceptos, emerge una *paradoja institucional estructurante*:

1. *El Co-Gobierno como Dirección Social Compartida Interna:* La conformación estatutaria de los órganos colegiados del CURZAS (Consejo Directivo integrado democráticamente por docentes, graduados, estudiantes y nodocentes) representa una experiencia pionera de dirección social compartida incrustada en las entrañas del Estado público.
2. *El Riesgo del "Silo Corporativo Endogámico":* No obstante su virtud democrática interna, la práctica institucional corre el riesgo recurrente de replegarse en una dinámica autorreferencial. En términos de *Cao y Blutman*, las organizaciones burocráticas tienden a operar como "islas" o silos aislados dominados por intereses estamentales, donde las disputas claustrales internas y la reproducción burocrática absorben la energía política, desatendiendo las demandas emergentes del entorno socio-territorial.
3. *El Desafío de la Poligobernanza con la Línea Sur y la Comarca Atlántica:* Para que el co-gobierno trascienda el encapsulamiento burocrático y concrete una verdadera poligobernanza territorial, el CURZAS debe consolidar redes horizontales y proyectos de cocreación con los pequeños productores ganaderos, las cooperativas de trabajo, las comunidades originarias y los municipios de la Línea Sur rionegrina. En este esquema, la *Secretaría de Extensión y Transferencia* se erige como el canal institucional estratégico y la frontera viva donde se debate la superación de la endogamia universitaria.

== 5. Evaluación de Gobernanza Pública Inteligente (Según Oszlak)

A partir de las tesis de *Oscar Oszlak (2020)* sobre la transición del Gobierno Electrónico hacia el *Estado Inteligente* y la Gobernanza Algorítmica, se analizó la penetración de tecnologías disruptivas e Inteligencia Artificial en el organismo.

=== A. Diagnóstico de Madurez Tecnológica

El CURZAS ha consolidado una fase madura de *Gobierno Electrónico e Interoperabilidad Digital* mediante la adopción integral del ecosistema SIU (Guaraní, Mapuche, Diaguita, Mocoví) y el sistema de expedientes digitales SUDOCU. Esto garantiza trazabilidad, firma digital y celeridad procesal, reduciendo sustancialmente el soporte físico en papel.

=== B. Análisis de la Pregunta Guía: Algoritmos e Inteligencia Artificial en Recursos Humanos

#callout("Pregunta de Investigación Institucional")[
  _¿Cuenta el organismo con normativas vigentes sobre la incorporación de algoritmos o software predictivo en la selección o monitoreo de personal?_
]

*Resultados del Relevamiento Normativo y de Gestión:*

- *Inexistencia Absoluta de Algoritmos Predictivos:* En el CURZAS no existen normativas, proyectos piloto ni herramientas de software predictivo o Inteligencia Artificial destinadas a la selección, evaluación de desempeño o monitoreo disciplinario de los trabajadores.
- *Blindaje Paritario y Garantía de Control Humano:* La selección y promoción del personal se rige con exclusividad por jurados y comisiones paritarias integradas por personas humanas, garantizadas por los Convenios Colectivos de Trabajo (Decretos N° 366/06 y N° 1246/15). Existe un consenso institucional y sindical explícito que rechaza la delegación de decisiones laborales en sistemas algorítmicos automatizados.
- *Ubicación en la Escala de Oszlak:* La institución se encuentra plenamente inserta en la etapa de *digitalización de trámites y expedientes*, pero distante de la *Gobernanza Algorítmica y el Estado Inteligente*. Esta distancia no obedece a un mero rezago tecnológico, sino a un blindaje ético, político y gremial orientado a resguardar la transparencia, la imparcialidad y las garantías constitucionales del empleo público.

== 6. Conclusión Sintética del Avance 1

El análisis del CURZAS evidencia una organización pública donde converge una matriz burocrática-profesional weberiana garantista, un régimen de autonomía y co-gobierno democrático conquistado históricamente, e innovaciones tecnológicas orientadas a la modernización de servicios. El desafío estratégico central radica en proyectar su co-gobierno interno hacia redes horizontales de poligobernanza con el territorio de la Línea Sur y la Zona Atlántica rionegrina, preservando la primacía del control humano y paritario frente a los desafíos de la era algorítmica.

#pagebreak()

// ==============================================================================
// SECCIÓN: AVANCE 2 (CONEXIÓN CON LA POLIGOBERNANZA)
// ==============================================================================

#avance-banner(
  "AVANCE 2: Conexión con la Poligobernanza",
  "Estado Plataforma, Interoperabilidad y Tramados Institucionales Ad Hoc"
)

== 1. Introducción y Enfoque Teórico del Avance 2

Avanzando en la aplicación de los marcos contemporáneos sobre modernización y reforma estatal, el presente módulo profundiza la conexión del *CURZAS (UNCo)* con el paradigma de la *Poligobernanza* desarrollado por *Horacio Cao y Gustavo Blutman (2019, 2021)*, complementado con las contribuciones de *Luis F. Aguilar Villanueva (2006)*, *Oscar Oszlak (2020)* y *Jorge Hintze (2018)*. 

El análisis se estructura en torno a dos desafíos organizacionales críticos para la gestión pública universitaria en el territorio norpatagónico: la capacidad de operar bajo la lógica de un *"Estado Plataforma"* interoperable frente a los silos de información, y la conformación de *"Tramados institucionales ad hoc"* para brindar respuestas socio-productivas ágiles frente a la rigidez departamental tradicional.

== 2. Desafío 1: El "Estado Plataforma" e Interoperabilidad frente a los Silos de Información

#callout("Pregunta de Investigación Institucional")[
  _Si pensamos en el "Estado Plataforma" de Cao y Blutman: ¿El CURZAS funciona de manera interoperable compartiendo datos integrados con otros organismos públicos e institutos científicos (como el CONICET o el INTA), o persisten los sistemas aislados de información?_
]

=== A. Marco Conceptual: Del Estado Burocrático al Estado Plataforma

Según *Cao y Blutman (2019, 2021)*, el *Estado Plataforma* representa una superación radical del modelo burocrático cerrado. En lugar de operar como un conjunto de pirámides aisladas que monopolizan trámites y retienen datos en compartimentos estancos, la administración pública se concibe como un *ecosistema digital y sociotécnico articulador*. El Estado provee una infraestructura común, estándares de datos abiertos y arquitecturas de microservicios mediante interfaces de programación de aplicaciones (APIs), permitiendo que diversas áreas gubernamentales, institutos científicos y actores de la sociedad civil colaboren en la coproducción de valor público.

La piedra angular de este modelo es la *Interoperabilidad de Sistemas de Información (IOP)*. Como destacan los autores y ratifica *Oszlak (2020)*, la interoperabilidad no solo asegura la comunicación fluida y segura entre bases de datos heterogéneas, sino que viabiliza el principio de *"una sola vez"* (*once-only*), según el cual ningún ciudadano, productor o investigador debe entregar a una ventanilla estatal información que ya consta en otra dependencia pública.

=== B. Diagnóstico Empírico en el CURZAS: Silos Informáticos y Duplicación Operativa

Al contrastar este modelo con la realidad organizativa del CURZAS y su articulación con los organismos del sistema científico-técnico nacional (*CONICET* e *INTA*), el relevamiento confirma de manera contundente la *persistencia de sistemas aislados de información*:

1. *Silos Informáticos en la Suite de Gestión:* La UNCo opera centralmente con la suite SIU (Guaraní para gestión académica, Mocoví para presupuesto y extensión, Wichi/Diaguita y SUDOCU para expedientes digitales). A nivel de ciencia y tecnología, la Universidad gestiona sus propios registros, mientras que el CONICET exige la carga curricular y de producción en *SIGEVA / CVar* y el INTA maneja sus plataformas propias (*SIGA / SIGEP*).
2. *Persistencia del Trabajo Manual Duplicado:* Aunque el CONICET desarrolló en 2009 un *"módulo de interoperabilidad"* en SIGEVA para convenios específicos con determinadas universidades (como la UBA), *no existe una pasarela API automatizada e institucionalizada en tiempo real* entre las bases de datos de la UNCo y las de CONICET o INTA. Como consecuencia, los docentes-investigadores del CURZAS con doble pertenencia (en el Centro de Investigaciones y Transferencia *CIT Río Negro / CCT Patagonia Norte* o en proyectos radicados en la *Estación Experimental Agropecuaria INTA Valle Inferior*) deben ingresar manualmente sus datos curriculares, memorias de investigación y producciones científicas por duplicado o triplicado en cada sistema por separado.
3. *Duplicación de Relevamientos en la Región Sur y Zona Atlántica:* En el plano socio-territorial, las iniciativas de relevamiento de datos socio-productivos, censos campesinos y mapas de vulnerabilidad agroclimática en la Línea Sur continúan ejecutándose de forma fragmentada por cada organismo. La falta de un repositorio digital interoperable único reproduce las *"islas burocráticas"*, insume costos transaccionales innecesarios y priva a la región de una analítica de datos integrada para la toma de decisiones públicas basadas en evidencia.

#callout("Dictamen sobre el Eje 1")[
  *Conclusión:* En el CURZAS *persiste un modelo de sistemas aislados de información*. Si bien se ha consolidado una fase madura de digitalización interna de trámites (SIU/SUDOCU), la transición hacia un *Estado Plataforma interoperable* con CONICET e INTA permanece como una deuda estructural pendiente.
]

== 3. Desafío 2: "Tramados Institucionales Ad Hoc" frente a la Rigidez Departamental

#callout("Pregunta de Investigación Institucional")[
  _Pensando en los "Tramados institucionales ad hoc": ¿Las secretarías de Extensión o Investigación configuran redes flexibles y temporales con municipios locales para resolver demandas socio-productivas de urgencia regional, rompiendo la rigidez de los departamentos tradicionales?_
]

=== A. Marco Conceptual: Tramados Ad Hoc y Gestión Matricial por Proyectos

El concepto de *tramados institucionales ad hoc* es formulado por *Cao y Blutman (2019, 2021)* en el seno de la teoría de la Poligobernanza. Frente a la naturaleza hipercompleja, volátil y heterogénea de las problemáticas sociales contemporáneas, las estructuras burocráticas jerárquicas y departamentales —diseñadas para administrar rutinas estables y estandarizadas— resultan excesivamente lentas, rígidas e ineficaces.

La Poligobernanza postula la conformación de *arreglos institucionales dinámicos, flexibles y temporales* (adhocracias y estructuras matriciales), donde organismos estatales, gobiernos locales, universidades y comunidades se articulan en red en función de metas concretas. Como analiza *Jorge Hintze (2018)*, estas modalidades por proyecto/programa permiten movilizar recursos interdisciplinarios y brindar respuestas rápidas a demandas de urgencia territorial sin necesidad de alterar la macroestructura burocrática permanente del organismo.

#pagebreak()
=== B. Evidencia Empírica Territorial: El Rol Articulador de Extensión y Ciencia y Técnica en el CURZAS

La estructura funcional del CURZAS ratifica plenamente este funcionamiento reticular. Frente a los dilatados tiempos administrativos y las deliberaciones reglamentarias de los Departamentos Académicos disciplinares (*Humanidades, Psicopedagogía, Administración, Ciencia y Técnica*), son las *Secretarías de Extensión y de Ciencia y Técnica / Posgrado* las que quiebran el aislamiento estamental y configuran *tramados institucionales ad hoc*:

1. *Proyecto Nodos Regionales del CURZAS (Red Territorial Descentralizada):* La UNCo consolidó y desplegó una red institucional descentralizada conformada por *10 nodos regionales* estratégicos en el territorio rionegrino (Noticias Río Negro, 2026). A través de convenios de cogestión con municipios locales y comisiones de fomento, y mediante la designación por concurso de *Asistentes Técnico-Pedagógicos locales*, el CURZAS acerca ofertas académicas territorializadas y carreras de grado, adaptando la presencia universitaria a la dispersión geográfica y conectando las distintas microrregiones provinciales con la sede central de Viedma:

  #v(2pt)
  #align(center)[
    #block(
      width: 100%,
      breakable: false,
      fill: bg-card,
      stroke: 0.6pt + border-subtle,
      radius: 4pt,
      inset: (x: 10pt, top: 8pt, bottom: 8pt),
      [
        #text(weight: "bold", fill: primary, size: 8.8pt)[Estructura Territorial y Oferta Académica del CURZAS en Río Negro]
        #v(4pt)
        #table(
          columns: (115pt, 1fr),
          stroke: 0.3pt + border-subtle,
          fill: (x, y) => if y == 0 { primary } else if calc.even(y) { rgb("#f8fafc") } else { white },
          align: (left + horizon, left + horizon),
          inset: (x: 7pt, y: 3.5pt),
          table.header(
            text(weight: "bold", fill: white, size: 8pt)[Eje Territorial y Académico],
            text(weight: "bold", fill: white, size: 8pt)[Detalle Institucional]
          ),
          [#text(weight: "bold", fill: primary, size: 8pt)[10 Nodos Regionales]],
          [#text(size: 8pt)[
            • *Línea Sur:* Ingeniero Jacobacci, Maquinchao, Los Menucos, Sierra Colorada, Ramos Mexía y Valcheta. \
            • *Zona Atlántica y Valles:* San Antonio Oeste, Sierra Grande, General Conesa y Río Colorado.
          ]],
          [#text(weight: "bold", fill: primary, size: 8pt)[Carreras Dictadas]],
          [#text(size: 8pt)[
            • *Licenciatura en Recursos Humanos* (Ciclo de Complementación Curricular) \
            • *Licenciatura en Arte y Sociedad* \
            • _Entre otras propuestas formativas de grado, ciclos y tecnicaturas del CURZAS._
          ]]
        )
        #v(8pt)
        #image("tareas/actividad_01/entregables/avance 2/img/RioNegro.svg", height: 300pt)
        #v(4pt)
        #text(size: 7.8pt, fill: text-muted, style: "italic")[
          *Figura 1:* Mapa de la Provincia de Río Negro con división departamental, cabeceras y Sede Central CURZAS (Viedma), articulando la red de Nodos Regionales y proyectos de extensión territorial.
        ]
      ]
    )
  ]

#pagebreak()
2. *Proyectos de Extensión Territorializados:* Un ejemplo paradigmático de la agenda extensionista del CURZAS es el proyecto *"Nodos en red: experiencias sustentables de producción para pequeños productores"* (liderado por docentes-investigadores del CURZAS como Mgtr. Nancy Osses y Esp. Silvia Martínez). Este dispositivo interviene directamente en territorio junto a pequeños productores de *Valcheta, San Antonio Oeste y General Conesa*, promoviendo la exploración de saberes previos, el acompañamiento técnico, la diversificación productiva y el agregado de valor en origen.
3. *Mesas Técnicas Interinstitucionales y Emergencias Regionales:* Ante problemáticas socio-ambientales críticas (como la crisis hídrica o la vulnerabilidad de la ganadería ovina y caprina), las secretarías conforman mesas ad hoc temporales junto al Departamento Provincial de Aguas (DPA), el INTA y cooperativas rurales para implementar sistemas de captación de agua de lluvia y mejoras en el manejo forrajero.
4. *Aporte de la Gobernanza Reticular (Aguilar Villanueva):* En estas experiencias, el CURZAS no impone soluciones tecnocráticas verticales (*top-down*), sino que se inserta como un nodo articulador en una red horizontal (*bottom-up*), donde el conocimiento científico-académico se negocia y coproduce con los saberes empíricos de las comunidades locales y la capacidad operativa de los gobiernos municipales.

#callout("Dictamen sobre el Eje 2")[
  *Conclusión:* Las Secretarías de Extensión y de Ciencia y Técnica del CURZAS *sí configuran tramados institucionales ad hoc y redes flexibles temporales*, funcionando como auténticas adhocracias matriciales que sortean la rigidez departamental y responden con celeridad a las urgencias socio-productivas de la Patagonia Norte.
]

#pagebreak()
=== C. Objetivo: Analizar la Viabilidad y las Capacidades Institucionales de la Entidad

A efectos de cumplir con el objetivo de evaluar la viabilidad organizativa y las capacidades institucionales para sostener la presencia territorial y académica del *CURZAS (UNCo)*, el análisis se organiza de forma sistemática articulando los entregables específicos requeridos, el relevamiento de las fuentes documentales institucionales y el procesamiento de las preguntas guía situacionales.

==== 1. Entregables Específicos

===== A. Elaboración de una Matriz FODA Situada en el Contexto Actual del Organismo

A partir del cotejo entre las memorias de gestión institucional y las variables críticas del entorno universitario y socio-productivo rionegrino, se presenta la siguiente *Matriz FODA situada*, que cruza los factores endógenos del CURZAS con el contexto actual:

#v(2pt)

#table(
  columns: (1fr, 1fr),
  stroke: 0.5pt + border-subtle,
  fill: (x, y) => if y == 0 { primary } else if y == 2 { rgb("#174075") } else { bg-card },
  inset: (x: 8pt, y: 6pt),
  table.header(
    text(weight: "bold", fill: white, size: 8.5pt)[FORTALEZAS (Factores Internos Positivos)],
    text(weight: "bold", fill: white, size: 8.5pt)[DEBILIDADES (Factores Internos Operativos)]
  ),
  [
    #text(size: 7.9pt)[
      - *Presencia Territorial Activa:* Red descentralizada de *10 Nodos Regionales* en la Línea Sur y Zona Atlántica, democratizando el acceso a la educación superior.
      - *Legitimidad Democrática e Institucional:* Co-gobierno cuatripartito participativo y funcionamiento regular de órganos colegiados de deliberación.
      - *Estabilidad Laboral y Blindaje por CCT:* Plantillas docentes y nodocentes amparadas por Decretos N° 366/06 y 1246/15, asegurando continuidad y retención técnica.
      - *Modernización de la Gestión Digital:* Adopción integral del ecosistema SIU (Guaraní, Mapuche, Diaguita) y tramitación electrónica por SUDOCU.
      - *Oferta Formativa Estratégica:* Pertinencia en carreras de grado y ciclos de articulación (e.g. Lic. en Recursos Humanos) adaptadas a la demanda local.
    ]
  ],
  [
    #text(size: 7.9pt)[
      - *Silos Informáticos y Falta de Interoperabilidad:* Ausencia de comunicación técnica automática con CONICET (SIGEVA) e INTA, con tareas manuales duplicadas.
      - *Sobrecarga Administrativa en Sede Central:* Cuello de botella en personal para atender simultáneamente las demandas telemáticas y presenciales de los 10 nodos.
      - *Rigidez de Estructuras Departamentales:* Resistencia disciplinar que enlentece la asignación flexible de recursos para proyectos matriciales ad hoc.
      - *Brechas en Competencias Técnicas Digitales:* Deficiencias en analítica de datos, gestión integral por procesos y soporte de redes telemáticas complejas.
      - *Infraestructura Edilicia y Tecnológica Prestada:* Dependencia funcional de convenios con municipios para el uso de dependencias en los nodos del interior.
    ]
  ],
  table.cell(fill: primary)[
    #text(weight: "bold", fill: white, size: 8.5pt)[OPORTUNIDADES (Factores Externos Positivos)]
  ],
  table.cell(fill: primary)[
    #text(weight: "bold", fill: white, size: 8.5pt)[AMENAZAS (Factores Externos de Riesgo)]
  ],
  [
    #text(size: 7.9pt)[
      - *Creciente Demanda Formativa Regional:* Alto interés de comunidades y agentes públicos del interior rionegrino por ofertas a distancia y de extensión.
      - *Alianzas de Poligobernanza Local:* Disposición favorable de intendencias y comisiones de fomento para cogestionar espacios y logística comarcal.
      - *Cocreación Socio-Productiva:* Articulación extensionista con pequeños productores rurales y cooperativas comarcales (Proyecto *Nodos en Red*).
      - *Fortalecimiento de la Educación Híbrida:* Consolidación de herramientas tecno-pedagógicas virtuales para mitigar el aislamiento territorial.
    ]
  ],
  [
    #text(size: 7.9pt)[
      - *Severo Desfinanciamiento Presupuestario Nacional:* Inflación, congelamiento de partidas para funcionamiento e interrupción de obras públicas educativas.
      - *Erosión Salarial y Conflictividad Gremial:* Pérdida del poder adquisitivo de salarios docentes y nodocentes ante la falta de paritarias nacionales homologadas.
      - *Dispersión Geográfica y Déficit de Conectividad:* Extensas distancias logísticas en la estepa patagónica y severas fallas en el tendido de internet en parajes.
      - *Volatilidad Regulatoria Nacional:* Retiro de programas de financiamiento universitario y restricciones para nuevas designaciones y cargos docentes.
    ]
  ]
)

#pagebreak()
===== B. Desarrollo de un Mapeo de Actores Clave (Stakeholders) que Influyen en las Decisiones del Área de Recursos Humanos

Las decisiones atinentes al empleo público, dotación y condiciones de trabajo en el CURZAS constituyen un campo de fuerzas donde interactúan múltiples actores con intereses y recursos de poder diferenciados:

#v(2pt)

#table(
  columns: (1fr, 0.65fr, 0.65fr, 1.8fr, 1.3fr),
  stroke: 0.4pt + border-subtle,
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  inset: (x: 5.5pt, y: 4.2pt),
  table.header(
    text(weight: "bold", fill: white, size: 7.6pt)[Actor Clave (Stakeholder)],
    text(weight: "bold", fill: white, size: 7.6pt)[Ámbito],
    text(weight: "bold", fill: white, size: 7.6pt)[Poder / Interés],
    text(weight: "bold", fill: white, size: 7.6pt)[Intereses y Demandas Centrales],
    text(weight: "bold", fill: white, size: 7.6pt)[Estrategia de Viabilidad / Gestión]
  ),
  [
    *Gremio Nodocente (APUNC / FATUN)*
  ],
  [Interno / Gremial],
  [Alto / Muy Alto],
  [
    #text(size: 7.4pt)[
      Cumplimiento estricto del CCT 366/06; llamado a concursos de planta y ascensos; capacitación técnica situada; condiciones seguras de trabajo; defensa salarial.
    ]
  ],
  [
    #text(size: 7.4pt)[
      Comisión Paritaria Particular permanente; acuerdos paritarios de criterios concursales; cogestión de programas de capacitación laboral.
    ]
  ],
  [
    *Gremio Docente (ADUNC / CEDIUNCO)*
  ],
  [Interno / Gremial],
  [Alto / Muy Alto],
  [
    #text(size: 7.4pt)[
      Aplicación efectiva del CCT 1246/15; regularización de interinatos mediante concursos de carrera docente; mayor dedicación horaria; recomposición salarial.
    ]
  ],
  [
    #text(size: 7.4pt)[
      Mesa de Paritaria Docente Particular; planificación concertada de cronogramas de sustanciación de concursos de oposición y antecedentes.
    ]
  ],
  [
    *Consejo Directivo (CURZAS)*
  ],
  [Interno / Co-Gobierno],
  [Muy Alto / Muy Alto],
  [
    #text(size: 7.4pt)[
      Aprobación de la estructura organizativa, llamado a concursos, asignación de cargos entre departamentos y fiscalización del presupuesto operativo.
    ]
  ],
  [
    #text(size: 7.4pt)[
      Construcción democrática de mayorías parlamentarias claustrales; fundamentación técnica y académica rigurosa de las propuestas de RR. HH.
    ]
  ],
  [
    *Decanato y Secretarías de Gestión*
  ],
  [Interno / Ejecutivo],
  [Muy Alto / Alto],
  [
    #text(size: 7.4pt)[
      Gobernabilidad administrativa; eficiencia en la asignación de recursos escasos; cobertura de funciones críticas para sostener la sede y los 10 nodos.
    ]
  ],
  [
    #text(size: 7.4pt)[
      Liderazgo institucional dialógico; articulación interdepartamental; flexibilización de cargas de trabajo mediante proyectos transversales.
    ]
  ],
  [
    *Claustros Estudiantil y Graduados*
  ],
  [Interno / Académico],
  [Medio / Alto],
  [
    #text(size: 7.4pt)[
      Excelencia pedagógica docente; cumplimiento de fechas de exámenes; agilidad en ventanilla de trámites de títulos y equivalencias; soporte virtual fluido.
    ]
  ],
  [
    #text(size: 7.4pt)[
      Atención por canales telemáticos multicanal (Guaraní/SUDOCU); fortalecimiento de tutorías académicas en los nodos regionales.
    ]
  ],
  [
    *Rectorado y Consejo Superior UNCo*
  ],
  [Central / Institucional],
  [Muy Alto / Medio-Alto],
  [
    #text(size: 7.4pt)[
      Coherencia normativa general universitaria; control del techo de masa salarial; homologación formal de concursos docentes y nodocentes.
    ]
  ],
  [
    #text(size: 7.4pt)[
      Defensa fundada de las especificidades territoriales, distancias y complejidades nodales del CURZAS ante la administración central de Neuquén.
    ]
  ],
  [
    *Subsecretaría de Políticas Universitarias (SPU)*
  ],
  [Externo / Nacional],
  [Muy Alto / Medio (Fiscal)],
  [
    #text(size: 7.4pt)[
      Control y restricción de partidas salariales (inciso 1); verificación de plantas de personal; cumplimiento de parámetros de disciplina fiscal del Estado nacional.
    ]
  ],
  [
    #text(size: 7.4pt)[
      Rigor en la rendición de cuentas financieras; actuación coordinada en el marco del Consejo Interuniversitario Nacional (CIN).
    ]
  ],
  [
    *Municipios y Comisiones de Fomento (Nodos)*
  ],
  [Externo / Territorial],
  [Medio / Alto],
  [
    #text(size: 7.4pt)[
      Presencia de Asistentes Técnico-Pedagógicos locales; estabilidad y continuidad de las cohortes de carreras universitarias en sus localidades.
    ]
  ],
  [
    #text(size: 7.4pt)[
      Convenios de contraprestación operativa (cesión de espacios físicos, personal comunal de apoyo, facilitación de conectividad e insumos).
    ]
  ]
)

#pagebreak()
===== C. Evaluación de las Capacidades Estatales del Organismo Siguiendo la Metodología de Bertranou

A partir del marco formulado por *Julián Bertranou (2015)*, la capacidad institucional del Estado se define como la *aptitud de las estructuras y agentes públicos para problematizar demandas, construir consensos, organizar rutinas y transformar recursos en bienes y servicios públicos de calidad*. Bertranou operacionaliza este concepto en tres dimensiones:

#v(2pt)

*1. Capacidad Político-Relacional (Gobernabilidad Democrática y Construcción de Redes):*
- *Definición:* Aptitud para interactuar con actores sociopolíticos, procesar pacíficamente conflictos, construir legitimidad y forjar alianzas estratégicas.
- *Diagnóstico en el CURZAS:* *Desempeño Alto.* El co-gobierno canaliza y resuelve institucionalmente las demandas claustrales en el Consejo Directivo y en comisiones paritarias particulares con APUNC y ADUNC. A nivel externo, el organismo exhibe una extraordinaria aptitud relacional para tejer convenios con municipios para los *10 Nodos Regionales*, así como con el INTA y asociaciones de pequeños productores en proyectos sustentables.

*2. Capacidad Administrativa / Organizacional (Rutinas, Procesos y Tecnologías de Gestión):*
- *Definición:* Aptitud de los dispositivos burocráticos y procedimientos formales para tramitar actos y asignar recursos con celeridad, legalidad y transparencia.
- *Diagnóstico en el CURZAS:* *Desempeño Medio-Alto.* Alta solvencia en el manejo normativo del empleo público, rendición financiera y digitalización por SUDOCU y SIU. Sin embargo, persisten dos puntos críticos: la falta de interoperabilidad automática con CONICET (SIGEVA) e INTA (silos de datos) y la sobrecarga administrativa en la sede central de Viedma para procesar demandas telemáticas de los 10 nodos.

*3. Capacidad Técnica / Analítica (Saberes, Idoneidad y Competencias de la Plantilla):*
- *Definición:* Calificación profesional, idoneidad técnica y habilidades cognitivas de la dotación de personal para diseñar, coordinar y evaluar políticas sustantivas.
- *Diagnóstico en el CURZAS:* *Desempeño Medio.* Coexiste una alta calificación académica disciplinar en docentes y dominio de rutinas regladas en nodocentes, pero con deficiencias críticas ante la digitalización compleja y la educación a distancia territorializada.

#pagebreak()
==== 2. Qué Buscar: Plan Estratégico Institucional Vigente, Planes Operativos Anuales (POA) y Memorias de Gestión Anuales

Para fundamentar empíricamente el diagnóstico institucional del CURZAS, se procedió a la búsqueda, relevamiento y análisis de los principales instrumentos de gestión y planificación de la UNCo:

1. *Plan Estratégico Institucional Vigente de la UNCo:* Define las líneas directrices, misión, visión y ejes de desarrollo académico, científico y extensionista. Se constata que formalmente plantea metas de democratización del conocimiento y despliegue territorial, pero su diseño responde predominantemente a una formulación normativa centralizada ("top-down"), con escasa consideración explícita de los condicionamientos de viabilidad sociopolítica de las unidades académicas descentralizadas.
2. *Planes Operativos Anuales (POA):* Traducen las metas estratégicas en programas presupuestarios anuales parametrizados. Exhiben una lógica de asignación cuantitativa de partidas y recursos, formulada bajo la hipótesis de previsibilidad macroeconómica, la cual resulta desbordada por los ciclos inflacionarios y los recortes del Estado nacional.
3. *Memorias Anuales de Gestión:* Constituyen el registro documental de balance de las acciones cumplidas, ejecución presupuestaria, matrícula estudiantil y producción académica. En ellas se refleja con claridad la brecha entre las metas programadas formalmente y las contingencias reales: registran la sobrecarga administrativa en las secretarías, las dificultades operativas de los nodos del interior y el impacto del congelamiento de vacantes de personal.

==== 3. Preguntas Guía para Recolectar

===== A. ¿Los planes vigentes son normativos (rígidos) o adoptan un enfoque situacional (PES) que considera a los trabajadores como actores estratégicos?

El relevamiento documental y funcional confirma que los planes vigentes son formalmente *normativos (rígidos)*, pero la dinámica operativa real exige de manera insoslayable un *enfoque situacional (PES)*:

- *Crítica al Modelo Normativo Tradicional:* Como postuló *Carlos Matus*, la planificación tradicional normativa asume erróneamente un sistema estático y cerrado, donde quien planifica cree poseer el monopolio del poder y el control absoluto de las variables. En esta concepción abstracta, el plan es un "deber ser" lineal y los trabajadores son tratados como meros recursos administrativos pasivos ejecutores de reglamentos.
- *Premisas Clave de la Planificación Estratégica Situacional (PES de Carlos Matus):*
  1. *La situación como punto de partida:* No hay un diagnóstico objetivo único; la realidad es explicada por diferentes actores desde su propia posición, intereses y cuota de poder (explicación situacional).
  2. *El juego social e incertidumbre:* El planificador convive en el tablero con la resistencia, intereses contrapuestos y alianzas de otros actores que también planifican y juegan.
  3. *Procesamiento de problemas complejos:* En lugar de metas cuantitativas ciegas, la PES actúa sobre problemas concretos (brecha entre realidad observada y deseada) identificando sus causas nodales.
  4. *Los trabajadores como actores estratégicos:* En el CURZAS, el personal docente y nodocente son actores estratégicos con representación en el co-gobierno, intereses propios y poder de veto en comisiones paritarias (APUNC y ADUNC). Todo planeamiento exige unir indisolublemente la *viabilidad técnica con la viabilidad política*.

#pagebreak()
*Matriz de los Cuatro Momentos de la Planificación Estratégica Situacional (PES de Carlos Matus):*

#v(3pt)

#table(
  columns: (1.1fr, 0.75fr, 1.55fr, 1.8fr),
  stroke: 0.4pt + border-subtle,
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  inset: (x: 6.5pt, y: 5.5pt),
  table.header(
    text(weight: "bold", fill: white, size: 7.8pt)[Momento de la PES (Carlos Matus)],
    text(weight: "bold", fill: white, size: 7.8pt)[Interrogante Rector],
    text(weight: "bold", fill: white, size: 7.8pt)[Fundamento Conceptual y Operativo],
    text(weight: "bold", fill: white, size: 7.8pt)[Aplicación Situada en el CURZAS (UNCo)]
  ),
  [
    *1. Momento Explicativo* \
    #text(size: 7pt, fill: text-muted)[(Apreciación situacional)]
  ],
  [*¿Fue, es y será?*],
  [
    #text(size: 7.3pt)[
      Indagación y selección de problemas complejos. Reconstrucción de causas nodales desde la perspectiva diferenciada de cada fuerza social. Rechazo del diagnóstico único tecnocrático.
    ]
  ],
  [
    #text(size: 7.3pt)[
      Diagnóstico situado de problemas críticos: asfixia presupuestaria nacional, sobrecarga administrativa en sede Viedma, dispersión en 10 nodos y silos de datos no interoperables con CONICET/INTA.
    ]
  ],
  [
    *2. Momento Normativo* \
    #text(size: 7pt, fill: text-muted)[(Diseño del horizonte)]
  ],
  [*¿Debiera ser?*],
  [
    #text(size: 7.3pt)[
      Diseño de la situación-objetivo y formulación de la estrategia deseable. Construcción del programa direccional y operaciones para cerrar la brecha entre realidad observada y deseada.
    ]
  ],
  [
    #text(size: 7.3pt)[
      Proyecto de un CURZAS descentralizado e inclusivo en la Línea Sur y Costa Atlántica, con co-gobierno transparente, oferta híbrida accesible y un Estado Plataforma interoperable.
    ]
  ],
  [
    *3. Momento Estratégico* \
    #text(size: 7pt, fill: text-muted)[(Construcción de viabilidad)]
  ],
  [*¿Puedo hacer?*],
  [
    #text(size: 7.3pt)[
      Cálculo de fuerzas en el juego social. Construcción articulada de viabilidad política (alianzas y neutralización de vetos), económica, institucional y cognitiva para vencer resistencias.
    ]
  ],
  [
    #text(size: 7.3pt)[
      Concertación paritaria permanente con gremios APUNC y ADUNC; acuerdos de cogestión con intendencias locales (aportes logísticos) y articulación interinstitucional con INTA y DPA.
    ]
  ],
  [
    *4. Momento Táctico-Operacional* \
    #text(size: 7pt, fill: text-muted)[(Acción y coyuntura)]
  ],
  [*¿Hacer?*],
  [
    #text(size: 7.3pt)[
      Mediación entre el plan y la acción diaria en la coyuntura. Monitoreo continuo, evaluación de trayectorias y reajuste flexible del plan en tiempo real ante imprevistos del entorno.
    ]
  ],
  [
    #text(size: 7.3pt)[
      Gestión cotidiana de cursadas telemáticas en nodos, resolución ágil de contingencias climáticas y de conectividad en la estepa, y reasignación de partidas ante la inflación nacional.
    ]
  ]
)

#v(4pt)

#callout("Articulación Teórico-Práctica de la PES")[
  *Conclusión del Análisis Situacional:* Como postula Matus, la planificación no es un ejercicio de cálculo aritmético sobre variables dadas, sino una *teoría del juego social*. La viabilidad del CURZAS no emana de la imposición vertical de reglamentos, sino de la capacidad directiva para articular la *viabilidad técnica* (calidad académica y solvencia digital) con la *viabilidad política* (procesamiento del conflicto claustral y negociación paritaria permanente).
]

#pagebreak()
===== B. ¿Cuáles son las principales fortalezas y debilidades operativas manifestadas de forma interna (insumo directo para la matriz FODA)?

El relevamiento operativo interno arroja las siguientes conclusiones que nutren directamente la Matriz FODA:
- *Fortalezas Operativas Internas:* Presencia activa y descentralizada en *10 Nodos Regionales*; co-gobierno democrático cuatripartito consolidado; estabilidad laboral y derechos blindados por Convenios Colectivos de Trabajo (Decretos N° 366/06 y 1246/15); adopción exitosa del ecosistema informático SIU y expediente digital SUDOCU; y oferta académica pertinente (Licenciatura en Recursos Humanos, Ciclos de Grado).
- *Debilidades Operativas Internas:* Persistencia de *silos informáticos* sin interoperabilidad con CONICET (SIGEVA) e INTA, con tareas manuales duplicadas; sobrecarga operativa y cuello de botella en la planta administrativa de la sede Viedma ante la demanda telemática de los nodos; rigidez departamental disciplinar frente a proyectos matriciales; y brechas en competencias técnicas digitales.

===== C. ¿Existen deficiencias críticas detectadas en las competencias técnicas de las plantillas actuales (capacidad estatal)?

El relevamiento empírico de las competencias laborales del personal docente y nodocente constata *cuatro deficiencias críticas*:
1. *Brechas en Analítica de Datos y Gestión Digital:* En el personal nodocente predomina la carga de datos rutinaria, con escasas competencias en analítica de datos, tableros de gestión, interoperabilidad y ciberseguridad.
2. *Asimetrías Pedagógicas para Entornos Híbridos:* En el cuerpo docente subsiste heterogeneidad en el dominio de herramientas tecno-pedagógicas y tutorías a distancia requeridas por el modelo de nodos territoriales.
3. *Rigidez Escalafonaria:* El escalafón administrativo tradicional dificulta la incorporación ágil de nuevos perfiles tecnológicos de vanguardia (programadores, ingenieros de datos).
4. *Necesidad de un Plan Situado de Capacitación Continua:* Se requiere diseñar en comisiones paritarias un plan específico que capacite en gobernanza digital, conectividad remota y gestión pública por resultados.

#callout("Dictamen Integral de Viabilidad y Capacidades")[
  *Conclusión:* El CURZAS ostenta una *robusta capacidad político-relacional* y una *eficiente capacidad administrativa procedimental*, pero su *capacidad técnica y analítica* enfrenta deficiencias operativas ante la digitalización compleja y la dispersión geográfica. La adopción de la *Planificación Estratégica Situacional (PES de Matus)* resulta imperativa para tratar a los trabajadores como actores estratégicos de coproducción y garantizar la viabilidad del proyecto universitario frente a las restricciones del contexto nacional.
]

#pagebreak()
== 4. Síntesis y Conclusiones del Avance 2

El análisis integral abordado a lo largo del Avance 2 articula los hallazgos en tres dimensiones nodales que definen la situación organizacional y las capacidades institucionales del *CURZAS (UNCo)*:

1. *En la Dimensión Informacional e Interoperabilidad (Eje 1):*
  Se constató que, pese al éxito en la digitalización interna de trámites con el ecosistema SIU y SUDOCU, *persiste un modelo fragmentado de silos informáticos*. La inexistencia de pasarelas API automatizadas e interoperables en tiempo real con organismos científicos estratégicos como CONICET (SIGEVA) e INTA reproduce tareas manuales duplicadas para los investigadores y obstaculiza la concreción de un auténtico *Estado Plataforma* en la región norpatagónica.

2. *En la Dimensión Territorial y Poligobernanza Reticular (Eje 2):*
  La institución demuestra una destacada y flexible *capacidad de respuesta adhocrática* a través de las Secretarías de Extensión y de Ciencia y Técnica. Mediante la conformación de *tramados institucionales ad hoc* y la consolidación de la *red descentralizada de 10 Nodos Regionales* en la Línea Sur y Costa Atlántica, el CURZAS rompe la lentitud y rigidez de los departamentos académicos tradicionales. Proyectos territoriales como *Nodos en Red* y las mesas técnicas comarcales expresan la potencia de la *gobernanza reticular* formulada por Aguilar Villanueva y la *poligobernanza* postulada por Cao y Blutman.

3. *En la Dimensión de Viabilidad, Planificación y Capacidades Estatales (Eje 3):*
  - *Superación del Paradigma Normativo hacia el Enfoque Situacional (PES de Matus):* Los planes institucionales formales (Plan Estratégico y POAs) conservan una matriz normativa rígida y lineal. Sin embargo, la gobernabilidad real del CURZAS demanda aplicar la *Planificación Estratégica Situacional*, en la cual los trabajadores docentes y nodocentes son reconocidos como *actores estratégicos vitales* con intereses propios, poder de veto paritario y capacidad de coproducción institucional.
  - *Matriz FODA Situada:* Se identificó una institución con fortalezas notables (red de 10 nodos, arraigo territorial, co-gobierno democrático, estabilidad por CCT) y oportunidades de expansión socio-productiva local, pero amenazada por una asfixiante crisis presupuestaria nacional y limitada internamente por silos informáticos, sobrecarga administrativa y brechas de competencias técnicas.
  - *Mapeo de Actores de Recursos Humanos:* La arena laboral se estructura sobre un equilibrio de fuerzas entre gremios (APUNC y ADUNC), órganos colegiados (Consejo Directivo y Superior), el Decanato y las regulaciones fiscales del Estado nacional (SPU), requiriendo acuerdos en paritarias locales permanentes para viabilizar cualquier reforma.
  - *Evaluación de Capacidades Estatales (Bertranou):* Mientras que la *capacidad político-relacional* se destaca como alta y la *capacidad administrativa* como media-alta en rutinas regladas, la *capacidad técnica y analítica* exhibe deficiencias críticas en analítica de datos, gestión telemática remota y pedagogía virtual híbrida, profundizadas por la rigidez del régimen escalafonario para captar perfiles de vanguardia.

*Dictamen Estratégico Final:*
El reto primordial de planeamiento para el CURZAS reside en *articular su potencia de poligobernanza territorial con la modernización de sus capacidades técnicas y de interoperabilidad digital*. Solo transitando hacia una planificación estratégica situacional que empodere y capacite a su personal, y estructurándose como nodo en un Estado Plataforma, la universidad afianzará su misión democratizadora y productiva en la Patagonia Norte.

#pagebreak()

// ==============================================================================
// 3. HOJA DEDICADA: BIBLIOGRAFÍA Y FUENTES ACADÉMICAS CONSOLIDADAS
// ==============================================================================

#heading(level: 1, outlined: true, bookmarked: true)[Bibliografía]

#v(15pt)

#rect(
  width: 100%,
  fill: bg-card,
  stroke: 0.5pt + border-subtle,
  radius: 6pt,
  inset: (x: 18pt, y: 18pt)
)[
  #text(weight: "bold", size: 12pt, fill: primary)[Bibliografía y Fuentes Académicas Consultadas]
  #v(6pt)
  #line(length: 100%, stroke: 0.6pt + accent)
  #v(12pt)
  
  #set text(size: 8.7pt, fill: text-main)
  - *Abal Medina, Juan Manuel (2014).* _Manual de Administración Pública._ Buenos Aires: Ariel. Capítulos 1 y 5.
  - *Aguilar Villanueva, Luis F. (2006).* _Gobernanza y Gestión Pública._ México D.F.: Fondo de Cultura Económica.
  - *Bertranou, Julián (2015).* _Capacidad estatal: revisión del concepto y algunos ejes de análisis y debate._ Revista Estado y Políticas Públicas, N° 4, FLACSO Argentina.
  - *Cao, Horacio y Blutman, Gustavo (2019).* _Continuidades y rupturas en las ideas sobre reforma y modernización del Estado._ Buenos Aires: INAP / Universidad de Buenos Aires.
  - *Cao, Horacio y Blutman, Gustavo (2021).* _Escenarios futuros para la administración pública: Poligobernanza y Neoweberianismo._ Documentos de Trabajo del INAP.
  - *CONICET (2009).* _Módulo de Interoperabilidad del Sistema Integral de Gestión y Evaluación (SIGEVA)._ Buenos Aires: Consejo Nacional de Investigaciones Científicas y Técnicas.
  - *CURZAS — Universidad Nacional del Comahue (2023).* _Avanza el proyecto Nodos CURZA UNCo Región Sur._ Área de Educación a Distancia y Nodos Territoriales. Disponible en: `https://web.curza.uncoma.edu.ar/educacion-distancia/nodos/avanza-el-proyecto-nodos-region-sur`.
  - *CURZAS — Universidad Nacional del Comahue (2024).* _Proyectos de Extensión: Nodos en red: experiencias sustentables de producción para pequeños productores (Dir. Mgtr. Nancy Osses et al.)._ Secretaría de Extensión y Transferencia. Disponible en: `https://web.curza.uncoma.edu.ar/extension/pe-proyectos`.
  - *Hintze, Jorge (2018).* _Gestión por procesos y diseño de estructuras en la administración pública: La articulación entre estructuras permanentes y proyectos temporales._ Buenos Aires: TOP / INAP.
  - *Matus, Carlos (1993).* _Guía de análisis teórico de la Planificación Estratégica Situacional._ Caracas: Fundación Altadir / Fondo Editorial Altadir.
  - *Matus, Carlos (2007).* _Teoría del juego social._ Lanús: Ediciones de la UNLa.
  - *Noticias Río Negro (2026).* _El CURZAS - UNCo abrió la preinscripción 2026 en Viedma y los 10 nodos regionales._ Disponible en: #link("https://noticiasrionegro.com.ar/contenido/88152/el-curzas-unco-abrio-la-preinscripcion-2026-en-viedma-y-los-10-nodos-regionales").
  - *Oszlak, Oscar (2020).* _El Estado en la era exponencial: Tecnologías disruptivas y gestión pública._ Buenos Aires: Editorial INAP.
  - *Universidad Nacional del Comahue (1993/2023).* _Estatuto de la Universidad Nacional del Comahue (Ordenanza N° 470/1993 y modificatorias)._ Neuquén / Viedma.
  - *Marco Normativo Nacional:*
    - Constitución de la Nación Argentina (Art. 75, inc. 19).
    - Ley de Educación Superior N° 24.521.
    - Ley de Acceso a la Información Pública N° 27.275.
    - Ley de Repositorios Digitales Abiertos de Ciencia y Tecnología N° 26.899.
    - Ley de Administración Financiera del Sector Público Nacional N° 24.156.
    - Decretos N° 366/2006 y N° 1246/2015 (Convenios Colectivos de Trabajo Nodocente y Docente).
]


