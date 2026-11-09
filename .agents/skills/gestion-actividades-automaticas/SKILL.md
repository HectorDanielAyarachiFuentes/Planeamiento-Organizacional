---
name: gestion-actividades-automaticas
description: Protocolo de inicio, resolución y compilación 100% autónoma de nuevas actividades y trabajos prácticos en Docs-as-Code para Planeamiento Organizacional (CURZAS - UNCo). Usar automáticamente ante cualquier mención de una nueva actividad sin requerir intervención técnica del usuario.
---

# 🤖 Protocolo Autónomo de Gestión de Nuevas Actividades (Docs-as-Code)

Este skill define la directiva operativa obligatoria para que el agente inicie, desarrolle, maquete y compile de forma **100% autónoma** cualquier nueva actividad o entrega académica solicitada por el usuario, sin que este deba ejecutar scripts, comandos de terminal o configurar archivos manualmente.

---

## ⚡ Flujo de Ejecución Autónomo (Zero-Friction)

Cuando el usuario indique frases como:
- *"Hacemos la actividad 5"*
- *"Empecemos el nuevo TP"*
- *"Acá está la consigna de la actividad 6: [...]"*

El agente ejecuta de inmediato los siguientes pasos **sin pedirle al usuario que corra ningún script**:

### Paso 1: Andamiaje Instantáneo (Scaffolding Autónomo)
El agente ejecuta internamente:
```powershell
python herramientas/automatizacion/scaffold_actividad.py --numero <XX> --titulo "<Título>" --unidad "<Unidad>"
```
Esto genera en menos de 1 segundo:
1. Directorios oficiales: `consigna/`, `material/`, `avances/`, `entregables/`.
2. Módulos Typst: `01_desarrollo.typ`, `02_bibliografia.typ`, `preview_actividad_XX.typ` y el archivo maestro.
3. Registro automático en `compilar_todos.py` y `compilar_todos.ps1`.

### Paso 2: Análisis de Consigna y Material Local (NotebookLM solo a pedido)
1. Si el usuario adjunta un archivo (`.docx`, `.pdf`), el agente extrae las consignas a `Actividades/consigna/actividad_XX/`.
2. **Procesamiento Local por Defecto:** El análisis conceptual y la fundamentación teórica se realizan de forma local a partir de la bibliografía en `Actividades/material/actividad_XX/` y las capacidades de razonamiento directo de la IA.
3. **NotebookLM MCP (Opcional / A Solicitud):** Solo se interactúa con el servidor de NotebookLM si el usuario lo indica explícitamente en su mensaje (ej. *"consultá la libreta de NotebookLM"* o *"buscá esto en NotebookLM"*).

### Paso 3: Redacción Modular según la Fórmula de Cátedra
El agente redacta el contenido en `Actividades/entregables/actividad_XX/modulos/secciones/01_desarrollo.typ` asegurando la estructura obligatoria de 4 componentes:
1. `#callout-pregunta[...]`: Pregunta oficial de la consigna.
2. **Encuadre Teórico:** Autores de cátedra (Makon, Schweinheim, Matus, Cao, Blutman, etc.).
3. **Diagnóstico Situacional:** Datos empíricos del CURZAS (Viedma y los 10 nodos territoriales).
4. **Matriz / Tabla Comparativa:** Resumen analítico visual.
5. `#callout-dictamen[...]`: Conclusión institucional orientada a la gestión pública.

### Paso 4: Compilación y Entrega Definitiva
1. El agente compila el preview ultrarrápido (0,2s):
   ```powershell
   python compilar_todos.py -t actividad_XX_preview
   ```
2. El agente compila el documento oficial maestro:
   ```powershell
   python compilar_todos.py -t actividad_XX
   ```
3. Verifica la integridad visual y la paginación con PyMuPDF.
4. Presenta al usuario el enlace clickeable directo al PDF final listo para presentar.

