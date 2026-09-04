# 🤖 Reglas de Comportamiento del Agente (Agent Rules)

Este archivo define la estructura, estándares y pautas operativas obligatorias para cualquier IA o asistente que trabaje en este repositorio.

---

## 🏛️ 1. Contexto del Proyecto
* **Materia:** Planeamiento Organizacional / Planeamiento y Control de las Organizaciones.
* **Institución:** Complejo Universitario Regional Zona Atlántica y Sur (CURZAS) — Universidad Nacional del Comahue (UNCo).
* **Autor / Alumno:** Héctor Daniel Ayarachi Fuentes.
* **Enfoque técnico:** *Docs-as-Code* (documentación técnica gestionada como código), automatización con Python y composición tipográfica profesional con **Typst**.

---

## 📂 2. Estructura de Directorios Obligatoria

```text
Planeamiento Organizacional/
├── .agents/
│   ├── rules/
│   │   ├── AGENTS.md        # Reglas operativas y estándares para el agente
│   │   ├── notebooklm.md    # Reglas operativas para NotebookLM MCP
│   │   └── supreme_guidelines.md # Pautas de diseño y estética
│   ├── skills/              # Skills de workspace (using-notebooklm-mcp)
│   └── mcp_config.json      # Configuración de servidores MCP
├── assets/                  # Recursos gráficos y multimedia
│   └── img/                 # Logotipos institucionales (CURZAS.png)
├── plantillas_pdf/          # Motores de exportación y plantillas reutilizables
│   ├── 1_typst/             # Sistema Typst, plantillas base y scripts de generación
│   ├── 2_playwright_html/   # Motor alternativo HTML / Playwright
│   ├── 3_pymupdf_editor/    # Motor de edición y anotación PyMuPDF
│   └── 4_fpdf2/             # Motor alternativo FPDF2
├── pruebas/                 # Zona de aislamiento para pruebas, procesamiento y scripts temporales
├── herramientas/            # Herramientas y utilidades complementarias
│   └── notebooklm/          # Entorno, guías y utilidades para NotebookLM MCP
│       ├── docs/            # Documentación y guías de configuración
│       ├── scripts/         # Herramientas de autenticación y soporte (auth_helper.py)
│       └── tutoriales/      # Material audiovisual y transcripciones
├── tareas/                  # Carpeta principal de actividades y trabajos prácticos
│   ├── README.md            # Índice general y estado de actividades
│   └── actividad_01/        # Estructura modular por actividad (actividad_01, actividad_02, etc.)
│       ├── README.md        # Resumen del módulo
│       ├── consigna/        # Consignas oficiales y pautas de cátedra (.docx, .pdf)
│       ├── material/        # Bibliografía y lecturas de referencia (PDFs de cátedra)
│       ├── avances/         # Borradores, código (.typ, .py) y versiones en desarrollo
│       └── entregables/     # ÚNICA FUENTE DE LA VERDAD para versiones finales (.pdf, .typ)
└── tests/                   # Pruebas automatizadas de compilación y validación
```

---

## 🔄 3. Flujo de Trabajo para Actividades y Tareas

Para cada nueva actividad o trabajo práctico (`actividad_XX`):
1. **Consigna:** Documento oficial o pautas provistas por los docentes en `tareas/actividad_XX/consigna/`.
2. **Material:** Bibliografía de lectura o insumos teóricos en `tareas/actividad_XX/material/`.
3. **Desarrollo / Avances:** Borradores, scripts de maquetación y archivos `.typ` de trabajo en `tareas/actividad_XX/avances/`.
4. **Entregables Finales:** El archivo `.pdf` definitivo (y su correspondiente `.typ` consolidado) compilado en `tareas/actividad_XX/entregables/`.

---

## 📄 4. Estándar para Documentos y Reportes (Typst)

