import xml.etree.ElementTree as ET
from pathlib import Path

svg_code = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 1015" width="100%" height="auto" font-family="Segoe UI, -apple-system, BlinkMacSystemFont, Roboto, sans-serif">
  <defs>
    <!-- Filtros de sombra -->
    <filter id="cardShadow" x="-3%" y="-3%" width="106%" height="108%">
      <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-opacity="0.08" />
    </filter>
    <filter id="blueShadow" x="-3%" y="-3%" width="106%" height="108%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#0284c7" flood-opacity="0.18" />
    </filter>
  </defs>

  <!-- Fondo blanco general -->
  <rect x="0" y="0" width="1400" height="1015" fill="#ffffff" />

  <!-- ========================================== -->
  <!-- 1. TÍTULO Y SUBTÍTULO GENERAL             -->
  <!-- ========================================== -->
  <text x="700" y="42" font-size="20" font-weight="bold" fill="#1e293b" letter-spacing="0.3" text-anchor="middle">COMPLEJO UNIVERSITARIO REGIONAL ZONA ATLÁNTICA Y SUR (CURZAS - UNCo)</text>
  <text x="700" y="66" font-size="12.5" font-weight="500" fill="#64748b" text-anchor="middle">Estructura Orgánico-Funcional Completa: Gobierno Colegiado, Conducción Ejecutiva, Gestión Sustantiva y Red Territorial</text>

  <!-- ========================================== -->
  <!-- 2. NIVEL DE GOBIERNO Y AUTORIDAD CENTRAL   -->
  <!-- ========================================== -->
  <!-- Box UNCo Central (Neuquén) -->
  <g filter="url(#cardShadow)">
    <rect x="130" y="90" width="255" height="72" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" />
    <path d="M 130 98 A 8 8 0 0 1 138 90 L 138 162 A 8 8 0 0 1 130 154 Z" fill="#334155" />
    <text x="152" y="114" font-size="10" font-weight="bold" fill="#64748b">UNCo CENTRAL (NEUQUÉN)</text>
    <text x="152" y="133" font-size="12.5" font-weight="bold" fill="#1e293b">Consejo Superior / Rectorado</text>
    <text x="152" y="149" font-size="9.5" fill="#64748b">Servidores Mapuche / Marco Salarial</text>
  </g>

  <!-- Línea conectora punteada UNCo Central <-> Consejo Directivo -->
  <line x1="385" y1="126" x2="540" y2="126" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4" />

  <!-- Box Órgano Deliberativo Colegiado: CONSEJO DIRECTIVO -->
  <g filter="url(#cardShadow)">
    <rect x="540" y="85" width="320" height="72" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
    <text x="700" y="106" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle" letter-spacing="0.5">ÓRGANO DELIBERATIVO COLEGIADO</text>
    <text x="700" y="128" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">CONSEJO DIRECTIVO (CURZAS)</text>
    <text x="700" y="145" font-size="9" fill="#94a3b8" text-anchor="middle">Claustros: Docentes, Nodocentes, Estudiantes, Graduados</text>
  </g>

  <!-- Línea continua de mando CD -> Decanato -->
  <line x1="700" y1="157" x2="700" y2="182" stroke="#64748b" stroke-width="2" />

  <!-- ========================================== -->
  <!-- 3. CONDUCCIÓN EJECUTIVA Y STAFF           -->
  <!-- ========================================== -->
  <!-- Box DECANATO Y VICEDECANATO -->
  <g filter="url(#blueShadow)">
    <rect x="540" y="182" width="320" height="105" rx="8" fill="#0284c7" stroke="#0369a1" stroke-width="1.5" />
    <text x="700" y="209" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">DECANATO</text>
    <text x="700" y="231" font-size="11.5" font-weight="500" fill="#ffffff" text-anchor="middle">Decana: Dra. Adriana Goicochea</text>
    <text x="700" y="253" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">VICEDECANATO</text>
    <text x="700" y="272" font-size="11.5" font-weight="500" fill="#ffffff" text-anchor="middle">Vicedecana: Mg. Cecilia Camera</text>
  </g>

  <!-- Línea punteada hacia Staff Asesor -->
  <line x1="860" y1="235" x2="1005" y2="235" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4" />

  <!-- Box Órganos Asesores / Staff -->
  <g filter="url(#cardShadow)">
    <rect x="1005" y="200" width="260" height="70" rx="8" fill="#ffffff" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4" />
    <text x="1135" y="222" font-size="9.5" font-weight="bold" fill="#0284c7" text-anchor="middle" letter-spacing="0.4">ÓRGANOS ASESORES / STAFF</text>
    <text x="1135" y="242" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Asesoría Legal y Despacho</text>
    <text x="1135" y="258" font-size="9.5" fill="#64748b" text-anchor="middle">Comisión Paritaria Particular (COPAR)</text>
  </g>

  <!-- Troncal distribuidor vertical y horizontal hacia las 5 Secretarías -->
  <line x1="700" y1="287" x2="700" y2="330" stroke="#64748b" stroke-width="2" />
  <line x1="180" y1="330" x2="1220" y2="330" stroke="#64748b" stroke-width="2" />

  <!-- Bajadas a las 5 Secretarías -->
  <line x1="180" y1="330" x2="180" y2="365" stroke="#64748b" stroke-width="2" />
  <line x1="440" y1="330" x2="440" y2="365" stroke="#64748b" stroke-width="2" />
  <line x1="700" y1="330" x2="700" y2="365" stroke="#64748b" stroke-width="2" />
  <line x1="960" y1="330" x2="960" y2="365" stroke="#64748b" stroke-width="2" />
  <line x1="1220" y1="330" x2="1220" y2="365" stroke="#64748b" stroke-width="2" />

  <!-- ========================================== -->
  <!-- 4. CINCO SECRETARÍAS / DIRECCIONES         -->
  <!-- ========================================== -->
  <!-- 1. Secretaría Académica -->
  <g filter="url(#cardShadow)" transform="translate(65, 365)">
    <rect x="0" y="0" width="230" height="102" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1.2" />
    <path d="M 0 6 A 6 6 0 0 1 6 0 L 224 0 A 6 6 0 0 1 230 6 L 230 32 L 0 32 Z" fill="#0284c7" />
    <text x="115" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Secretaría Académica</text>
    <text x="115" y="54" font-size="11.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Mg. Alba Eterovich</text>
    <text x="115" y="73" font-size="9" fill="#64748b" text-anchor="middle">Planes de Estudio • Concursos</text>
    <text x="115" y="89" font-size="9" fill="#64748b" text-anchor="middle">Coordinación Curricular</text>
  </g>

  <!-- 2. Sec. de Ciencia y Técnica -->
  <g filter="url(#cardShadow)" transform="translate(325, 365)">
    <rect x="0" y="0" width="230" height="102" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.2" />
    <path d="M 0 6 A 6 6 0 0 1 6 0 L 224 0 A 6 6 0 0 1 230 6 L 230 32 L 0 32 Z" fill="#0f172a" />
    <text x="115" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Sec. de Ciencia y Técnica</text>
    <text x="115" y="54" font-size="11.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Esp. Lucrecia Avilés</text>
    <text x="115" y="73" font-size="9" fill="#64748b" text-anchor="middle">Proyectos PI / PIN • CIT R.N.</text>
    <text x="115" y="89" font-size="9" fill="#64748b" text-anchor="middle">Posgrados y Becas Científicas</text>
  </g>

  <!-- 3. Sec. de Extensión Univ. -->
  <g filter="url(#cardShadow)" transform="translate(585, 365)">
    <rect x="0" y="0" width="230" height="102" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1.2" />
    <path d="M 0 6 A 6 6 0 0 1 6 0 L 224 0 A 6 6 0 0 1 230 6 L 230 32 L 0 32 Z" fill="#0284c7" />
    <text x="115" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Sec. de Extensión Univ.</text>
    <text x="115" y="54" font-size="11.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Esp. Mónica Amado</text>
    <text x="115" y="73" font-size="9" fill="#64748b" text-anchor="middle">Vinculación Territorial • Pasantías</text>
    <text x="115" y="89" font-size="9" fill="#64748b" text-anchor="middle">Convenios Municipales y Cultura</text>
  </g>

  <!-- 4. Sec. Bienestar Estudiantil -->
  <g filter="url(#cardShadow)" transform="translate(845, 365)">
    <rect x="0" y="0" width="230" height="102" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.2" />
    <path d="M 0 6 A 6 6 0 0 1 6 0 L 224 0 A 6 6 0 0 1 230 6 L 230 32 L 0 32 Z" fill="#0f172a" />
    <text x="115" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Sec. Bienestar Estudiantil</text>
    <text x="115" y="54" font-size="11.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Esp. Carlos Comolay</text>
    <text x="115" y="73" font-size="9" fill="#64748b" text-anchor="middle">Becas • Residencias • Deportes</text>
    <text x="115" y="89" font-size="9" fill="#64748b" text-anchor="middle">Salud Integral y Género</text>
  </g>

  <!-- 5. Dir. Gestión Administrativa -->
  <g filter="url(#cardShadow)" transform="translate(1105, 365)">
    <rect x="0" y="0" width="230" height="102" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1.2" />
    <path d="M 0 6 A 6 6 0 0 1 6 0 L 224 0 A 6 6 0 0 1 230 6 L 230 32 L 0 32 Z" fill="#0284c7" />
    <text x="115" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Dir. Gestión Administrativa</text>
    <text x="115" y="54" font-size="11.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Mg. Fabián Fernandez</text>
    <text x="115" y="73" font-size="9" fill="#64748b" text-anchor="middle">Presupuesto • Compras • RRHH</text>
    <text x="115" y="89" font-size="9" fill="#64748b" text-anchor="middle">Mesa General e Infraestructura</text>
  </g>

  <!-- ========================================== -->
  <!-- LÍNEAS DE CONEXIÓN A NIVEL OPERATIVO      -->
  <!-- ========================================== -->
  <!-- Sec. Académica -> Departamentos I y II -->
  <line x1="180" y1="467" x2="180" y2="500" stroke="#64748b" stroke-width="1.8" />
  <line x1="180" y1="500" x2="550" y2="500" stroke="#64748b" stroke-width="1.8" />
  <line x1="220" y1="500" x2="220" y2="530" stroke="#64748b" stroke-width="1.8" />
  <line x1="550" y1="500" x2="550" y2="530" stroke="#64748b" stroke-width="1.8" />

  <!-- Sec. de Extensión -> Red Territorial (Línea naranja punteada) -->
  <line x1="700" y1="467" x2="700" y2="767" stroke="#d97706" stroke-width="2.2" stroke-dasharray="5,4" />

  <!-- Sec. Bienestar y Dir. Gestión Adm -> Servicios y Documentación -->
  <line x1="960" y1="467" x2="960" y2="505" stroke="#64748b" stroke-width="1.8" />
  <line x1="1220" y1="467" x2="1220" y2="505" stroke="#64748b" stroke-width="1.8" />
  <line x1="872" y1="505" x2="1220" y2="505" stroke="#64748b" stroke-width="1.8" />
  <line x1="872" y1="505" x2="872" y2="530" stroke="#64748b" stroke-width="1.8" />

  <!-- Dir. Gestión Adm -> Dirección de Personal (Línea directa) -->
  <line x1="1190" y1="505" x2="1190" y2="530" stroke="#64748b" stroke-width="1.8" />

  <!-- ========================================== -->
  <!-- 5. CUATRO BLOQUES OPERATIVOS Y DE GESTIÓN  -->
  <!-- ========================================== -->
  <!-- Box 1: DEPARTAMENTOS ACADÉMICOS (I) -->
  <g filter="url(#cardShadow)">
    <rect x="65" y="530" width="310" height="205" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" />
    <text x="80" y="555" font-size="10.5" font-weight="bold" fill="#475569">DEPARTAMENTOS ACADÉMICOS (I)</text>
    
    <text x="80" y="580" font-size="10" font-weight="bold" fill="#1e293b">• Dpto. de Administración Pública</text>
    <text x="90" y="596" font-size="8.5" fill="#64748b">(Lic. en RRHH, Lic. Adm. Pública, Tecnicaturas)</text>

    <text x="80" y="622" font-size="10" font-weight="bold" fill="#1e293b">• Dpto. de Psicopedagogía</text>
    <text x="90" y="638" font-size="8.5" fill="#64748b">(Licenciatura y Profesorado)</text>

    <text x="80" y="666" font-size="10" font-weight="bold" fill="#1e293b">• Dpto. de Lengua, Literatura y Comunicación</text>

    <text x="80" y="696" font-size="10" font-weight="bold" fill="#1e293b">• Dpto. de Estudios Políticos</text>
  </g>

  <!-- Box 2: DEPARTAMENTOS Y COORDINACIONES (II) -->
  <g filter="url(#cardShadow)">
    <rect x="395" y="530" width="310" height="205" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" />
    <text x="410" y="555" font-size="10.5" font-weight="bold" fill="#475569">DEPARTAMENTOS Y COORDINACIONES (II)</text>
    
    <text x="410" y="580" font-size="10" font-weight="bold" fill="#1e293b">• Dpto. de Ciencia y Tecnología</text>

    <text x="410" y="610" font-size="10" font-weight="bold" fill="#1e293b">• Dpto. de Gestión Agropecuaria</text>

    <text x="410" y="640" font-size="10" font-weight="bold" fill="#1e293b">• Coordinación Carrera de Enfermería</text>

    <text x="410" y="670" font-size="10" font-weight="bold" fill="#1e293b">• Dirección de Alumnos y Asuntos Estudiantiles</text>
    <text x="420" y="686" font-size="8.5" fill="#64748b">(Gestión de Actas y Matrículas en SIU-Guaraní)</text>
  </g>

  <!-- Box 3: SERVICIOS Y DOCUMENTACIÓN -->
  <g filter="url(#cardShadow)">
    <rect x="725" y="530" width="295" height="205" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" />
    <text x="740" y="555" font-size="10.5" font-weight="bold" fill="#475569">SERVICIOS Y DOCUMENTACIÓN</text>
    
    <text x="740" y="580" font-size="10" font-weight="bold" fill="#1e293b">• Dirección de Biblioteca Central</text>
    <text x="750" y="596" font-size="8.5" fill="#64748b">(Centros de Documentación e ISBN)</text>

    <text x="740" y="622" font-size="10" font-weight="bold" fill="#1e293b">• Dirección de Despacho y Mesa General</text>
    <text x="750" y="638" font-size="8.5" fill="#64748b">(Recepción, Folios, Trámites SUDOCU)</text>

    <text x="740" y="666" font-size="10" font-weight="bold" fill="#1e293b">• Mantenimiento y Servicios Generales</text>

    <text x="740" y="696" font-size="10" font-weight="bold" fill="#1e293b">• Informática y Soporte Tecnológico Local</text>
  </g>

  <!-- Box 4: DIRECCIÓN DE PERSONAL (RRHH) - HIGHLIGHTED -->
  <g filter="url(#blueShadow)">
    <rect x="1045" y="530" width="290" height="205" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="2" />
    <path d="M 1045 538 A 8 8 0 0 1 1053 530 L 1327 530 A 8 8 0 0 1 1335 538 L 1335 562 L 1045 562 Z" fill="#0284c7" />
    <text x="1190" y="551" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">DIRECCIÓN DE PERSONAL (RRHH)</text>
    
    <text x="1060" y="580" font-size="9.5" font-weight="bold" fill="#0284c7">Área Clave de Flujograma y GDE:</text>
    <text x="1060" y="600" font-size="9.5" font-weight="bold" fill="#1e293b">• Administración de Legajos (Doc/Nodoc)</text>
    <text x="1060" y="622" font-size="9.5" font-weight="bold" fill="#1e293b">• Control de Asistencia y Partes Médicos</text>
    <text x="1060" y="644" font-size="9.5" font-weight="bold" fill="#1e293b">• Carga de Novedades Salariales</text>
    <text x="1070" y="660" font-size="8.5" fill="#64748b">(Interfaz SUDOCU -> SIU-Mapuche)</text>
    <text x="1060" y="682" font-size="9.5" font-weight="bold" fill="#1e293b">• Articulación con Salud Ocupacional</text>
    <text x="1070" y="698" font-size="8.5" fill="#64748b">(Juntas Médicas y CCT 366/06 y 1246/15)</text>
  </g>

  <!-- ========================================== -->
  <!-- 6. RED TERRITORIAL EMERGENTE: 10 NODOS     -->
  <!-- ========================================== -->
  <g>
    <!-- Marco contenedor punteado en naranja -->
    <rect x="230" y="780" width="940" height="175" rx="10" fill="#fffdfa" stroke="#d97706" stroke-width="2" stroke-dasharray="6,4" />
    
    <!-- Pastilla / Píldora de encabezado -->
    <rect x="520" y="767" width="360" height="26" rx="13" fill="#d97706" />
    <text x="700" y="784" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="0.3">ESTRUCTURA REAL EMERGENTE: RED TERRITORIAL</text>

    <!-- Textos explicativos -->
    <text x="700" y="815" font-size="12" font-weight="bold" fill="#9a3412" text-anchor="middle">Coordinación de Educación a Distancia y Nodos Regionales (Res. CD N° 135/2022)</text>
    <text x="700" y="835" font-size="9.5" fill="#c2410c" text-anchor="middle">Despliegue territorial de facto no tipificado plenamente en el escalafón central del Consejo Superior. Opera mediante convenios de cogestión con Municipios.</text>

    <!-- Fila 1 de Nodos (5 localidades) -->
    <g transform="translate(275, 852)">
      <rect x="0" y="0" width="155" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="77" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">Los Menucos</text>

      <rect x="170" y="0" width="155" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="247" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">Sierra Colorada</text>

      <rect x="340" y="0" width="170" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="425" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">Valcheta</text>

      <rect x="525" y="0" width="155" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="602" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">Ramos Mexía</text>

      <rect x="695" y="0" width="155" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="772" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">San Antonio Oeste</text>
    </g>

    <!-- Fila 2 de Nodos (4 localidades) -->
    <g transform="translate(355, 894)">
      <rect x="0" y="0" width="160" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="80" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">General Conesa</text>

      <rect x="175" y="0" width="160" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="255" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">Lamarque</text>

      <rect x="350" y="0" width="160" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="430" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">Maquinchao</text>

      <rect x="525" y="0" width="165" height="30" rx="6" fill="#fef3c7" stroke="#fde68a" />
      <text x="607" y="19" font-size="9.5" font-weight="600" fill="#78350f" text-anchor="middle">Comallo / Sierra Grande</text>
    </g>
  </g>

  <!-- ========================================== -->
  <!-- 7. PIE DE PÁGINA: REFERENCIAS Y FUENTE     -->
  <!-- ========================================== -->
  <text x="65" y="985" font-size="9.5" fill="#64748b">Referencias: Línea continua = Jerarquía y dependencia formal (Estatuto UNCo Ord. 470/93). Línea punteada = Staff / Asesoría y Convenios de Red (Hintze, 2001).</text>
  <text x="1335" y="985" font-size="9.5" fill="#64748b" text-anchor="end">Fuente: Elaboración propia en base a datos institucionales y Res. CD CURZAS.</text>
</svg>'''

ET.fromstring(svg_code)
print("VALID XML!")

target1 = Path("Actividades/material/actividad_03/organigrama.svg")
target2 = Path("assets/img/organigrama.svg")

target1.write_text(svg_code, encoding="utf-8")
print(f"Updated {target1}")

target2.write_text(svg_code, encoding="utf-8")
print(f"Updated {target2}")
