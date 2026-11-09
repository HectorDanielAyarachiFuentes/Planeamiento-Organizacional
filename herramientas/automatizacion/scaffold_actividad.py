#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de Automatización Autónoma de Actividades y TPs
Planeamiento Organizacional — CURZAS / UNCo
===================================================
Genera en un solo paso y de forma 100% automatizada el andamiaje completo,
los módulos Typst, las plantillas visuales institucionales y la integración al
pipeline de compilación sin que el usuario deba ejecutar comandos ni scripts manuales.
"""

import sys
import argparse
import re
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent


def normalizar_numero(num_str):
    """Convierte '5', '05', 'actividad_5' en '05'."""
    clean = re.sub(r"[^\d]", "", str(num_str))
    if not clean:
        raise ValueError(f"Número de actividad inválido: '{num_str}'")
    return f"{int(clean):02d}"


def generar_slug(texto):
    """Genera un slug seguro para nombres de archivo."""
    slug = re.sub(r"[^\w\s-]", "", texto).strip()
    slug = re.sub(r"[-\s]+", "_", slug)
    return slug


def crear_directorios(num):
    """Crea la estructura reglamentaria de carpetas en Actividades/."""
    carpetas = [
        WORKSPACE_ROOT / "Actividades" / "consigna" / f"actividad_{num}",
        WORKSPACE_ROOT / "Actividades" / "material" / f"actividad_{num}",
        WORKSPACE_ROOT / "Actividades" / "avances" / f"actividad_{num}",
        WORKSPACE_ROOT / "Actividades" / "entregables" / f"actividad_{num}" / "modulos" / "secciones",
    ]
    for c in carpetas:
        c.mkdir(parents=True, exist_ok=True)
    return carpetas


def generar_archivos_typst(num, titulo, unidad):
    """Genera las plantillas modulares con estándares institucionales de cátedra."""
    entregable_dir = WORKSPACE_ROOT / "Actividades" / "entregables" / f"actividad_{num}"
    secciones_dir = entregable_dir / "modulos" / "secciones"
    
    slug_titulo = generar_slug(titulo)
    nombre_maestro = f"Avance_{num}_{slug_titulo}.typ"
    archivo_maestro = entregable_dir / nombre_maestro
    archivo_preview = entregable_dir / f"preview_actividad_{num}.typ"
    
    # 1. Sección de desarrollo modular (01_desarrollo.typ)
    seccion_desarrollo = secciones_dir / "01_desarrollo.typ"
    if not seccion_desarrollo.exists():
        contenido_desarrollo = f'''#import "/Actividades/entregables/actividad_02/modulos/config/estilos.typ": *
#import "/Actividades/entregables/actividad_02/modulos/components/cajas.typ": *

// ==============================================================================
// AVANCE {int(num)}: {titulo.upper()} ({unidad.upper()})
// ==============================================================================

#avance-banner(
  "AVANCE {int(num)}: {titulo}",
  "Diagnóstico y Aplicación Situada en el CURZAS (Universidad Nacional del Comahue)"
)

#block(
  width: 100%,
  stroke: (left: 3.5pt + primary, rest: 0.5pt + border-subtle),
  fill: bg-card,
  radius: (right: 4pt),
  inset: (x: 14pt, y: 9.5pt),
  [
    #text(weight: "bold", size: 8.8pt, fill: primary)[Ejes Temáticos y Objetivos de la Entrega ({unidad})]
    #v(3pt)
    #text(size: 8.3pt, fill: text-muted)[
      • *Marco Teórico-Conceptual:* Fundamentación según los autores de la cátedra. \\
      • *Diagnóstico Situacional:* Análisis empírico sobre la estructura y funcionamiento del CURZAS (Viedma y Nodos). \\
      • *Propuesta y Dictamen:* Lineamientos estratégicos y viabilidad organizacional.
    ]
  ]
)
#v(6pt)

== Eje 1: Desarrollo de la Consigna de Cátedra

=== A. Respuesta a la Pregunta Guía Oficial

#callout-pregunta[
  [Inserte aquí la consigna oficial provista por el equipo docente]
]

1. *Encuadre Teórico de Cátedra:*
  Desarrollo de los conceptos teóricos sustantivos aplicables al caso.

2. *Diagnóstico Situacional en el CURZAS:*
  Contraste y aplicación empírica en el ámbito del Complejo Universitario Regional Zona Atlántica y Sur.

#v(3pt)

#callout-dictamen("Dictamen Estratégico de la Actividad {int(num)}")[
  *Conclusión y Propuesta:* Síntesis analítica orientada a la toma de decisiones y al fortalecimiento de las capacidades institucionales.
]
'''
        seccion_desarrollo.write_text(contenido_desarrollo, encoding="utf-8")

    # 2. Sección de bibliografía modular (02_bibliografia.typ)
    seccion_biblio = secciones_dir / "02_bibliografia.typ"
    if not seccion_biblio.exists():
        contenido_biblio = f'''#import "/Actividades/entregables/actividad_02/modulos/config/estilos.typ": *
#import "/Actividades/entregables/actividad_02/modulos/components/cajas.typ": *

// ==============================================================================
// BIBLIOGRAFÍA Y FUENTES ACADÉMICAS CONSULTADAS (AVANCE {int(num)})
// ==============================================================================

#heading(level: 1, outlined: true, bookmarked: true)[Bibliografía]

#v(8pt)

#block(
  width: 100%,
  fill: bg-card,
  stroke: 0.5pt + border-subtle,
  radius: 6pt,
  inset: (x: 16pt, y: 14pt),
  breakable: true
)[
  #text(weight: "bold", size: 11pt, fill: primary)[Bibliografía y Fuentes Académicas Consultadas]
  #v(4pt)
  #line(length: 100%, stroke: 0.6pt + accent)
  #v(8pt)
  
  #set text(size: 8.2pt, fill: text-main)
  - *Universidad Nacional del Comahue (1993/2023).* _Estatuto de la Universidad Nacional del Comahue (Ordenanza N° 470/1993 y modificatorias)._ Neuquén / Viedma.
  - *Marco Normativo e Institucional de Referencia.*
]
'''
        seccion_biblio.write_text(contenido_biblio, encoding="utf-8")

    # 3. Archivo Preview Ultrarrápido (<0.2s)
    if not archivo_preview.exists():
        contenido_preview = f'''#import "/Actividades/entregables/actividad_02/modulos/config/estilos.typ": *
#import "/Actividades/entregables/actividad_02/modulos/components/cajas.typ": *

// ==============================================================================
// PREVIEW RÁPIDO: AVANCE {int(num)} — {titulo.upper()}
// ==============================================================================

#set page(
  paper: "a4",
  margin: (x: 2.3cm, top: 2.4cm, bottom: 2.4cm),
  header: [
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      text(size: 8pt, fill: text-muted)[Planeamiento y Control de las Organizaciones | CURZAS — Avance {int(num)}],
      text(size: 8pt, fill: primary, weight: "bold")[UNCo — CURZAS]
    )
    #v(3pt)
    #line(length: 100%, stroke: 0.5pt + border-line)
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

#include "modulos/secciones/01_desarrollo.typ"
#pagebreak()
#include "modulos/secciones/02_bibliografia.typ"
'''
        archivo_preview.write_text(contenido_preview, encoding="utf-8")

    # 4. Archivo Maestro Consolidado
    if not archivo_maestro.exists():
        contenido_maestro = f'''#import "/Actividades/entregables/actividad_02/modulos/config/estilos.typ": *
#import "/Actividades/entregables/actividad_02/modulos/components/cajas.typ": *

// ==============================================================================
// DOCUMENTO OFICIAL DEFINITIVO: AVANCE {int(num)} — {titulo.upper()}
// ==============================================================================

// 1. Portada Institucional
#include "/Actividades/entregables/actividad_02/modulos/secciones/00_portada.typ"

// 2. Numeración y Configuración de Página
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
    #v(3pt)
    #line(length: 100%, stroke: 0.5pt + border-line)
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

#include "modulos/secciones/01_desarrollo.typ"
#pagebreak()
#include "modulos/secciones/02_bibliografia.typ"
'''
        archivo_maestro.write_text(contenido_maestro, encoding="utf-8")

    return {
        "maestro_typ": archivo_maestro,
        "preview_typ": archivo_preview,
        "desarrollo_typ": seccion_desarrollo,
        "biblio_typ": seccion_biblio,
        "pdf_salida": entregable_dir / f"{archivo_maestro.stem}.pdf",
        "preview_pdf": entregable_dir / f"preview_actividad_{num}.pdf",
    }


def registrar_en_compilar_todos(num, titulo, archivos):
    """Inyecta la nueva actividad en el pipeline de compilar_todos.py de forma idempotente."""
    compilar_script = WORKSPACE_ROOT / "compilar_todos.py"
    contenido = compilar_script.read_text(encoding="utf-8")
    
    clave_act = f"actividad_{num}"
    if f'"{clave_act}":' in contenido:
        print(f"ℹ️ La actividad '{clave_act}' ya se encontraba registrada en compilar_todos.py.")
        return

    # Buscar el final del diccionario ENTREGABLES
    patron_entregables = r'(ENTREGABLES\s*=\s*\{[\s\S]*?)(\n\}\n)'
    match = re.search(patron_entregables, contenido)
    if not match:
        print("⚠️ No se pudo ubicar el diccionario ENTREGABLES en compilar_todos.py para inyección automática.")
        return

    nueva_entrada = f''',
    "{clave_act}": {{
        "nombre": "Actividad {int(num)} — Avance {int(num)}: {titulo} (CURZAS)",
        "entrada": WORKSPACE_ROOT / "Actividades" / "entregables" / "{clave_act}" / "{archivos['maestro_typ'].name}",
        "salidas": [
            WORKSPACE_ROOT / "Actividades" / "entregables" / "{clave_act}" / "{archivos['pdf_salida'].name}"
        ]
    }},
    "{clave_act}_preview": {{
        "nombre": "Actividad {int(num)} — Preview Rápido Avance {int(num)} (CURZAS)",
        "entrada": WORKSPACE_ROOT / "Actividades" / "entregables" / "{clave_act}" / "{archivos['preview_typ'].name}",
        "salidas": [
            WORKSPACE_ROOT / "Actividades" / "entregables" / "{clave_act}" / "{archivos['preview_pdf'].name}"
        ]
    }}'''

    nuevo_contenido = contenido[:match.end(1)] + nueva_entrada + contenido[match.start(2):]

    # Actualizar las opciones del parser si corresponde
    if f'"{clave_act}"' not in nuevo_contenido:
        nuevo_contenido = nuevo_contenido.replace(
            'choices=[',
            f'choices=["{clave_act}", "{clave_act}_preview", "{int(num)}", '
        )
        
    compilar_script.write_text(nuevo_contenido, encoding="utf-8")
    print(f"✅ Integrada la actividad '{clave_act}' en compilar_todos.py.")


def main():
    parser = argparse.ArgumentParser(description="Andamiaje automático de nuevas actividades académicas.")
    parser.add_argument("--numero", "-n", required=True, help="Número de actividad (ej. 5 o 05)")
    parser.add_argument("--titulo", "-t", default="Nuevo Avance Académico", help="Título temático de la actividad")
    parser.add_argument("--unidad", "-u", default="Unidad V", help="Unidad académica del programa")
    args = parser.parse_args()

    num = normalizar_numero(args.numero)
    crear_directorios(num)
    archivos = generar_archivos_typst(num, args.titulo, args.unidad)
    registrar_en_compilar_todos(num, args.titulo, archivos)

    print(f"\n🎉 Andamiaje completado exitosamente para la Actividad {num}!")
    print(f"   • Archivo de desarrollo: {archivos['desarrollo_typ'].relative_to(WORKSPACE_ROOT)}")
    print(f"   • Archivo de preview   : {archivos['preview_typ'].relative_to(WORKSPACE_ROOT)}")
    print(f"   • Archivo maestro final: {archivos['maestro_typ'].relative_to(WORKSPACE_ROOT)}")


if __name__ == "__main__":
    main()

