import argparse, os
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='data/frames')
    parser.add_argument('--out', default='models/nerf_checkpoints')
    args = parser.parse_args()
    os.makedirs(args.out, exist_ok=True)
    print('Placeholder: aquí llamarías a instant-ngp / nerfstudio con los datos en', args.data)
    print('Salida prevista en', args.out)
