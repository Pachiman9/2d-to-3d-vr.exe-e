# Minimal GUI (PyQt6) - ejecutable generado por PyInstaller en GitHub Actions
import sys, subprocess, os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox

class MainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('2d-to-3d-vr - Minimal GUI')
        self.resize(700,320)
        layout = QtWidgets.QVBoxLayout(self)

        row = QtWidgets.QHBoxLayout()
        self.input_edit = QtWidgets.QLineEdit()
        btn_in = QtWidgets.QPushButton('Seleccionar input (carpeta o vídeo)')
        btn_in.clicked.connect(self.select_input)
        row.addWidget(self.input_edit); row.addWidget(btn_in)
        layout.addLayout(row)

        btns = QtWidgets.QHBoxLayout()
        self.btn_frames = QtWidgets.QPushButton('Extraer frames')
        self.btn_colmap = QtWidgets.QPushButton('Ejecutar COLMAP')
        self.btn_midas = QtWidgets.QPushButton('Depth MiDaS (placeholder)')
        self.btn_mesh = QtWidgets.QPushButton('Crear malla (placeholder)')
        self.btn_export = QtWidgets.QPushButton('Exportar GLB (placeholder)')

        btns.addWidget(self.btn_frames); btns.addWidget(self.btn_colmap)
        btns.addWidget(self.btn_midas); btns.addWidget(self.btn_mesh); btns.addWidget(self.btn_export)
        layout.addLayout(btns)

        self.log = QtWidgets.QTextEdit(); self.log.setReadOnly(True)
        layout.addWidget(self.log)

        self.btn_frames.clicked.connect(self.extract_frames)
        self.btn_colmap.clicked.connect(self.run_colmap)
        self.btn_midas.clicked.connect(self.run_midas)
        self.btn_mesh.clicked.connect(self.run_mesh)
        self.btn_export.clicked.connect(self.run_export)

    def log_msg(self, s):
        self.log.append(s); self.log.ensureCursorVisible()

    def select_input(self):
        path = QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta') or QFileDialog.getOpenFileName(self, 'Seleccionar archivo')[0]
        if path: self.input_edit.setText(path)

    def run_process(self, cmd, shell=False):
        self.log_msg(f"> {cmd}")
        try:
            proc = subprocess.run(cmd if isinstance(cmd,list) else cmd, shell=shell, capture_output=True, text=True)
            out = proc.stdout.strip() or proc.stderr.strip() or str(proc.returncode)
            self.log_msg(out)
        except Exception as e:
            self.log_msg('Error: ' + str(e))

    def extract_frames(self):
        path = self.input_edit.text().strip()
        if not path:
            QMessageBox.warning(self, 'Falta input', 'Selecciona un vídeo o carpeta primero.')
            return
        if os.path.isfile(path) and path.lower().endswith(('.mp4','.mov','.avi','.mkv')):
            cmd = [sys.executable, 'src/preprocess.py', '--video', path, '--out', 'data/frames', '--fps', '8']
        else:
            cmd = [sys.executable, 'src/preprocess.py', '--input', path, '--out', 'data/frames']
        self.run_process(cmd)

    def run_colmap(self):
        imgdir = 'data/frames'; workspace = 'data/colmap_workspace'
        cmd = ['src\\colmap_run.bat', imgdir, workspace]
        self.run_process(cmd, shell=True)

    def run_midas(self):
        cmd = [sys.executable, 'src/depth_midas.py', '--input', 'data/frames', '--out', 'data/frames_depth', '--model', 'models/midas_v21_small.pt']
        self.run_process(cmd)

    def run_mesh(self):
        cmd = [sys.executable, 'src/mesh_fuse.py', '--colmap_dense', 'data/colmap_workspace/dense', '--out_mesh', 'data/meshes/scene.obj']
        self.run_process(cmd)

    def run_export(self):
        cmd = [sys.executable, 'src/export_gltf.py', '--mesh', 'data/meshes/scene.obj', '--out', 'data/output/scene.glb']
        self.run_process(cmd)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWin(); w.show()
    sys.exit(app.exec())
