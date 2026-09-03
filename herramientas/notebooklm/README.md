# 🛠️ Herramientas · Google NotebookLM MCP

Este directorio centraliza los recursos, documentación técnica, utilidades de autenticación y material tutorial de **Google NotebookLM** integrado a través del protocolo MCP en **Antigravity IDE**.

---

## 📁 Estructura del Módulo

```text
herramientas/notebooklm/
├── README.md               # Guía de referencia rápida y documentación de uso
├── docs/                   # Guías técnicas y documentación de integración MCP
│   └── notebooklm_mcp_guide.md
├── scripts/                # Scripts de soporte y autenticación
│   ├── auth_helper.py      # Asistente CLI para renovación rápida de tokens
│   └── cookies.txt         # Archivo local para pegar cabeceras cookie (ignorado en git)
└── tutoriales/             # Videos tutoriales y transcripciones operativas
    ├── NotebookLM acaba de mejorar x10 Antigravity.mp4
    ├── Tutorial.txt
    └── VIdeo.txt
```

---

## ⚙️ Integración con NotebookLM MCP

La configuración del servidor MCP se encuentra centralizada a nivel del espacio de trabajo en `.agents/mcp_config.json`:

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "C:\\Users\\Ramoncito\\.local\\bin\\notebooklm-mcp.exe"
    }
  }
}
```

---

## 🛠️ Renovación de Credenciales / Autenticación

Si la sesión de NotebookLM expira (error `401 Unauthorized`):

1. **Método Rápido (Script Local):**
   Copia las cabeceras `cookie:` desde DevTools (`F12` -> `Network` -> `batchexecute` -> `cookie:`) o pégalas en `herramientas/notebooklm/scripts/cookies.txt` y ejecuta:
   ```powershell
   python herramientas/notebooklm/scripts/auth_helper.py
   ```

2. **Método Directo con Navegador:**
   ```powershell
   notebooklm-mcp-auth
   ```
