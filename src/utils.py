import os, subprocess, yaml
from pathlib import Path

def load_config(path='config/config.yml'):
    with open(path,'r',encoding='utf-8') as f:
        return yaml.safe_load(f)

def ensure_dirs(cfg):
    for k in ['input_dir','frames_dir','colmap_workspace','meshes_dir']:
        p = Path(cfg['paths'][k]); p.mkdir(parents=True, exist_ok=True)

def run_cmd(cmd, shell=False):
    print('> Ejecutando:', ' '.join(cmd) if isinstance(cmd,list) else cmd)
    return subprocess.run(cmd, shell=shell)
