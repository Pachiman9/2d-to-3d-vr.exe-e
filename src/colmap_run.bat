@echo off
REM Wrapper mínimo para ejecutar COLMAP en Windows. Asume colmap.exe en PATH.
SET IMAGE_DIR=%~1
SET WORKSPACE=%~2

if "%IMAGE_DIR%"=="" (
    echo Uso: colmap_run.bat path\to\images path\to\workspace
    exit /b 1
)

if "%WORKSPACE%"=="" (
    set WORKSPACE=.\data\colmap_workspace
)

echo IMAGE_DIR=%IMAGE_DIR%
echo WORKSPACE=%WORKSPACE%

mkdir "%WORKSPACE%\sparse" 2>nul
mkdir "%WORKSPACE%\dense" 2>nul

colmap feature_extractor --database_path "%WORKSPACE%\database.db" --image_path "%IMAGE_DIR%"
colmap exhaustive_matcher --database_path "%WORKSPACE%\database.db"
colmap mapper --database_path "%WORKSPACE%\database.db" --image_path "%IMAGE_DIR%" --output_path "%WORKSPACE%\sparse"
colmap image_undistorter --image_path "%IMAGE_DIR%" --input_path "%WORKSPACE%\sparse\0" --output_path "%WORKSPACE%\dense" --output_type COLMAP
colmap patch_match_stereo --workspace_path "%WORKSPACE%\dense" --PatchMatchStereo.geom_consistency true
colmap stereo_fusion --workspace_path "%WORKSPACE%\dense" --output_path "%WORKSPACE%\dense\fused.ply"

echo COLMAP terminado. Salida en %WORKSPACE%\dense
