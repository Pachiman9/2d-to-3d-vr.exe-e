# 2d-to-3d-vr

Proyecto minimalista para convertir imágenes 2D (foto/video) a 3D para VR — edición Windows con GUI mínima.
El repositorio está preparado para que GitHub Actions genere automáticamente un ejecutable portable `2d-to-3d-vr.exe`.

## Qué hace este repo
- GUI minimalista en PyQt6 (`main.py`) que lanza las etapas del flujo (frames -> COLMAP -> depth -> mesh -> export).
- Scripts esqueleto en `src/` que actúan como hooks para que añadas tus implementaciones reales (MiDaS, instant-ngp, OpenMVS...).
- Workflow en `.github/workflows/build.yml` que compila con PyInstaller en runner Windows y sube el `.exe` como artifact.

## Importante
- **NO** se incluyen modelos (MiDaS, checkpoints NeRF, etc.). Colócalos manualmente en `models/` una vez descargados.
- COLMAP no está incluido: instala COLMAP en Windows y añádelo a PATH si quieres usar esa etapa desde la GUI.

## Cómo usar
1. Subir este repositorio a GitHub (repo llamado `2d-to-3d-vr` en tu cuenta).
2. Hacer `push` a la rama `main` — GitHub Actions en `windows-latest` construirá el `.exe` y lo dejará como artifact.
3. Descargar artifact: Actions → Build Portable EXE → Artifacts → `2d-to-3d-vr`.
4. Descargar y colocar modelos en `models/` si los necesitas para producción.

## Estructura
```
2d-to-3d-vr/
├─ .github/workflows/build.yml
├─ main.py
├─ requirements.txt
├─ src/
├─ config/config.yml
├─ models/.gitkeep
└─ README.md
```
