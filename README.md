# 🏛️ Planeamiento Organizacional — CURZAS (UNCo)

Repositorio institucional y académico para la materia **Planeamiento y Control de las Organizaciones** (Planeamiento Organizacional) en el **Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)** de la **Universidad Nacional del Comahue (UNCo)**.

---

## 👤 Información del Proyecto

* **Institución:** Universidad Nacional del Comahue (UNCo) — CURZAS
* **Materia:** Planeamiento y Control de las Organizaciones / Planeamiento Organizacional
* **Autor / Alumno:** Héctor Daniel Ayarachi Fuentes
* **Metodología:** *Docs-as-Code* (Documentación técnica y académica estructurada como código)
* **Motor Tipográfico:** [Typst](https://typst.app/) & Python

---

## 📂 Arquitectura del Repositorio

```text
Planeamiento Organizacional/
├── .agents/                 # Configuración y reglas operativas para IA/asistentes
│   └── rules/
│       └── AGENTS.md        # Estándares, diseño institucional y flujo de trabajo
├── assets/                  # Recursos gráficos e imágenes
│   └── img/                 # Escudo y logotipos institucionales (CURZAS.png)
├── plantillas_pdf/          # Motores de renderizado y plantillas reutilizables
│   ├── 1_typst/             # Plantillas base en Typst y scripts de compilación
│   ├── 2_playwright_html/   # Motor alternativo HTML / Playwright
│   ├── 3_pymupdf_editor/    # Motor de manipulación y anotación PyMuPDF
│   ├── 4_fpdf2/             # Motor alternativo FPDF2
├── herramientas/            # Herramientas y utilidades complementarias
│   └── notebooklm/          # Entorno, guías y utilidades para NotebookLM MCP
│       ├── docs/            # Documentación y guías técnicas de integración
│       ├── scripts/         # Herramientas de autenticación y soporte (auth_helper.py)
│       └── tutoriales/      # Video tutoriales y transcripciones operativas
├── tareas/                  # Gestión modular de actividades y trabajos prácticos
│   ├── README.md            # Índice general y estado de entregas
│   └── actividad_01/        # Estructura modular por actividad
│       ├── README.md        # Resumen y objetivos del módulo
│       ├── consigna/        # Consignas oficiales y pautas de la cátedra (.docx, .pdf)
│       ├── material/        # Bibliografía, lecturas teóricas y artículos de referencia
│       ├── avances/         # Código fuente (.typ), borradores y scripts de maquetación
│       └── entregables/     # Versión definitiva lista para entrega (.pdf, .typ)
├── pruebas/                 # Zona de aislamiento para procesamiento y scripts temporales
└── tests/                   # Pruebas automatizadas de compilación y validación
```

---

## 🚀 Compilación de Documentos Typst

Para compilar cualquier archivo `.typ` a PDF de manera directa:

```powershell
# Compilación directa usando typst CLI
typst compile "tareas/actividad_01/avances/avance_1_typst.typ" "tareas/actividad_01/entregables/Avance_1.pdf"

# O mediante el wrapper de Python
python -c "import typst; typst.compile('tareas/actividad_01/avances/avance_1_typst.typ', output='tareas/actividad_01/entregables/Avance_1.pdf')"
```

---

## 🎨 Identidad Visual y Estándar de Documentos

* **Tipografía:** *Segoe UI* / *Arial* con espaciado optimizado.
* **Paleta de Colores:**
  * **Primario (Azul Marino / Institucional):** `#0f2d59` / `#0e6873`
  * **Acento (Dorado Elegante):** `#c89632`
  * **Texto Principal:** `#1f2937` / `#24292f`
  * **Fondos de Tarjetas / Callouts:** `#f8fafc`
* **Carátula & Paginación:** Portada sobria con logotipo oficial de CURZAS y paginación `Página X de Y` a partir de la segunda página.
