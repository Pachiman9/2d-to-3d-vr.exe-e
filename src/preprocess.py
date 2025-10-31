import cv2, os, sys
from pathlib import Path
import argparse

def extract_frames(video_path, out_dir, fps=8):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    vid = cv2.VideoCapture(video_path)
    if not vid.isOpened():
        print('No se pudo abrir el vídeo:', video_path); return
    video_fps = vid.get(cv2.CAP_PROP_FPS) or fps
    step = max(1, int(round(video_fps / fps)))
    idx = 0; saved = 0
    while True:
        ok, frame = vid.read()
        if not ok: break
        if idx % step == 0:
            fname = os.path.join(out_dir, f'frame_{saved:05d}.jpg')
            cv2.imwrite(fname, frame); saved += 1
        idx += 1
    print(f'Frames guardados: {saved} en {out_dir}')

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', required=False, help='ruta a video')
    parser.add_argument('--input', required=False, help='carpeta de imágenes (copiaré a frames)')
    parser.add_argument('--out', default='data/frames')
    parser.add_argument('--fps', type=int, default=8)
    args = parser.parse_args()
    if args.video: extract_frames(args.video, args.out, args.fps)
    elif args.input:
        from shutil import copy2
        Path(args.out).mkdir(parents=True, exist_ok=True)
        files = [f for f in os.listdir(args.input) if f.lower().endswith(('.jpg','.png','.jpeg'))]
        for i,f in enumerate(sorted(files)):
            copy2(os.path.join(args.input,f), os.path.join(args.out,f'frame_{i:05d}.jpg'))
        print(f'Copiadas {len(files)} imágenes a {args.out}')
    else:
        print('No input provided. Use --video or --input.')
