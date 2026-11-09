#import "../../config/estilos.typ": *
#import "../../components/cajas.typ": *

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

