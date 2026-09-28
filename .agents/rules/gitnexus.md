# 🕸️ GitNexus Workspace Rule — Inteligencia de Código y Control de Arquitectura

Este archivo define las directivas y pautas operativas obligatorias para el uso de **GitNexus** en este repositorio de **Planeamiento Organizacional / Planeamiento y Control de las Organizaciones (CURZAS - UNCo)**.

---

## 📌 1. Misión y Alcance de GitNexus en el Repositorio

GitNexus actúa como el **Cerebro Técnico y Arquitectural** del proyecto, complementando a NotebookLM (Cerebro Académico y Conceptual). Su función principal es:

1. **Gobernar la Arquitectura *Docs-as-Code*:** Indexar y mapear las dependencias entre el pipeline central de compilación (`compilar_todos.py`, `compilar_todos.ps1`), scripts auxiliares en Python (`plantillas_pdf/`, `tests/`), motores de maquetación, plantillas institucionales y módulos tipográficos en **Typst (`.typ`)** distribuidos en `Actividades/`.
2. **Protección del Pipeline de Maquetación y Compilación:** Salvaguardar la modularidad, estilos y estabilidad de los documentos (portadas, pie de página institucional, numeración dinámica, callouts, tablas y secciones modulares) ante cualquier refactorización o cambio estructural.
3. **Análisis de Impacto Previo (*Blast Radius*):** Garantizar que cualquier modificación en `compilar_todos.py`, componentes compartidos, variables de estilo o scripts no altere negativamente entregas previas ya aprobadas o en curso (`actividad_01`, `actividad_02`, etc.).

---

## 🛡️ 2. Reglas Operativas Obligatorias (Guardarraíles)

### ✅ Obligatorio (Always Do):
1. **Análisis de Impacto Antes de Editar:**
   - Antes de modificar cualquier función, script o módulo tipográfico compartido, ejecutar el análisis de impacto:
     ```powershell
     node .gitnexus/run.cjs impact "<nombreSimbolo>" --direction upstream --repo .
     ```
     *(o alternativamente: `npx gitnexus impact "<nombreSimbolo>" --direction upstream`)*
   - Evaluar los llamadores (*callers*), dependencias aguas arriba y nivel de riesgo (*risk*).
2. **Detección de Cambios en el Grafo Antes de Confirmar (Commit):**
   - Antes de realizar cualquier commit de código o refactorización estructural:
     ```powershell
     node .gitnexus/run.cjs detect-changes --scope all --repo .
     ```
   - Si se analiza regresión contra la rama principal:
     ```powershell
     node .gitnexus/run.cjs detect-changes --scope compare --base-ref "main" --repo .
     ```
3. **Gestión Rigurosa de Riesgos:**
   - Alertar inmediatamente si el análisis arroja riesgo **HIGH** o **CRITICAL**.
   - Tratar `risk: UNKNOWN` como advertencia no resuelta (requiere verificación manual adicional antes de continuar).
4. **Navegación Asistida por Grafo:**
   - Para explorar conceptos o arquitectura de los scripts/módulos:
     ```powershell
     node .gitnexus/run.cjs query "<concepto>" --repo .
     ```
   - Para inspeccionar un símbolo, función o componente específico:
     ```powershell
     node .gitnexus/run.cjs context "<nombreSimbolo>" --repo .
     ```

### ❌ Prohibido (Never Do):
1. **Nunca editar funciones, scripts o módulos compartidos a ciegas** sin previo análisis de impacto.
2. **Nunca renombrar símbolos o variables globales mediante búsqueda y reemplazo masivo (*find-and-replace*)** sin verificar el grafo de referencias.
3. **Nunca confirmar cambios (commit) en la infraestructura de compilación sin verificar `detect-changes`**.
4. **Nunca ignorar advertencias de riesgo alto** o romper compatibilidad entre los módulos de entregables.

---

## 🔄 3. Mantenimiento y Actualización del Índice

Si se incorporan nuevos módulos, scripts o cambios estructurales mayores:

* **Reindexar de forma rápida (solo índice):**
  ```powershell
  node .gitnexus/run.cjs analyze --index-only
  ```
* **Consultar estado actual del grafo:**
  ```powershell
  node .gitnexus/run.cjs status
  ```

---

## 🛠️ 4. Guía Rápida de Skills y Tareas de GitNexus

| Tarea Requerida | Skill de Referencia | Comando / Flujo |
| :--- | :--- | :--- |
| **Comprender arquitectura / "¿Cómo funciona X?"** | `.agents/skills/gitnexus-exploring/SKILL.md` | `node .gitnexus/run.cjs context "<simbolo>"` |
| **Radio de impacto / "¿Qué se rompe si toco X?"** | `.agents/skills/gitnexus-impact-analysis/SKILL.md` | `node .gitnexus/run.cjs impact "<simbolo>" --direction upstream` |
| **Diagnosticar fallas / "¿Por qué falla la compilación?"** | `.agents/skills/gitnexus-debugging/SKILL.md` | Rastreo de flujo y ejecución de pruebas controladas |
| **Refactorizar / modularizar scripts y plantillas** | `.agents/skills/gitnexus-refactoring/SKILL.md` | `node .gitnexus/run.cjs detect-changes --scope all` |
| **Referencia completa de comandos CLI** | `.agents/skills/gitnexus-cli/SKILL.md` | `node .gitnexus/run.cjs --help` |
