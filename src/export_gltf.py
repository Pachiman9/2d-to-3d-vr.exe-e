import argparse, os
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mesh', default='data/meshes/scene.obj')
    parser.add_argument('--out', default='data/output/scene.glb')
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    if os.path.exists(args.mesh):
        print('Exportando (placeholder) {} -> {}'.format(args.mesh, args.out))
        open(args.out,'wb').write(b'GLB_PLACEHOLDER')
    else:
        print('Malla no encontrada:', args.mesh)
