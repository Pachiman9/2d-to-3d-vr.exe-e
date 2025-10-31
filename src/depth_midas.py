import os, argparse
from pathlib import Path
from PIL import Image
import numpy as np

def placeholder_process(input_dir, out_dir, model_path):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    imgs = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg','.png'))]
    for i,f in enumerate(sorted(imgs)):
        im = Image.open(os.path.join(input_dir,f)).convert('L')
        arr = np.array(im)
        grad = np.linspace(0,255,arr.shape[1], dtype=np.uint8)
        fake = np.tile(grad, (arr.shape[0],1))
        Image.fromarray(fake).save(os.path.join(out_dir, f'depth_{i:05d}.png'))
    print('Depth maps (placeholder) generados en', out_dir)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/frames'); parser.add_argument('--out', default='data/frames_depth')
    parser.add_argument('--model', default='models/midas_v21_small.pt')
    args = parser.parse_args()
    if os.path.exists(args.model):
        print('Modelo encontrado:', args.model)
    else:
        print('Modelo no encontrado. Ejecutando placeholder.')
    placeholder_process(args.input, args.out, args.model)
