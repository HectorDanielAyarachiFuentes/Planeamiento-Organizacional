# PowerShell Script: Compilación Rápida Docs-as-Code — Planeamiento Organizacional
param (
    [string]$Target = "all"
)

Write-Host "Iniciando compilador de entregables Typst..." -ForegroundColor Cyan
python compilar_todos.py --target $Target

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Compilación finalizada exitosamente." -ForegroundColor Green
} else {
    Write-Host "`n❌ Error en la compilación de documentos." -ForegroundColor Red
}