1. **Formato Principal:** Todas las entregas académicas, informes y reportes deben redactarse en **Typst (`.typ`)** y compilarse a **PDF (`.pdf`)**.
2. **Sincronización:** Cada vez que se cree o edite un archivo `.typ`, se debe compilar y actualizar su `.pdf` correspondiente en la carpeta `entregables/` de la actividad respectiva.
3. **Estilo Visual e Institucional:**
   * **Tipografía:** *Segoe UI* o *Arial*, tamaño base `9.5pt` a `10pt`, interlineado `0.65em` a `0.7em`.
   * **Paleta de Colores:**
     * **Primario (Azul Marino / Institucional):** `#0f2d59` / `#0e6873`
     * **Acento / Destacados:** `#c89632` (Dorado elegante) / `#c65911`
     * **Texto Principal:** `#1f2937` / `#24292f`
     * **Texto Secundario / Metadatos:** `#6b7280` / `#787878`
     * **Fondos de Cajas / Callouts:** `#f8fafc` / `#f2f7f7`
     * **Bordes Sutiles:** `#e2e8f0`
   * **Componentes:**
     * Cajas destacadas (`callout`) con barra lateral en color primario y fondo neutro suave.
     * Tablas estilizadas con cabecera en color primario y texto blanco.
     * Encabezados con decoradores visuales sutiles.
4. **Fidelidad al Contenido y Rigor Teórico:** Respetar los conceptos organizacionales, marcos teóricos de la cátedra (Oszlak, Cao, Mintzberg, etc.) y las consignas provistas.
5. **Carátula y Paginación Obligatoria:**
   * **Carátula / Portada:** Todo documento debe incluir una portada inicial con:
     * Nombre de la Institución: *Universidad Nacional del Comahue — CURZAS*.
     * Materia: *Planeamiento y Control de las Organizaciones* / *Planeamiento Organizacional*.
     * Título y subtítulo de la actividad.
     * Nombre del autor: **Héctor Daniel Ayarachi Fuentes**.
     * Fecha de entrega / actualización.
   * **Sin Numeración en Portada:** La carátula no debe mostrar encabezado ni número de página (`header: none, footer: none`).
   * **Numeración desde la 2ª Página:** La numeración de páginas debe figurar visible a partir de la segunda página (cuerpo del documento) con el formato `Página X de Y`.
6. **Integración Obligatoria del Logotipo de CURZAS (`assets/img/CURZAS.png`):**
   * **En la Carátula:** Debe figurar el logotipo oficial en tamaño grande y destacado en la portada (`width: 110pt` a `140pt`).
   * **En el Pie de Página:** Debe incluirse en el centro del pie de página, entre el texto informativo de la izquierda y la numeración de la derecha, en tamaño reducido pero nítido y visible (`height: 12pt` a `15pt`).

---

## 🧹 5. Higiene y Mantenimiento del Repositorio

* **Prohibido ensuciar la raíz:** Nunca crear scripts temporales, volcados de texto o archivos de prueba (`test_*.py`, `temp_*.typ`, `dump.txt`) en el directorio raíz.
* **Uso de `pruebas/` y `tests/`:** Cualquier prueba intermedia, script desechable o procesamiento de datos debe ubicarse en `pruebas/` o `tests/`.
* **Uso de librerías:** Usar las librerías instaladas en el entorno Python (`import typst`) sin duplicar ejecutables binarios pesados en carpetas de trabajo.

---

## 💬 6. Comunicación y Respuestas

* **Idioma:** Español neutro/argentino, profesional y pedagógico.
* **Concisión:** Explicaciones claras, enlaces directos a archivos (`[nombre](file:///...)`) y confirmación de compilaciones exitosas.

---

## 🏷️ 7. Mensajes de Confirmación y Control de Versiones (Git Commits)

* **Idioma Obligatorio:** Todos los mensajes de commit generados o propuestos deben redactarse exclusivamente en **español**.
* **Estándar:** Utilizar el formato *Conventional Commits*:
  * `feat:` para nuevas características, documentos o entregables.
  * `fix:` para correcciones de errores, sintaxis o inconsistencias.
  * `docs:` para actualizaciones de documentación, bibliografía o consignas.
  * `refactor:` para reestructuración de archivos, renombrado o mejoras de maquetación.
  * `test:` para scripts de validación, pruebas o compilación.
  * `chore:` para tareas de mantenimiento, configuración o limpieza.
* **Estructura y Tono:** Claros, descriptivos, en minúsculas y sin punto final en la primera línea.

