#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pipeline Central de Compilación Docs-as-Code — Planeamiento Organizacional (CURZAS - UNCo)
========================================================================================
Compila y sincroniza de forma unificada los documentos académicos en Typst (.typ) 
hacia sus correspondientes entregables en PDF (.pdf) en Actividades/entregables/.
"""

import os
import sys
import time
import argparse
from pathlib import Path

try:
    import typst
except ImportError:
    print("❌ Error: La librería 'typst' no está instalada en el entorno de Python.")
    print("   Instalar con: pip install typst")
    sys.exit(1)


WORKSPACE_ROOT = Path(__file__).resolve().parent

# Configuración de los entregables del repositorio
ENTREGABLES = {
    "actividad_01": {
        "nombre": "Actividad 1 — Avance 1: Contexto, Modelo de Gestión y Gobernanza (CURZAS)",
        "entrada": WORKSPACE_ROOT / "Actividades" / "entregables" / "actividad_01" / "Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.typ",
        "salidas": [
            WORKSPACE_ROOT / "Actividades" / "entregables" / "actividad_01" / "Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf"
        ]
    },
    "actividad_02": {
        "nombre": "Actividad 2 — Avance 2: Modelo de Gestión, Gobernanza y Poligobernanza (CURZAS)",
        "entrada": WORKSPACE_ROOT / "Actividades" / "entregables" / "actividad_02" / "modulos" / "Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Correccion.typ",
        "salidas": [
            WORKSPACE_ROOT / "Actividades" / "entregables" / "actividad_02" / "Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Correccion.pdf",
            WORKSPACE_ROOT / "Actividades" / "entregables" / "actividad_02" / "Avance_2_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi.pdf"
        ]
    }
}


def verificar_recursos():
    """Valida la existencia de recursos estáticos críticos antes de compilar."""
    logo = WORKSPACE_ROOT / "assets" / "img" / "CURZAS.png"
    if not logo.exists():
        print(f"⚠️ Advertencia: Logotipo institucional no encontrado en: {logo}")
        return False
    return True


def compilar_documento(nombre_clave, config):
    """Compila un entregable específico usando la biblioteca Typst."""
    entrada = config["entrada"]
    salidas = config["salidas"]
    nombre = config["nombre"]

    print(f"\n📄 Compilando: {nombre}")
    print(f"   Fuente Typst : {entrada.relative_to(WORKSPACE_ROOT)}")

    if not entrada.exists():
        print(f"❌ Error: Archivo de entrada no encontrado: {entrada}")
        return False

    inicio = time.time()
    try:
        # Primera salida principal
        primera_salida = salidas[0]
        primera_salida.parent.mkdir(parents=True, exist_ok=True)
        
        # Compilación con root establecido en el workspace para resolver rutas absolutas (/assets/...)
        typst.compile(
            str(entrada),
            output=str(primera_salida),
            root=str(WORKSPACE_ROOT)
        )
        
        duracion = time.time() - inicio
        tamano_kb = primera_salida.stat().st_size / 1024
        print(f"   ✅ PDF Generado: {primera_salida.relative_to(WORKSPACE_ROOT)} ({tamano_kb:.1f} KB) en {duracion:.2f}s")

        # Replicar a salidas adicionales si están definidas (ej. nombre canónico y nombre corrección)
        for salida_extra in salidas[1:]:
            salida_extra.parent.mkdir(parents=True, exist_ok=True)
            typst.compile(
                str(entrada),
                output=str(salida_extra),
                root=str(WORKSPACE_ROOT)
            )
            print(f"   ✅ Sincronizado : {salida_extra.relative_to(WORKSPACE_ROOT)}")

        return True

    except Exception as e:
        print(f"❌ Falló la compilación de {nombre}: {e}")
        return False


def compilar_todos(filtro=None):
    """Orquesta la compilación de todos los entregables o del filtro especificado."""
    print("=" * 75)
    print("🚀 PIPELINE DE COMPILACIÓN DOCS-AS-CODE — PLANEAMIENTO ORGANIZACIONAL")
    print("   Universidad Nacional del Comahue — CURZAS | Autor: Héctor Ayarachi")
    print("=" * 75)

    verificar_recursos()

    exitosos = 0
    total = 0

    objetivos = {}
    if filtro:
        filtro_normalizado = filtro.lower().replace("-", "_")
        for k, v in ENTREGABLES.items():
            if filtro_normalizado in k or filtro_normalizado in v["nombre"].lower():
                objetivos[k] = v
        if not objetivos:
            print(f"⚠️ No se encontró ningún entregable que coincida con: '{filtro}'")
            print(f"   Entregables disponibles: {list(ENTREGABLES.keys())}")
            return False
    else:
        objetivos = ENTREGABLES

    total = len(objetivos)
    for clave, config in objetivos.items():
        if compilar_documento(clave, config):
            exitosos += 1

    print("\n" + "=" * 75)
    if exitosos == total:
        print(f"🎉 COMPILACIÓN EXITOSA: {exitosos}/{total} entregables generados correctamente.")
    else:
        print(f"⚠️ COMPILACIÓN PARCIAL: {exitosos}/{total} entregables generados con éxito.")
    print("=" * 75)

    return exitosos == total


def main():
    parser = argparse.ArgumentParser(
        description="Pipeline central de compilación Typst a PDF para Planeamiento Organizacional."
    )
    parser.add_argument(
        "--target", "-t",
        choices=["actividad_01", "actividad_02", "1", "2", "all"],
        default="all",
        help="Entregable específico a compilar (por defecto: all)."
    )
    args = parser.parse_args()

    filtro = None
    if args.target in ["1", "actividad_01"]:
        filtro = "actividad_01"
    elif args.target in ["2", "actividad_02"]:
        filtro = "actividad_02"

    resultado = compilar_todos(filtro=filtro)
    sys.exit(0 if resultado else 1)


if __name__ == "__main__":
    main()
